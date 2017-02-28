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
    "name": "velvet_revolution ::",
    "description": "Pack your stuff to go",
    "author": "szaszak - http://blendervelvets.org",
    "version": (1, 0, 20170227),
    "blender": (2, 78, 0),
    "warning": "Bang! Bang! That awful sound.",
    "category": ":",
    "location": "File > External Data > Velvet Revolution",
    "support": "COMMUNITY"}


import bpy
import os
from shutil import copyfile, which
from subprocess import call
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, IntProperty


def check_scenes(scene, sequences):
    """Checks scenes for video/audio files being used
    that have the same filename (excluding extension)"""
    # Create lists with sounds and movies filenames to check if they repeat
    sounds, movies = [], []
    for s in sequences:
        if s.type == 'SOUND':
            basename = os.path.basename(s.sound.filepath)
            f_name, f_ext = os.path.splitext(basename)
            if f_ext.lower() in bpy.path.extensions_audio and f_name not in sounds:
                sounds.append(f_name)
        elif s.type == 'MOVIE':
            basename = os.path.basename(s.filepath)
            f_name, f_ext = os.path.splitext(basename)
            if f_ext.lower() in bpy.path.extensions_movie and f_name not in movies:
                movies.append(f_name)

    # Check for repeated instances of sounds and movies filenames
    # If there aren't, return True for cheking. Else, return False, print
    # files with similar filenames and select them in the VSE Timeline
    # for easier user interaction.
    repeated_names = [m for m in movies if m in sounds]
    if not repeated_names:
        print("\nScene named '%s' is ok to go." % (scene))
        return True
    else:
        print("\n\
            The following video and audio strips have the same file name (even if with\n\
            different extensions). To continue, change either the movie or the sound\n\
            original name, update their paths and run 'Velvet - Pack Your Stuff' again.\n\
            The strips have been selected for you in your timeline for identification.\n\
            \nStrips in scene named '%s':\nType - File name - Path to file:\n" % (scene))

        for rn in repeated_names:
            for i in sequences:
                if i.type == 'SOUND' and rn in i.sound.filepath:
                    i.select = True
                    print("(%s) %s - %s" % (i.type, i.name, i.sound.filepath))
                if i.type == 'MOVIE' and rn in i.filepath:
                    i.select = True
                    print("(%s) %s - %s" % (i.type, i.name, i.filepath))

        return False


def sanity_check(scenes):
    sanity = True
    for scene in scenes:
        sequences = bpy.data.scenes[scene.name].sequence_editor.sequences_all
        sanity_check = check_scenes(scene.name, sequences)
        # If sanity checks false in one of the Scenes, return False
        if sanity_check is False:
            sanity = False

    return sanity


def copy_keyframes(current_strip, scene1, scene2):
    # First, select strip
    cs = current_strip
    cs.select = True

    # Go to sequence's copy and select the same strip
    bpy.context.screen.scene = scene2
    for i in bpy.context.sequences:
        if i.name == cs.name:
            i.select = True

    # Copy that strip's keyframes
    area = bpy.context.area
    old_type = area.type
    area.type = 'GRAPH_EDITOR'

    #bpy.data.scenes[-1].frame_current = 0
    bpy.ops.graph.select_leftright(mode='RIGHT', extend=False)
    bpy.ops.graph.copy()

    area.type = old_type

    # Change back to previous scene and replace those keyframes
    bpy.context.screen.scene = bpy.data.scenes[scene1.name]

    area = bpy.context.area
    old_type = area.type
    area.type = 'GRAPH_EDITOR'
    # bpy.data.scenes['Scene'].frame_current = 0
    bpy.ops.graph.select_leftright(mode='RIGHT', extend=False)
    bpy.ops.graph.paste(offset='NONE' , merge='OVER_ALL')

    area.type = old_type


