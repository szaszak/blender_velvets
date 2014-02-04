bl_info = {
    "name": "velvet_revolver ::",
    "description": "Mass-create proxies and/or transcode to equalize FPSs",
    "author": "qazav_szaszak",
    "version": (1, 0, 20140203),
    "blender": (2, 69, 0),
    "warning": "Current in test phase",
    "category": ":",
    "location": "File > Export > Velvet Revolver",
    "support": "COMMUNITY"}

import bpy

from shutil import which
from subprocess import call

from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty

import glob
import os

print("-------------------------------------------")

#ffCommand = "C:\Documents and Settings\FFreitas.CTI\Meus documentos\HCKR\FFMPEG\bin\ffmpeg.exe"


class VideoSource(object):
    def __init__(self, ffCommand, filepath, v_source, v_format, fps, deinter, ar, ac, v_output):
        self.ffCommand = ffCommand
        self.input = v_source
        self.filepath = filepath
        self.fps = str(round(fps, 3))
        self.arate = str(ar)
        self.output = v_output

        if deinter:
            self.deinter = "-vf yadif"
        else:
            self.deinter = ""

        if ac:
            self.achannels = "-ac 1"
        else:
            self.achannels = ""

        if v_format == "proxy": # can be proxy, prores422 or mjpeg
            self.format = "-s 640x368 -c:v mjpeg -qscale 5 -acodec pcm_s16be"
            #self.format = "-s 640x368 -f image2 -c:v prores_ks -profile:v 0 -qscale:v 13"
            #self.format = "-s 640x368 -c:v prores -profile:v 0 -qscale:v 13"
            #ffmpeg -y -probesize 5000000 -f image2 -r 48 -force_fps -i ${DPX_HERO} -c:v prores_ks -profile:v 3 -qscale:v ${QSCALE} -vendor ap10 -pix_fmt yuv422p10le -s 2048x1152 -r 48 output.mov
        elif v_format == "prores422":
            self.format = "-probesize 5000000 -f image2 -c:v prores_ks -profile:v 3 -qscale:v 5 -vendor ap10 -pix_fmt yuv422p10le"
        else: # v_format == "mjpeg"
            self.format = "-probesize 5000000 -f image2 -c:v mjpeg -qscale:v 1 -vendor ap10 -pix_fmt yuvj422p -acodec pcm_s16be"

    def runFF(self):
        # Due to spaces, the command entries (ffCommand, input and output) have
        # to be read as strings by the call command, thus the escapings below
        callFFMPEG = "\"%s\" -i \"%s\" -y %s -r %s %s -ar %s %s %s" \
                     % (self.ffCommand, self.input, self.format, self.fps, self.deinter, self.arate, self.achannels, self.output)

        print(callFFMPEG)
        call(callFFMPEG, shell=True)


######## ----------------------------------------------------------------------
######## EXPORT TO ARDOUR
######## ----------------------------------------------------------------------

from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, EnumProperty, IntProperty, FloatProperty, BoolProperty


class VelvetRevolver(bpy.types.Operator, ExportHelper):
    """Mass create proxies and/or ProRes422//MJPEG from original files"""
    bl_idname = "export.revolver"
    bl_label = "Export to Revolver"
    filename_ext = ".revolver"
    filter_glob = StringProperty(subtype='FILE_PATH')

######## ----------------------------------------------------------------------

    transcode_items = (
        ('do_not_transcode', 'Do not create copies', ''),
        ('transcode_prores', 'in ProRes422', ''),
        ('transcode_mjpeg', 'in MJPEG', '')
    )

    proxies = BoolProperty(
            name="Proxies at SD resolution",
            description="Create Standard Definition 480p proxies with custom FPS set below",
            default=False,
            )
    transcode = EnumProperty(
            name="Copies",
            default="do_not_transcode",
            description="Also create copies in this format for final render (slow)",
            items=transcode_items
            )
    prop_fps = FloatProperty(
            name="FPS (Beware!)",
            description="Transcoded videos will have this FPS - this *MUST* be the same as your project",
            default=24.00
            )
    prop_ar = IntProperty(
            name="Audio Sample Rate",
            description="Transcoded videos will have this audio rate",
            default=48000
            )
    prop_deint = BoolProperty(
            name="Deinterlace videos",
            description="Uses FFMPEG Yadif filter to deinterlace all videos",
            default=False,
            )
    prop_ac = BoolProperty(
            name="Force mono audio?",
            description="Forces FFMPEG to transcode videos to mono - easier panning in Blender, but usually not recommended",
            default=False,
            )


    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.label('What to do in selected folder?')
        box.label('Create proxies:')
        box.prop(self, 'proxies')
        box.label('Create copies of source videos:')
        box.prop(self, 'transcode')
        box = layout.box()
        box.label('Properties for videos:')
        box.label('FPS *must* be the same as project\'s!')
        box.prop(self, 'prop_fps')
        box.prop(self, 'prop_ar')
        box.prop(self, 'prop_deint')
        box.prop(self, 'prop_ac')


######## ----------------------------------------------------------------------
    
    @classmethod
    def poll(cls, context):
        if bpy.context.sequences:
            return context.sequences is not None

    def execute(self, context):
        bpy.ops.file.make_paths_absolute()

        preferences = bpy.context.user_preferences
        ffCommand = preferences.addons['velvet_revolver'].preferences.ffCommand
        
        videosFolderPath, blenderFile = os.path.split(self.filepath)
        videosFolderPath += os.sep
        #print(videosFolderPath)

        sources = []
        for i in glob.glob(videosFolderPath + "*.*"):
            if i[-4:].lower() in bpy.path.extensions_movie:
                sources.append(i)

        #print(sources)

        if self.proxies:
            for source in sources:
                print(source)
                #vs = VideoSource(ffCommand, filepath, input, format, fps, deinter, audioRate, audioChannels, output)
                #ext = source[-4:]
                output_v = source[:-4] + "_proxy.mkv"
                vs = VideoSource(ffCommand, videosFolderPath, source, "proxy", self.prop_fps, self.prop_deint, self.prop_ar, self.prop_ac, output_v)
                vs.runFF()

        return {'FINISHED'}

        #return main(self.filepath, ffCommand, input, format, fps, deinter, audioRate, audioChannels, output)
        #ffCommand, self.filepath, self.create_proxies, self.transcode_videos, self.video_properties_fps, self.video_properties_deinterlace, self.audio_properties_samplerate, self.audio_properties_channels)
        #ffCommand, filepath, input, format, fps, deinter, audioRate, audioChannels, output


class Velvet_Revolver_Transcoder(bpy.types.AddonPreferences):
    bl_idname = __name__.split(".")[0]
    bl_option = {'REGISTER'}

    if which('ffmpeg') is not None:
        ffmpeg = which('ffmpeg')
    else:
        ffmpeg = "/usr/bin/ffmpeg"

    ffCommand = StringProperty(
        name="Path to FFMPEG binary or executable",
        description="If you have a local FFMPEG, change this path",
        subtype='FILE_PATH',
        default=ffmpeg,
    )

    def draw(self, context):

        layout = self.layout
        layout.label(text="The path below *must* be absolute. If you have to "
                          "change it, do so with no .blend files open or "
                          "they will be relative.")
        layout.prop(self, "ffCommand")


def menuEntry(self, context):
    self.layout.operator(VelvetRevolver.bl_idname, text="Revolver (.revolver)")


def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_export.append(menuEntry)


def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_export.remove(menuEntry)


if __name__ == "__main__":
    register()
