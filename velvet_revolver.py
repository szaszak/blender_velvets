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

# <pep8 compliant>

bl_info = {
    "name": "velvet_revolver ::",
    "description": "Mass-create proxies and/or transcode to equalize FPSs",
    "author": "qazav_szaszak",
    "version": (1, 0, 20140403),
    "blender": (2, 69, 0),
    "warning": "Bang! Bang! That awful sound.",
    "category": ":",
    "location": "File > Export > Revolver (.revolver)",
    "support": "COMMUNITY"}

import bpy
from subprocess import call


class VideoSource(object):
    """Uses video source to run FFMPEG and create
       proxies or full-res intra-frame copies"""
    def __init__(self, ffCommand, filepath, v_source, v_res, v_format,
                 fps, deinter, ar, ac):
        self.ffCommand = ffCommand
        self.input = v_source
        self.filepath = filepath
        self.fps = str(round(fps, 3))
        self.arate = str(ar)

        if deinter:
            self.deinter = "-vf yadif"
        else:
            self.deinter = ""

        if ac:
            self.achannels = "-ac 1"
        else:
            self.achannels = ""

        if v_res == "proxy":
            self.v_output = self.input[:-4] + "_proxy.mov"
            if v_format == "is_prores":
                self.format = "-probesize 5000000 -s 640x368 -c:v prores \
                               -profile:v 0 -qscale:v 13 -vendor ap10 \
                               -pix_fmt yuv422p10le -acodec pcm_s16be"
            else:  # v_format == "is_mjpeg":
                self.format = "-probesize 5000000 -s 640x368 -c:v mjpeg \
                               -qscale:v 5 -acodec pcm_s16be"
        else:  # v_res == "fullres"
            if v_format == "is_prores":
                self.v_output = self.input[:-4] + "_PRORES.mov"
                self.format = "-probesize 5000000 -c:v prores -profile:v 3 \
                               -qscale:v 5 -vendor ap10 -pix_fmt yuv422p10le \
                               -acodec pcm_s16be"
            else:  # v_format == "is_mjpeg":
                self.v_output = self.input[:-4] + "_MJPEG.mov"
                self.format = "-probesize 5000000 -c:v mjpeg -qscale:v 1 \
                               -acodec pcm_s16be"

    def runFF(self):
        # Due to spaces, the command entries (ffCommand, input and output) have
        # to be read as strings by the call command, thus the escapings below
        callFFMPEG = "\"%s\" -i \"%s\" -y %s -r %s %s -ar %s %s \"%s\"" \
                     % (self.ffCommand, self.input, self.format, self.fps,
                        self.deinter, self.arate, self.achannels, self.v_output)

        print(callFFMPEG)
        call(callFFMPEG, shell=True)


######## ----------------------------------------------------------------------
######## VELVET REVOLVER MAIN CLASS
######## ----------------------------------------------------------------------

from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, EnumProperty, IntProperty, FloatProperty, BoolProperty
from shutil import which

import glob
import os


class VelvetRevolver(bpy.types.Operator, ExportHelper):
    """Mass create proxies and/or intra-frame copies from original files"""
    bl_idname = "export.revolver"
    bl_label = "Export to Revolver"
    filename_ext = ".revolver"
    filter_movie = BoolProperty(default=True, options={'HIDDEN'})

######## ----------------------------------------------------------------------

    transcode_items = (
        ('is_prores', 'ProRes422', ''),
        ('is_mjpeg', 'MJPEG', '')
    )

######## ----------------------------------------------------------------------

    proxies = BoolProperty(
        name="Create proxies at SD resolution",
        description="Create Standard Definition 480p \
                    proxies with custom FPS set below",
        default=False,
    )
    copies = BoolProperty(
        name="Create copies in intra-frame codec",
        description="Create full res copies of sources \
                    in an intra-frame codec (slow)",
        default=False,
    )
    v_format = EnumProperty(
        name="Format",
        default="is_prores",
        description="Intra-frame format for the creation \
                    of proxies and/or copies",
        items=transcode_items
    )
    prop_fps = FloatProperty(
        name="FPS (Beware!)",
        description="Transcoded videos will have this FPS - \
                    this *MUST* be the same as your project",
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
        description="Forces FFMPEG to transcode videos to mono - easier \
                    panning in Blender, but usually not recommended",
        default=False,
    )

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.label('What to do in selected folder?')
        box.prop(self, 'proxies')
        box.prop(self, 'copies')
        box.label('Proxies and/or copies should be in:')
        box.prop(self, 'v_format')
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
        if bpy.data.scenes:
            return bpy.data.scenes is not None

    def execute(self, context):
        preferences = bpy.context.user_preferences
        ffCommand = preferences.addons['velvet_revolver'].preferences.ffCommand

        videosFolderPath, blenderFile = os.path.split(self.filepath)
        videosFolderPath += os.sep

        sources = []
        for i in glob.glob(videosFolderPath + "*.*"):
            if i[-4:].lower() in bpy.path.extensions_movie:
                if "_proxy." not in i and "_MJPEG." not in i and "_PRORES." not in i:
                    sources.append(i)

        if self.proxies:
            for source in sources:
                v_res = "proxy"
                vs = VideoSource(ffCommand, videosFolderPath, source, v_res,
                                 self.v_format, self.prop_fps, self.prop_deint,
                                 self.prop_ar, self.prop_ac)
                vs.runFF()

        if self.copies:
            for source in sources:
                v_res = "fullres"
                vs = VideoSource(ffCommand, videosFolderPath, source, v_res,
                                 self.v_format, self.prop_fps, self.prop_deint,
                                 self.prop_ar, self.prop_ac)
                vs.runFF()

        return {'FINISHED'}


class Velvet_Revolver_Transcoder(bpy.types.AddonPreferences):
    """Velver Revolver preferences"""
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
