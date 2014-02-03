# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


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

print("-------------------------------------------")

#ffCommand = "C:\Documents and Settings\FFreitas.CTI\Meus documentos\HCKR\FFMPEG\bin\ffmpeg.exe"


class FF(object):    
    def __init__(self, ffCommand, input, format, fps, deinter, audioRate, audioChannels, output):
        self.ffCommand = ffCommand
        self.input = input
        self.format = format # can be proxy
        self.fps = fps
        self.deinter = deinter
        self.arate = audioRate
        self.achannels = audioChannels
        self.output = output
        
    def runFF(self):        
        # Due to spaces, the command entries (ffCommand, input and output) have
        # to be read as strings by the call command, thus the escapings below
        callFFMPEG = "\"%s\" -i \"%s\" -y \"%s\" -r:v \"%s\" \"%s\" -ar \"%s\" -ac \"%s\" \"%s\"" \
                     % (self.ffCommand, self.input, self.format, self.fps, self.deinter, self.arate, self.achannels, self.output)
                     
        print(callFFMPEG)


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

    create_proxies = BoolProperty(
            name="Proxies at SD resolution",
            description="Create Standard Definition 480p proxies with custom FPS set below",
            default=False,
            )
    #transcode_videos_prores = BoolProperty(
    #        name="ProRes422",
    #        description="Transcode to ProRes422 - keeps original resolution, uses custom FPS set below",
    #        default=False,
    #        )
    #transcode_videos_mjpeg = BoolProperty(
    #        name="MJPEG",
    #        description="Transcode to MJPEG - keeps original resolution, uses custom FPS set below",
    #        default=False,
    #        )                
    transcode_videos = EnumProperty(
            name="Copies",
            default="do_not_transcode",
            description="Also create copies in this format for final render (slow)",
            items=transcode_items
            )    
    video_properties_fps = FloatProperty(
            name="FPS (Beware!)",
            description="Transcoded videos will have this FPS - this *MUST* be the same as your project",
            default=24.00
            )
    audio_properties_samplerate = IntProperty(
            name="Audio Sample Rate",
            description="Transcoded videos will have this audio rate",
            default=48000
            )
    video_properties_deinterlace = BoolProperty(
            name="Deinterlace videos",
            description="Uses FFMPEG Yadif filter to deinterlace all videos",
            default=False,
            )
    audio_properties_channels = BoolProperty(
            name="Force mono audio?",
            description="Forces FFMPEG to transcode videos to mono - easier panning in Blender, but usually not recommended",
            default=False,
            )

            
    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.label('What to do in selected folder?')
        box.label('Create proxies:')
        box.prop(self, 'create_proxies')
        box.label('Create copies of source videos:')
        box.prop(self, 'transcode_videos')
        #box.prop(self, 'transcode_videos_prores')
        #box.prop(self, 'transcode_videos_mjpeg')
        box = layout.box()
        box.label('Properties for videos:')
        box.label('FPS *must* be the same as project\'s!')
        box.prop(self, 'video_properties_fps')
        box.prop(self, 'audio_properties_samplerate')
        box.prop(self, 'video_properties_deinterlace')
        box.prop(self, 'audio_properties_channels')


######## ----------------------------------------------------------------------
    
    @classmethod
    def poll(cls, context):
        if bpy.context.sequences:
            return context.sequences is not None

    def execute(self, context):
        bpy.ops.file.make_paths_absolute()
        
        render = bpy.context.scene.render
        fps = round((render.fps / render.fps_base), 3)

        scene = bpy.context.scene
        startFrame = scene.frame_start
        endFrame = scene.frame_end
        fps, timecode = checkFPS()

        preferences = bpy.context.user_preferences
        system = preferences.system
        audioRate = int(system.audio_sample_rate.split("_")[1])

        audiosFolderPath, ardourFile = os.path.split(self.filepath)
        ardourBasename = os.path.splitext(ardourFile)[0]
        audiosFolder = audiosFolderPath + os.sep + "Audios_for_" + ardourBasename

        sources = []
        Session, sources = createXML(sources, startFrame, endFrame, fps,
                                     timecode, audioRate, ardourBasename,
                                     audiosFolder)

        ffCommand = preferences.addons['velvet_revolver'].preferences.ffCommand
        runFFMPEG(ffCommand, sources, audioRate, audiosFolder)

        writeXML(self.filepath, Session)

        return main(self.filepath, context, self.include_animation, self.include_active_cam, self.include_selected_cams, self.include_selected_objects, self.include_cam_bundles)
        #return {'FINISHED'}


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
    #ffDefaultFPS = StringProperty(
    #    name="Default FPS to be used by FFMPEG for transcoding:",
     #   description="This is the default FPS used for creting proxies or transcoding to ProRes422/MJPEG",
        #subtype='FILE_PATH',
      #  default='24.00',
    #)

    def draw(self, context):
    
        layout = self.layout
        layout.label(text="The path below *must* be absolute. If you have to "
                          "change it, do so with no .blend files open or "
                          "they will be relative.")
        layout.prop(self, "ffCommand")
     #   layout = self.layout        
      #  layout.prop(self, "ffDefaultFPS")


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
