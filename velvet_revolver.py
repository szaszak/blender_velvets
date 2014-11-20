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
    "version": (1, 0, 20141120),
    "blender": (2, 69, 0),
    "warning": "Bang! Bang! That awful sound.",
    "category": ":",
    "location": "File > External Data > Velvet Revolver",
    "url": "blendervelvets.org",
    "support": "COMMUNITY"}

import bpy
import os
import glob
from subprocess import call


######## ----------------------------------------------------------------------
######## VSE TIMELINE TOGGLE PROXIES <-> FULLRES
######## ----------------------------------------------------------------------

class Proxy_Editing_ToProxy(bpy.types.Operator):
    """Change filepaths of current strips to proxy files (_proxy.mov)"""
    bl_idname = "sequencer.proxy_editing_toproxy"
    bl_label = "Proxy Editing - Change to Proxies"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcuts: Ctrl + Alt + P

    @classmethod
    def poll(cls, context):
        if bpy.context.sequences:
            return bpy.context.sequences is not None

    def execute(self, context):

        # Making strips' paths absolute is necessary for script's execution.
        bpy.ops.file.make_paths_absolute()

        proxy_end = "_proxy.mov"
        prores_end = "_PRORES.mov"
        mjpeg_end = "_MJPEG.mov"

        for s in bpy.context.sequences:
            if (s.type == "SOUND") or (s.type == "MOVIE"):
                f_name = s.filepath[:-10]

                # if strip is already a proxy, do nothing
                if s.filepath.endswith(proxy_end):
                    print("Strip '" + s.filepath + "' is already a proxy.")
                    pass
                # or strip is a fullres that has correspondent proxy files
                elif s.filepath.endswith(prores_end) and \
                        os.path.isfile(f_name[:-1] + proxy_end):
                    s.filepath = f_name[:-1] + proxy_end
                    print("Proxy file for '" + s.filepath + "' is OK.")
                elif s.filepath.endswith(mjpeg_end) and \
                        os.path.isfile(f_name + proxy_end):
                    s.filepath = f_name + proxy_end
                    print("Proxy file for '" + s.filepath + "' is OK.")
                else:
                    # for fullres files without _PRORES or _MJPEG in their name
                    ext_len = len(s.filepath.split(".")[-1]) + 1
                    # search in folder for any file with the same name appended
                    # by "_proxy" and with recognizeable movie extension
                    if glob.glob(s.filepath[:-ext_len] + "_proxy.*") and \
                            s.filepath[-ext_len:].lower() in bpy.path.extensions_movie:
                        s.filepath = glob.glob(s.filepath[:-ext_len] + "_proxy.*")[0]
                        print("Proxy file for '" + s.filepath + "' is OK.")
                    else:
                        print("No proxy file found for '" + s.filepath + "'.")
                        pass

        # Make all paths relative; behaviour tends to be standard in Blender
        bpy.ops.file.make_paths_relative()

        return {'FINISHED'}


class Proxy_Editing_ToFullRes(bpy.types.Operator):
    """Change filepaths of current strips back to full-resolution files"""
    bl_idname = "sequencer.proxy_editing_tofullres"
    bl_label = "Proxy Editing - Change to Full Resolution"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcuts: Ctrl + Shift + P

    @classmethod
    def poll(cls, context):
        if bpy.context.sequences:
            return bpy.context.sequences is not None

    def execute(self, context):

        # Making strips' paths absolute is necessary for script's execution.
        bpy.ops.file.make_paths_absolute()
        
        proxy_end = "_proxy.mov"
        prores_end = "_PRORES.mov"
        mjpeg_end = "_MJPEG.mov"

        for s in bpy.context.sequences:
            if (s.type == "SOUND") or (s.type == "MOVIE"):
                f_name = s.filepath[:-10]

                # if strip is a proxy and has correspondent fullres files
                if s.filepath.endswith(proxy_end):
                    print("Checking full-res file for '" + s.filepath + "'...")
                    if os.path.isfile(f_name + prores_end):
                        s.filepath = f_name + prores_end
                        print("OK.")
                    elif os.path.isfile(f_name + mjpeg_end):
                        s.filepath = f_name + mjpeg_end
                        print("OK.")
                    elif glob.glob(s.filepath[:-10] + ".*"):
                        # if strip's filepath doesn't end with '_MJPEG.mov' or
                        # '_PRORES.mov', script will look for files in folder
                        # with the same name as the strip in the timeline,
                        # independent of file's extension (ie. .mov, .avi etc).
                        s.filepath = glob.glob(s.filepath[:-10] + ".*")[0]
                        print("OK.")
                    else:
                        print("No full-res file found for" + f_name + ".")
                        pass
                else:
                    print("Strip " + s.filepath + " is not a proxy.")
                    pass

        # Make all paths relative; behaviour tends to be standard in Blender
        bpy.ops.file.make_paths_relative()

        return {'FINISHED'}


