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
    "author": "szaszak - http://blendervelvets.org",
    "version": (2, 0, 20191007),
    "blender": (2, 80, 0),
    "warning": "Bang! Bang! That awful sound.",
    "category": ":",
    "location": "File > External Data > Velvet Revolver",
    "support": "COMMUNITY"}

import bpy
import os
import glob
from subprocess import call
from shutil import which
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, EnumProperty, IntProperty, FloatProperty, BoolProperty

######## ----------------------------------------------------------------------
######## VSE TIMELINE TOGGLE PROXIES <-> FULLRES
######## ----------------------------------------------------------------------

class Proxy_Editing_ToProxy(bpy.types.Operator):
    """Change filepaths of current strips to proxy files (_proxy.mov)"""
    bl_idname = "sequencer.proxy_editing_toproxy"
    bl_label = "Proxy Editing - Change to Proxies"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcuts: Ctrl + Alt + Shift + P

    @classmethod
    def poll(cls, context):
        if bpy.context.sequences:
            return bpy.context.sequences is not None

    def execute(self, context):

        # Making strips' paths absolute is necessary for script's execution.
        bpy.ops.file.make_paths_absolute()

        def checkProxyFile(f_path, ref):
            ''' Checks for (and returns) correspondent proxy file that may or
            may not have the same extension as the original full_res file '''
            base_path, ext = os.path.splitext(f_path)
            proxy_file = base_path[:ref] + "_proxy" + ext
            # ...and the proxy file has same extension as the fullres
            if os.path.isfile(proxy_file):
                return proxy_file
            # ...or the proxy file has different extension than fullres
            else:
                for e in bpy.path.extensions_movie:
                    proxy_file = base_path[:ref] + "_proxy" + e
                    if os.path.isfile(proxy_file):
                        return proxy_file

        #for s in bpy.context.sequences:
        scene = bpy.context.scene
        for s in scene.sequence_editor.sequences_all:
            if (s.type == "MOVIE"):
                f_path = s.filepath

                # if strip is already a proxy, do nothing
                if "_proxy." in f_path:
                    print("Strip '" + f_path + "' is already a proxy.")
                    pass

                # or strip is a fullres that has correspondent proxy files...
                elif "_PRORES." in f_path:
                    s.filepath = checkProxyFile(f_path, -7)
                    print("Proxy file for '" + f_path + "' is OK.")

                elif "_MJPEG." in f_path:
                    s.filepath = checkProxyFile(f_path, -6)
                    print("Proxy file for '" + f_path + "' is OK.")

                elif "_h264." in f_path:
                    s.filepath = checkProxyFile(f_path, -5)
                    print("Proxy file for '" + f_path + "' is OK.")

                # for fullres files without _PRORES or _MJPEG or _h264 in name
                else:
                    base_path, ext = os.path.splitext(f_path)
                    ext_len = len(ext) + 1
                    # search in folder for any file with the same name appended
                    # by "_proxy" and with recognizeable movie extension
                    if glob.glob(base_path + "_proxy.*") and \
                            ext.lower() in bpy.path.extensions_movie:
                        s.filepath = glob.glob(base_path + "_proxy.*")[0]
                        print("Proxy file for '" + f_path + "' is OK.")
                    else:
                        print("No proxy file found for '" + f_path + "'.")
                        pass

            elif (s.type == "SOUND"):
                # From Blender 2.77 onwards, sound files filepath have to
                # be referred to as s.sound.filepath instead of s.filepath
                f_path = s.sound.filepath

                # if strip is already a proxy, do nothing
                if "_proxy." in f_path:
                    print("Strip '" + f_path + "' is already a proxy.")
                    pass

                # or strip is a fullres that has correspondent proxy files...
                elif "_PRORES." in f_path:
                    s.sound.filepath = checkProxyFile(f_path, -7)
                    print("Proxy file for '" + f_path + "' is OK.")

                elif "_MJPEG." in f_path:
                    s.sound.filepath = checkProxyFile(f_path, -6)
                    print("Proxy file for '" + f_path + "' is OK.")

                elif "_h264." in f_path:
                    s.sound.filepath = checkProxyFile(f_path, -5)
                    print("Proxy file for '" + f_path + "' is OK.")

                # for fullres files without _PRORES or _MJPEG or _h264 in name
                else:
                    base_path, ext = os.path.splitext(f_path)
                    ext_len = len(ext) + 1
                    # search in folder for any file with the same name appended
                    # by "_proxy" and with recognizeable movie extension
                    if glob.glob(base_path + "_proxy.*") and \
                            ext.lower() in bpy.path.extensions_movie:
                        s.sound.filepath = glob.glob(base_path + "_proxy.*")[0]
                        print("Proxy file for '" + f_path + "' is OK.")
                    else:
                        print("No proxy file found for '" + f_path + "'.")
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

        #for s in bpy.context.sequences:
        scene = bpy.context.scene
        for s in scene.sequence_editor.sequences_all:
            if (s.type == "MOVIE"):
                f_path = s.filepath

                # if strip is a proxy and has correspondent fullres files
                if "_proxy." in f_path:
                    print("Checking full-res file for '" + f_path + "'...")
                    base_path, ext = os.path.splitext(f_path)
                    f_name = base_path[:-6]

                    if glob.glob(f_name + "_PRORES.*"):
                        s.filepath = glob.glob(f_name + "_PRORES.*")[0]
                        print("Full-res file found.")
                    elif glob.glob(f_name + "_MJPEG.*"):
                        s.filepath = glob.glob(f_name + "_MJPEG.*")[0]
                        print("Full-res file found.")
                    elif glob.glob(f_name + "_h264.*"):
                        s.filepath = glob.glob(f_name + "_h264.*")[0]
                        print("Full-res file found.")
                    elif glob.glob(f_name + ".*"):
                        # if strip's filepath doesn't end with '_MJPEG.mov',
                        # '_PRORES.mov' or '_h264.mov', script will look for
                        # files in folder with the same name as the strip in
                        # the timeline, independent of file's extension
                        # (ie: .mov, .avi etc).
                        s.filepath = glob.glob(f_name + ".*")[0]
                        print("Full-res file found.")
                    else:
                        print("No full-res file found for " + f_name + ".")
                        pass
                else:
                    print("Strip " + f_path + " is not a proxy.")
                    pass

            elif (s.type == "SOUND"):
                # From Blender 2.77 onwards, sound files filepath have to
                # be referred to as s.sound.filepath instead of s.filepath
                f_path = s.sound.filepath

                if "_proxy." in f_path:
                    print("Checking full-res file for '" + f_path + "'...")
                    base_path, ext = os.path.splitext(f_path)
                    f_name = base_path[:-6]

                    if glob.glob(f_name + "_PRORES.*"):
                        s.sound.filepath = glob.glob(f_name + "_PRORES.*")[0]
                        print("Full-res file found.")
                    elif glob.glob(f_name + "_MJPEG.*"):
                        s.sound.filepath = glob.glob(f_name + "_MJPEG.*")[0]
                    elif glob.glob(f_name + "_h264.*"):
                        s.sound.filepath = glob.glob(f_name + "_h264.*")[0]
                        print("Full-res file found.")
                    elif glob.glob(f_name + ".*"):
                        s.sound.filepath = glob.glob(f_name + ".*")[0]
                        print("Full-res file found.")
                    else:
                        print("No full-res file found for " + f_name + ".")
                        pass
                else:
                    print("Strip " + f_path + " is not a proxy.")
                    pass

        # Make all paths relative; behaviour tends to be standard in Blender
        bpy.ops.file.make_paths_relative()

        return {'FINISHED'}