def pack_your_stuff(scenes, export_path, sec_margin):
    render = bpy.context.scene.render
    fps = render.fps / render.fps_base
    chosen_margin = sec_margin * round(fps)

    audio_ext = bpy.path.extensions_audio
    movie_ext = bpy.path.extensions_movie

    preferences = bpy.context.user_preferences
    ffCommand = preferences.addons['velvet_revolution'].preferences.ffCommand

    # Create new folders to organize content
    audio_f = export_path + "AUDIO/"
    movie_f = export_path + "VIDEO/"
    image_f = export_path + "IMAGES/"
    for bkp_f in (audio_f, movie_f, image_f):
        if not os.path.exists(bkp_f):
            os.mkdir(bkp_f)

    audio_pool = []
    video_counter = 0
    for scene in scenes:
        # We're forcing the change of scene here so that files are not skipped
        bpy.context.screen.scene = bpy.data.scenes[scene.name]

        # Position cursor at the frame 0 and create a full copy of scene
        # This copy will be necessary for copying the keyframes
        bpy.data.scenes[scene.name].frame_current = 0
        bpy.ops.scene.new(type='FULL_COPY')
        bpy.context.screen.scene = bpy.data.scenes[scene.name]

        for seq in bpy.context.sequences:

            if seq.type == 'SOUND': 
                # We have to create an 'audio_pool' to know which audios have already
                # been processed by the script. This is because seq.sound.filepath is
                # updated while the loop is still going through the sound files.
                # In Blender, once you update the seq.sound.filepath for one audio, it'll
                # update for all instances of that audio in the timeline. This will
                # throw an error saying the file to be copied is the same as its copy.
                # Now, the trick is - if the audio comes from a video, Blender will
                # only update that one instance of seq.sound.filepath so we have to
                # separate this second checking conditional from the first one.
                s_path = seq.sound.filepath
                basename = os.path.basename(s_path)
                new_name = os.path.splitext(basename)[0]

                # If strip refers to an audio file, copy it to new location
                if s_path.lower().endswith(tuple(audio_ext)) and new_name not in audio_pool:
                    new_path = audio_f + basename
                    copyfile(s_path, new_path)
                    audio_pool.append(new_name)
                    # Update change in timeline
                    seq.sound.filepath = new_path
                # If strip belongs to a movie, extract audio as .wav to new location
                elif s_path.lower().endswith(tuple(movie_ext)):
                    new_path = audio_f + new_name + ".wav"

                    # If it's the first ocurrence of this video, extract wav
                    # else, just update seq.sound.filepath
                    if new_name not in audio_pool:
                        # Due to spaces, the command entries (ffCommand, input and output) 
                        # have to be read as strings by call command, thus the escapings
                        callFFMPEG = "\"%s\" -i \"%s\" -y \"%s\"" % \
                                     (ffCommand, s_path, new_path)

                        print(callFFMPEG)
                        call(callFFMPEG, shell=True)
                        audio_pool.append(new_name)

                    # Update keyframes for strip
                    copy_keyframes(seq, scene, bpy.data.scenes[-1])
                    
                    # Update change in timeline
                    seq.sound.filepath = new_path

            elif seq.type == 'IMAGE':
                # Check if original images' directory exists; else create it
                s_path = seq.directory
                s_folder = os.path.dirname(s_path).split(os.sep)[-1]
                new_f = image_f + s_folder
                if not os.path.exists(new_f):
                    os.mkdir(new_f)

                # If images do not exist in new folder yet, copy them
                # Images in image strips can be acessed with a loop on
                # seq.elements; they are stored at seq.directory
                new_f += os.sep
                for e in seq.elements:
                    new_image = new_f + e.filename
                    if not os.path.isfile(new_image):
                        copyfile(seq.directory+e.filename, new_image)

                # Update change in timeline
                seq.directory = new_f

            elif seq.type == 'MOVIE':
                video_counter += 1
                # Sum possible offsets (animation_offset and frame_offset)
                # to pass as argument for ffmpeg. Values are in frames
                start_offset = seq.animation_offset_start + seq.frame_offset_start
                end_offset = seq.animation_offset_end + seq.frame_offset_end

                # Check start offsets first
                if start_offset > chosen_margin:
                    seek = start_offset - chosen_margin
                    duration = seq.frame_final_duration + chosen_margin
                    new_offset_start = chosen_margin
                else: # start_offset <= chosen_margin
                    seek = start_offset
                    duration = seq.frame_final_duration + start_offset
                    new_offset_start = start_offset

                # Check end offsets; end offsets do not affect ffmpeg seeking
                if end_offset > chosen_margin:
                    duration += chosen_margin
                    new_offset_end = chosen_margin
                else: # end_offset <= chosen_margin
                    duration += end_offset
                    new_offset_end = end_offset

                # Convert frames to seconds/milliseconds.
                seek_value = seek/fps
                duration = duration/fps

                # ffmpeg MUST transcode original file to preserve seeking accuray
                new_name = "video_%d" % (video_counter)
                new_name += ".mkv"
                new_path = movie_f + new_name
                ff_parameters = "-t %s -probesize 5000000 -c:v mjpeg -qscale:v 1 -an"\
                                % (str(duration))
                callFFMPEG = "\"%s\" -ss %s -i \"%s\" -y %s \"%s\"" % (ffCommand, \
                              str(seek_value), seq.filepath, ff_parameters, new_path)

                print(callFFMPEG)
                call(callFFMPEG, shell=True)

                # Prepare infos for replacing strip
                new_position = seq.frame_final_start - new_offset_start
                original_channel = seq.channel
 
                # Update keyframes for strip
                copy_keyframes(seq, scene, bpy.data.scenes[-1])

                # Replace strip's path to point to the new one. We temporarily
                # position it at channel 35 so that when we clear its offsets, it
                # won't bump into another strip and be replaced at an odd channel
                seq.channel = 35
                # The name of the strips cannot be changed if we want the
                # keyframes to be pasted back to them accordingly. Maybe
                # a bug in the API?
                #seq.name = new_name
                seq.filepath = new_path
                # Clear all possible offsets and reposition strip
                seq.animation_offset_start = 0
                seq.animation_offset_end = 0
                seq.frame_offset_start = new_offset_start
                seq.frame_offset_end = new_offset_end
                # Reposition strip
                seq.frame_start = new_position
                seq.channel = original_channel

        # Remove previously created backup scene for keyframe copying
        bpy.context.screen.scene = bpy.data.scenes[-1]
        bpy.ops.scene.delete()

        print("Strips for %s packed." % (scene.name))

    print("\nFinished.")