######## ----------------------------------------------------------------------
######## FFMPEG TRANSCODING
######## ----------------------------------------------------------------------

class VideoSource(object):
    """Uses video source to run FFMPEG and create
       proxies or full-res intra-frame copies"""
    def __init__(self, ffCommand, filepath, v_source, v_res, v_format,
                 fps, deinter, ar, ac):
        self.ffCommand = ffCommand
        self.input = v_source
        self.filepath = filepath
        self.fps = fps
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
            # Proxy files generated by Velvet Revolver end with "_proxy.mov"
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

        return {'FINISHED'}


######## ----------------------------------------------------------------------
######## VELVET REVOLVER MAIN CLASS
######## ----------------------------------------------------------------------

from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, EnumProperty, IntProperty, FloatProperty, BoolProperty
from shutil import which


class VelvetRevolver(bpy.types.Operator, ExportHelper):
    """Mass create proxies and/or intra-frame copies from original files"""
    bl_idname = "export.revolver"
    bl_label = "Export to Revolver"
    filename_ext = ".revolver"

    transcode_items = (
        ('is_prores', 'ProRes422', ''),
        ('is_mjpeg', 'MJPEG', '')
    )

    proxies = BoolProperty(
        name="360p proxies",
        description="Create 640x368 proxies with same FPS as current scene",
        default=False,
    )
    copies = BoolProperty(
        name="Full-res copies in intra-frame codec",
        description="Create full-res copies with same FPS as current scene (slow)",
        default=False,
    )
    v_format = EnumProperty(
        name="Format",
        default="is_prores",
        description="Intra-frame format for the creation of proxies and/or copies",
        items=transcode_items
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
        render = context.scene.render
        fps = render.fps / render.fps_base

        layout = self.layout
        box = layout.box()
        box.label('What to do in selected folder? Create...')
        box.prop(self, 'proxies')
        box.prop(self, 'copies')
        box.label('Proxies and/or copies should be in:')
        box.prop(self, 'v_format')
        box.label("Resulting videos will have %.2f FPS." % fps)
        box.label("You can change the FPS at Properties.")

        box = layout.box()
        box.label('Properties for videos:')
        box.prop(self, 'prop_ar')
        box.prop(self, 'prop_deint')
        box.prop(self, 'prop_ac')

    @classmethod
    def poll(cls, context):
        if bpy.data.scenes:
            return bpy.data.scenes is not None

    def execute(self, context):
        preferences = bpy.context.user_preferences
        ffCommand = preferences.addons['velvet_revolver'].preferences.ffCommand

        videosFolderPath, blenderFile = os.path.split(self.filepath)
        videosFolderPath += os.sep

        render = context.scene.render
        fps = render.fps / render.fps_base

        sources = []
        for i in glob.glob(videosFolderPath + "*.*"):
            if i[-4:].lower() in bpy.path.extensions_movie:
                if "_proxy." not in i and "_MJPEG." not in i and "_PRORES." not in i:
                    sources.append(i)

        if self.proxies:
            for source in sources:
                v_res = "proxy"
                vs = VideoSource(ffCommand, videosFolderPath, source, v_res,
                                 self.v_format, fps, self.prop_deint,
                                 self.prop_ar, self.prop_ac)
                vs.runFF()

        if self.copies:
            for source in sources:
                v_res = "fullres"
                vs = VideoSource(ffCommand, videosFolderPath, source, v_res,
                                 self.v_format, fps, self.prop_deint,
                                 self.prop_ar, self.prop_ac)
                vs.runFF()

        if not self.proxies and not self.copies:
            print("No action selected for Velvet Revolver. Aborting.")

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
    self.layout.operator(VelvetRevolver.bl_idname, text="Velvet Revolver")


revolver_keymaps = []


def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_external_data.append(menuEntry)

    # Register shortcut for Proxy_Editing
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new('Sequencer', space_type='SEQUENCE_EDITOR', region_type='WINDOW', modal=False)
    kmi = km.keymap_items.new(Proxy_Editing_ToFullRes.bl_idname, 'P', 'PRESS', shift=True, ctrl=True)
    kmi = km.keymap_items.new(Proxy_Editing_ToProxy.bl_idname, 'P', 'PRESS', ctrl=True, alt=True)
    revolver_keymaps.append((km, kmi))


def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_external_data.remove(menuEntry)

    # Unregister Proxy_Editing shortcut
    for km, kmi in revolver_keymaps:
        km.keymap_items.remove(kmi)
    revolver_keymaps.clear()


if __name__ == "__main__":
    register()