######## ----------------------------------------------------------------------
######## FFMPEG TRANSCODING
######## ----------------------------------------------------------------------

class VideoSource(object):
    """Uses video source to run FFMPEG and create proxies or full-res copies"""
    def __init__(self, ffCommand, filepath, v_source, v_res, v_res_w, v_res_h, v_format,
                 fps, deinter, ar, ac):
        self.ffCommand = ffCommand
        self.input = v_source
        self.filepath = filepath
        self.fps = fps
        self.arate = str(ar)

        self.v_size = "%sx%s" % (v_res_w, v_res_h)

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
                self.format = "-probesize 5000000 -c:v prores \
                               -profile:v 0 -qscale:v 13 -vendor ap10 \
                               -pix_fmt yuv422p10le -acodec pcm_s16be"
            elif v_format == "is_mjpeg":
                self.format = "-probesize 5000000 -c:v mjpeg \
                               -qscale:v 5 -pix_fmt yuvj422p -acodec pcm_s16be"
            else: # v_format == "is_h264":
                self.format = "-probesize 5000000 -c:v libx264 -pix_fmt yuv420p \
                               -preset ultrafast -tune fastdecode -c:a copy"
                # -preset ultrafast was having problems
                # dealing with ProRes422 from Final Cut
        else: # v_res == "fullres"
            if v_format == "is_prores":
                self.v_output = self.input[:-4] + "_PRORES.mov"
                self.format = "-probesize 5000000 -c:v prores -profile:v 3 \
                               -qscale:v 5 -vendor ap10 -pix_fmt yuv422p10le \
                               -pix_fmt yuvj422p -acodec pcm_s16be"
            elif v_format == "is_mjpeg":
                self.v_output = self.input[:-4] + "_MJPEG.mov"
                self.format = "-probesize 5000000 -c:v mjpeg -qscale:v 1 \
                               -acodec pcm_s16be"
            else: # v_format == "is_h264":
                self.v_output = self.input[:-4] + "_h264.mkv"
                self.format = "-probesize 5000000 -c:v libx264 \
                               -pix_fmt yuv420p -c:a copy"
                # -preset ultrafast was having problems
                # dealing with ProRes422 from Final Cut


    def runFF(self):
        # Due to spaces, the command entries (ffCommand, input and output) have
        # to be read as strings by the call command, thus the escapings below
        callFFMPEG = "\"%s\" -hwaccel auto -i \"%s\" -y %s -r %s -s %s %s -ar %s %s \"%s\"" \
                     % (self.ffCommand, self.input, self.format, self.fps, self.v_size,
                        self.deinter, self.arate, self.achannels, self.v_output)

        print(callFFMPEG)
        call(callFFMPEG, shell=True)

        return {'FINISHED'}