class VelvetRevolution_PackYourStuff(bpy.types.Operator, ExportHelper):
    """Packs shortened versions of used files on all scenes to backup folder"""
    bl_idname = "export.revolution_pack"
    bl_label = "Revolution - Pack your stuff"
    filename_ext = ".blend"

    prop_sec = IntProperty(
        name="Seconds",
        description="Seconds to leave as margin in movie strips in backup",
        default=2
    )

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label('Margin for backup:')
        box.prop(self, 'prop_sec')

    @classmethod
    def poll(cls, context):
        if bpy.data.scenes:
            return bpy.data.scenes is not None

    def execute(self, context):
        # Save a new bkp .blend file in folder
        export_path, blend_file = os.path.split(self.filepath)
        export_path += os.sep
        bpy.ops.wm.save_mainfile(filepath = export_path + "BKP_" + blend_file)
        bpy.ops.file.make_paths_absolute()

        # Main function
        sec_margin = self.prop_sec
        scenes = bpy.data.scenes
        if sanity_check(scenes):
            pack_your_stuff(scenes, export_path, sec_margin)

        # Save all changes in .blend file and finish
        bpy.ops.file.make_paths_relative()
        bpy.ops.wm.save_mainfile()

        # Print simple output to check for validity of new filepaths
        for scene in scenes:
            bpy.context.screen.scene = bpy.data.scenes[scene.name]
            for sq in bpy.context.sequences:
                if sq.type == 'IMAGE':
                    print(sq.directory)
                elif sq.type == 'SOUND':
                    print(sq.sound.filepath)
                elif sq.type == 'MOVIE':
                    print(sq.filepath)
                else:
                    pass

        return {'FINISHED'}


class Velvet_Revolution_Transcoder(bpy.types.AddonPreferences):
    """Velver Revolution preferences"""
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
    self.layout.operator(VelvetRevolution_PackYourStuff.bl_idname, text="Velvet Revolution")


def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_external_data.append(menuEntry)


def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_external_data.remove(menuEntry)


if __name__ == "__main__":
    register()