######## ----------------------------------------------------------------------
######## VELVET REVOLVER MAIN CLASS
######## ----------------------------------------------------------------------

class VelvetRevolver(bpy.types.Operator, ExportHelper):
    """Mass create proxies and/or intra-frame copies from original files"""
    bl_idname = "export.revolver"
    bl_label = "Export to Revolver"
    filename_ext = ".revolver"

    transcode_items = (
        ('is_mjpeg', 'MJPEG', ''),
        ('is_prores', 'ProRes422', ''),
        ('is_h264', 'h264 (experimental)', '')
    )

    proxies: BoolProperty(
        name="Create Proxies",
        description="Create proxies with same FPS as current scene",
        default=True,
    )
    prop_proxy_w: IntProperty(
        name="Proxy Width",
        description="Proxy videos will have this width",
        default=640
    )
    prop_proxy_h: IntProperty(
        name="Height",
        description="Proxy videos will have this height",
        default=360
    )
    copies: BoolProperty(
        name="Create Full-res Copies",
        description="Create full-res copies with same FPS as current scene (slow)",
        default=False,
    )
    prop_fullres_w: IntProperty(
        name="Full-res Width",
        description="Full-res videos will have this width",
        default=1920
    )
    prop_fullres_h: IntProperty(
        name="Height",
        description="Full-res videos will have this height",
        default=1080
    )
    v_format: EnumProperty(
        name="Format",
        default="is_mjpeg",
        description="Intra-frame format for the creation of proxies and/or copies",
        items=transcode_items
    )
    prop_ar: IntProperty(
        name="Audio Sample Rate",
        description="Transcoded videos will have this audio rate",
        default=48000
    )
    prop_deint: BoolProperty(
        name="Deinterlace videos",
        description="Uses FFMPEG Yadif filter to deinterlace all videos",
        default=False,
    )
    prop_ac: BoolProperty(
        name="Force Mono",
        description="Forces FFMPEG to transcode videos to mono - easier panning in Blender, but usually not recommended",
        default=False,
    )

    def draw(self, context):

        #fps = context.scene.render.fps
        render = context.scene.render
        fps = round(render.fps / render.fps_base, 2)

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column(align=True)
        col.label(text="Navigate to your videos folder, choose")
        col.label(text="options below and hit 'Export to Revolver'")

        box = layout.box()
        box.use_property_split = False
        box.prop(self, 'proxies')
        box.use_property_split = True
        col = box.column(align=True)
        col.active = self.proxies
        col.prop(self, 'prop_proxy_w')
        col.prop(self, 'prop_proxy_h')

        box = layout.box()
        box.use_property_split = False
        box.prop(self, 'copies')
        box.use_property_split = True
        col = box.column(align=True)
        col.active = self.copies
        col.prop(self, 'prop_fullres_w')
        col.prop(self, 'prop_fullres_h')
        col.prop(self, 'v_format')

        box = layout.box()
        box.prop(self, 'prop_ar')
        box.prop(self, 'prop_deint')
        box.prop(self, 'prop_ac')

        col = layout.column(align=True)
        col.label(text="Resulting videos will have %.2f FPS." % fps)
        col.label(text="(FPS inherited from project's Properties)")


    @classmethod
    def poll(cls, context):
        if bpy.data.scenes:
            return bpy.data.scenes is not None

    def execute(self, context):
        ffCommand = bpy.context.preferences.addons['velvet_revolver'].preferences.ffCommand

        videosFolderPath, blenderFile = os.path.split(self.filepath)
        videosFolderPath += os.sep

        #fps = context.scene.render.fps
        render = context.scene.render
        fps = round(render.fps / render.fps_base, 2)

        sources = []

        for i in glob.glob(videosFolderPath + "*.*"):
            if i[-4:].lower() in bpy.path.extensions_movie:
                # The line below does not allow for the creation of proxies from
                # a _PRORES or _MJPEG file. TO-DO: creation of sources = [] has
                # to be inside self.proxies and self.copies. Then, the script
                # should check for a "original" file (ie. without _prores) ->
                # if it finds it, pass; else, execute ffmpeg command.
                # Also: 'sources' should be sorted by filesize, so that
                # smaller files are transcoded first (create this as an option:
                # sort by filesize, sort by name).
                if "_proxy." not in i and "_MJPEG." not in i \
                   and "_PRORES." not in i and "_h264" not in i:
                    sources.append(i)

        # If nothing is selected to do, abort. Else, continue
        if not self.proxies and not self.copies:
            print("No action selected for Velvet Revolver. Aborting.")

        else:
            # Create a percentage to base a (mouse) progress counter
            wm = bpy.context.window_manager

            if self.proxies and self.copies:
                # If Revolver has to create both proxies and copies,
                # there are 2x as many levels to be considered
                inc_level = int(100 / (2 * len(sources)))
            else:
                inc_level = int(100 / len(sources))

            wm.progress_begin(1, 100)
            percentage_level = 1


            if self.proxies:
                for source in sources:
                    v_res = "proxy"
                    vs = VideoSource(ffCommand, videosFolderPath, source, v_res,
                                     self.prop_proxy_w, self.prop_proxy_h,
                                     self.v_format, fps, self.prop_deint,
                                     self.prop_ar, self.prop_ac)

                    # Update window_manager progress counter
                    wm.progress_update(percentage_level)
                    percentage_level += inc_level

                    vs.runFF()

            if self.copies:
                for source in sources:
                    v_res = "fullres"
                    vs = VideoSource(ffCommand, videosFolderPath, source, v_res,
                                     self.prop_fullres_w, self.prop_fullres_h,
                                     self.v_format, fps, self.prop_deint,
                                     self.prop_ar, self.prop_ac)

                    # Update window_manager progress counter
                    wm.progress_update(percentage_level)
                    percentage_level += inc_level

                    vs.runFF()


            # Finish report on progress counter
            wm.progress_end()

            self.report({'INFO'}, "Velvet Revolver Encoding Finished")

        return {'FINISHED'}


class Velvet_Revolver_Transcoder(bpy.types.AddonPreferences):
    """Velver Revolver preferences"""
    bl_idname = __name__.split(".")[0]
    bl_option = {'REGISTER'}

    if which('ffmpeg') is not None:
        ffmpeg = which('ffmpeg')
    else:
        ffmpeg = "/usr/bin/ffmpeg"

    ffCommand: StringProperty(
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


classes = (
    Proxy_Editing_ToProxy,
    Proxy_Editing_ToFullRes,
#    VideoSource,
    VelvetRevolver,
    Velvet_Revolver_Transcoder,
)

# store keymaps here to access after registration
revolver_keymaps = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # Add menu entry
    bpy.types.TOPBAR_MT_file_external_data.append(menuEntry)

    # Handle the keymap for Proxy_Editing
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name = "Sequencer",space_type='SEQUENCE_EDITOR', region_type='WINDOW')

    kmi = km.keymap_items.new(Proxy_Editing_ToFullRes.bl_idname, 'P', 'PRESS', shift=True, ctrl=True)
    revolver_keymaps.append((km, kmi))

    kmi = km.keymap_items.new(Proxy_Editing_ToProxy.bl_idname, 'P', 'PRESS', shift=True, ctrl=True, alt=True)
    revolver_keymaps.append((km, kmi))


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    # Remove menu entry
    bpy.types.TOPBAR_MT_file_external_data.remove(menuEntry)

    # Unregister Proxy_Editing shortcut
    for km, kmi in revolver_keymaps:
        km.keymap_items.remove(kmi)
    revolver_keymaps.clear()


if __name__ == "__main__":
    register()
