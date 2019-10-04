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


import bpy

bl_info = {
    "name": "velvet_goldmine ::",
    "description": "Glamorous new shortcuts for video editing in Blender VSE",
    "author": "szaszak - http://blendervelvets.org",
    "version": (2, 0, 20190909),
    "blender": (2, 80, 0),
    "warning": "TO BE USED WITH LOTS OF GLITTER",
    "category": ":",
    "location": "Sequencer",
    "support": "COMMUNITY"}


class Audio_Strips_Display_Waveform(bpy.types.Operator):
    """Displays the audio waveform in selected strips"""
    bl_idname = "sequencer.strips_display_waveform"
    bl_label = "Display Waveform - Selected Strips"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: W

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):

        for strip in bpy.context.selected_sequences:
            if (strip.type == "SOUND"):
                if (strip.show_waveform is False):
                    strip.show_waveform = True

        return {'FINISHED'}


class Audio_Strips_Hide_Waveform(bpy.types.Operator):
    """Hides the audio waveform in selected strips"""
    bl_idname = "sequencer.strips_hide_waveform"
    bl_label = "Hide Waveform - Selected Strips"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Alt + W

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):

        for strip in bpy.context.selected_sequences:
            if (strip.type == "SOUND"):
                if (strip.show_waveform is True):
                    strip.show_waveform = False

        return {'FINISHED'}


class Delete_Direct(bpy.types.Operator):
    """Deletes without prompting for confirmation"""
    bl_idname = "sequencer.delete_direct"
    bl_label = "Delete Direct"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Delete

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        bpy.ops.sequencer.delete()
        return {'FINISHED'}


class Delete_Direct_Gaps(bpy.types.Operator):
    """Deletes removing gaps without prompting for confirmation"""
    bl_idname = "sequencer.delete_direct_gaps"
    bl_label = "Delete Direct - Remove Gaps"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Ctrl + Delete

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        scene = bpy.context.scene
        orig_pos = scene.frame_current
        updated_pos = []

        for i in bpy.context.selected_sequences:
            updated_pos.append(i.frame_offset_start + i.frame_start)

        new_pos = sorted(set(updated_pos))[0]

        # Places i-beam at beginning of selected strips, deletes them,
        # then remove gaps and return i-beam to original position
        bpy.ops.sequencer.delete()
        scene.frame_set(new_pos)
        bpy.ops.sequencer.gap_remove()
        scene.frame_set(orig_pos)

        return {'FINISHED'}


class Fade_In_Strip_Start(bpy.types.Operator):
    """Creates a one second fade in (for audio and/or video) at strip start"""
    bl_idname = "sequencer.fade_in_strip_start"
    bl_label = "Fade In - Strip Start"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Ctrl + F

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        fps = bpy.context.scene.render.fps
        #render = bpy.context.scene.render
        #fps = render.fps / render.fps_base

        for strip in bpy.context.selected_sequences:
            keyframePosition1 = strip.frame_offset_start + strip.frame_start
            keyframePosition2 = keyframePosition1 + fps
            if (strip.type == "SOUND"):
                originalVolume = strip.volume
                strip.volume = 0
                strip.keyframe_insert('volume', -1, keyframePosition1)
                strip.volume = originalVolume
                strip.keyframe_insert('volume', -1, keyframePosition2)

            else:
                originalAlpha = strip.blend_alpha
                strip.blend_alpha = 0
                strip.keyframe_insert('blend_alpha', -1, keyframePosition1)
                strip.blend_alpha = originalAlpha
                strip.keyframe_insert('blend_alpha', -1, keyframePosition2)

        return {'FINISHED'}


class Fade_Out_Strip_End(bpy.types.Operator):
    """Creates a one second fade out (for audio and/or video) at strip end"""
    bl_idname = "sequencer.fade_out_strip_end"
    bl_label = "Fade Out - Strip End"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Alt + F

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        fps = bpy.context.scene.render.fps
        #render = bpy.context.scene.render
        #fps = render.fps / render.fps_base

        for strip in bpy.context.selected_sequences:
            keyframePosition1 = strip.frame_final_end
            keyframePosition2 = keyframePosition1 - fps
            if (strip.type == "SOUND"):
                originalVolume = strip.volume
                strip.volume = 0
                strip.keyframe_insert('volume', -1, keyframePosition1)
                strip.volume = originalVolume
                strip.keyframe_insert('volume', -1, keyframePosition2)

            else:
                originalAlpha = strip.blend_alpha
                strip.blend_alpha = 0
                strip.keyframe_insert('blend_alpha', -1, keyframePosition1)
                strip.blend_alpha = originalAlpha
                strip.keyframe_insert('blend_alpha', -1, keyframePosition2)

        return {'FINISHED'}


class Markers_Delete_Closest(bpy.types.Operator):
    """Deletes the closest marker to the cursor"""
    bl_idname = "sequencer.marker_delete_closest"
    bl_label = "Markers - Delete Closest"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Alt + M

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        scene = bpy.context.scene
        currentFrame = scene.frame_current
        marker = scene.timeline_markers
        markers = []

        def nameMarker(n):
            for m in marker:
                if m.frame == markers[n]:
                    markerName = m.name
            return markerName

        if (len(marker) != 0):
            for i in scene.timeline_markers:
                markers.append(i.frame)

            markers.append(currentFrame)
            markers.sort()

            idx = markers.index(currentFrame)

            if (idx == 0):
                # cursor before all markers, remove first
                markerName = nameMarker(1)
            elif (idx == (len(markers)-1)):
                # cursor after all markers, remove last
                markerName = nameMarker(-2)
            else:
                # cursor on a marker, remove current or
                # cursor between markers, remove closest
                sum1 = markers[idx] - markers[idx-1]
                sum2 = markers[idx+1] - markers[idx]
                if (sum1 < sum2):
                    markerName = nameMarker(idx-1)
                else:
                    markerName = nameMarker(idx+1)

            marker.remove(marker[markerName])

            return {'FINISHED'}

        else:
            print("There are no markers in the timeline!")

            return {'CANCELLED'}


class Markers_Goto_Left(bpy.types.Operator):
    """Moves cursor to left marker position"""
    bl_idname = "sequencer.marker_goto_left"
    bl_label = "Markers - Go to Left Marker"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Ctrl + LeftArrow

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        scene = bpy.context.scene
        currentFrame = scene.frame_current
        marker = scene.timeline_markers

        if (len(marker) != 0):
            markers = []

            for i in scene.timeline_markers:
                markers.append(i.frame)

            markers.append(currentFrame)
            markers.sort()

            idx = markers.index(currentFrame)

            if (idx != 0):
                # if cursor is not before markers
                scene.frame_current = markers[idx-1]
                return {'FINISHED'}
            else:
                scene.frame_current = scene.frame_preview_start
                return {'FINISHED'}
        else:
            scene.frame_current = scene.frame_preview_start
            return {'FINISHED'}


class Markers_Goto_Right(bpy.types.Operator):
    """Moves cursor to right marker position"""
    bl_idname = "sequencer.marker_goto_right"
    bl_label = "Markers - Go to Right Marker"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Ctrl + RightArrow

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        scene = bpy.context.scene
        currentFrame = scene.frame_current
        marker = scene.timeline_markers

        if (len(marker) != 0):
            markers = []

            for i in scene.timeline_markers:
                markers.append(i.frame)

            markers.append(currentFrame)
            markers = sorted(set(markers))

            idx = markers.index(currentFrame)

            if (idx != len(markers)-1):
                # if cursor is not after markers
                scene.frame_current = markers[idx+1]
                return {'FINISHED'}
            else:
                scene.frame_current = scene.frame_end
                return {'FINISHED'}
        else:
            scene.frame_current = scene.frame_end
            return {'FINISHED'}


class Scene_Toggle(bpy.types.Operator):
    """Toggles between existing Scenes"""
    bl_idname = "screen.scene_toggle"
    bl_label = "Scene toggle"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcuts: Shift + TAB

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        scene = bpy.context.scene

        index = 0
        for i in bpy.data.scenes:
            if (i.name == scene.name):
                break
            else:
                index += 1

        if (index == (len(bpy.data.scenes)-1)):
            bpy.context.window.scene = bpy.data.scenes[0]
        else:
            bpy.context.window.scene = bpy.data.scenes[index+1]

        return {'FINISHED'}


class Set_End_Frame_In_Last(bpy.types.Operator):
    """Sets Timeline end to last video frame"""
    bl_idname = "anim.end_frame_last_set"
    bl_label = "Set End Frame in Last"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Alt + End

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        scene = bpy.context.scene

        lastFrame = 0
        for sequence in scene.sequence_editor.sequences:
                if (sequence.frame_final_end > lastFrame):
                    lastFrame = sequence.frame_final_end - 1

        scene.frame_end = lastFrame
        scene.frame_preview_end = lastFrame

        return {'FINISHED'}


class Set_Start_Frame_In_One(bpy.types.Operator):
    """Sets Timeline start to frame one"""
    bl_idname = "anim.start_frame_one_set"
    bl_label = "Set Start Frame in 1"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Alt + Home

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        scene = bpy.context.scene
        scene.frame_start = 1
        scene.frame_preview_start = 1

        return {'FINISHED'}


class Slight_Desync_Adjust(bpy.types.Operator):
    """Adjust selected audio strips that are 
    1 frame bigger than its movies"""
    bl_idname = "sequencer.slight_desync_adjust"
    bl_label = "Slight Desync Adjust"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Ctrl + Alt + Shift + D

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        sel_seq = bpy.context.selected_sequences

        sounds = [s for s in sel_seq if s.type == 'SOUND']
        movies = [m for m in sel_seq if m.type == 'MOVIE']

        for sound in sounds:
            ss = sound.frame_offset_start + sound.frame_start
            se = sound.frame_final_end
            sp = sound.sound.filepath

            for movie in movies:
                ms = movie.frame_offset_start + movie.frame_start
                me = movie.frame_final_end
                mp = movie.filepath

                # Checks if both strips have the same filepath, start
                # at the same frame and have a difference of 1 between
                # their final frames - if so, remove 1 frame from audio
                if ss == ms and sp == mp and (se - me == 1):
                    sound.animation_offset_end += 1
                
                if ss == ms and sp == mp and (se - me == 2):
                    sound.animation_offset_end += 2

        return {'FINISHED'}


class Snap_Selected_To_Playhead(bpy.types.Operator):
    """Adjusts selected strips to playhead in the timeline"""
    bl_idname = "sequencer.snap_selected_to_playhead"
    bl_label = "Snap Selected to Playhead"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Ctrl + Alt + Shift + C

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        scene = bpy.context.scene

        selectedStrips = []
        for strip in bpy.context.selected_sequences:
            stripStart = strip.frame_start + strip.frame_offset_start
            selectedStrips.append([stripStart, strip.channel, strip.name])

        # reference is lowest (most to the left) stripStart of selected strips
        reference = sorted(selectedStrips)[0][0]

        gap = reference - scene.frame_current

        for strip in bpy.context.selected_sequences:
            try:
                strip.frame_start -= gap
            except AttributeError:
                pass

        # places strips back to their original channels or they'll be scattered
        for s in selectedStrips:
            scene.sequence_editor.sequences_all[s[2]].channel = s[1]

        return {'FINISHED'}


class Snap_Selected_To_TimelineStart(bpy.types.Operator):
    """Adjusts selected strips to the beginning of the timeline"""
    bl_idname = "sequencer.snap_selected_to_timelinestart"
    bl_label = "Snap Selected to Timeline Start"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Ctrl + Alt + Shift + S

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        scene = bpy.context.scene

        selectedStrips = []
        for strip in bpy.context.selected_sequences:
            stripStart = strip.frame_start + strip.frame_offset_start
            selectedStrips.append([stripStart, strip.channel, strip.name])

        # reference is lowest (most to the left) stripStart of selected strips
        reference = sorted(selectedStrips)[0][0]

        gap = reference - scene.frame_preview_start

        for strip in bpy.context.selected_sequences:
            try:
                strip.frame_start -= gap
            except AttributeError:
                pass

        # places strips back to their original channels or they'll be scattered
        for s in selectedStrips:
            scene.sequence_editor.sequences_all[s[2]].channel = s[1]

        return {'FINISHED'}


class Strips_Channel_Up(bpy.types.Operator):
    """Moves selected strips one channel up"""
    bl_idname = "sequencer.strip_up"
    bl_label = "Strips - Channel Up"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Alt + UpArrow

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        selectedStrips = bpy.context.selected_sequences

        myRange = range(len(selectedStrips)-1, -1, -1)
        for mr in myRange:
            selectedStrips[mr].channel += 1

        return {'FINISHED'}


class Strips_Channel_Down(bpy.types.Operator):
    """Moves selected strips one channel down"""
    bl_idname = "sequencer.strip_down"
    bl_label = "Strips - Channel Down"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Alt + DownArrow

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        # The code below used to work fine for Blender versions pre 2.73.
        # In that version, a bug was introduced that if you decreased a strip
        # channel value and that strip would overlap the one below, it would
        # be placed in some apparently random place in the new channel - not
        # where you wanted it or where it was supposed to be. Here is the
        # bug report: https://developer.blender.org/T46628 (it is *not* fixed)
        # This is horrible for video editing because it makes you easily lose 
        # track of your edits. The code below is here just because it was
        # simpler and nicer, so whenever the bug gets fixed, we'll shift
        # towards it again.

        # for strip in bpy.context.selected_sequences:
        #     if (strip.channel > 1):
        #         strip.channel -= 1

        for ss in bpy.context.selected_sequences:
            ss_start = ss.frame_start + ss.frame_offset_start
            ss_end = ss.frame_final_end

            # From all strips, check those in channel below selected strips
            for r in range(ss.channel - 1, 0, -1):
                strips_below = 0
                #print(r, strips_below)

                for s in bpy.context.sequences:
                    if s.channel == r:
                        s_start = s.frame_start + s.frame_offset_start
                        s_end = s.frame_final_end

                        # If a there is a strip (or part of any strip)
                        # below selected one, mark ocurrence
                        if (ss_start <= s_start < ss_end) or \
                           (ss_start < s_end <= ss_end) is not False:
                            strips_below += 1
            
                # Move strips down only if there is no strip below it
                if strips_below == 0 and ss.channel > 1:
                    ss.channel -= 1
                    break

        return {'FINISHED'}


class Strips_Concatenate_Selected(bpy.types.Operator):
    """Concatenates selected strips in channel (only works for 1 channel)"""
    bl_idname = "sequencer.strips_concatenate_selected"
    bl_label = "Strips - Concatenate Selected (Same channel)"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Shift + C

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):

        channels = []
        for strips in bpy.context.selected_sequences:
            channels.append(strips.channel)

        if (len(sorted(set(channels))) == 1):
            list = []
            for strip in bpy.context.selected_sequences:
                stripStart = strip.frame_start + strip.frame_offset_start
                list.append([stripStart, strip.frame_final_duration,
                             strip.name])

            list.sort()

            base = list[0][0] + list[0][1] # 1st strip start + duration
            for i in list[1:]:
                strip = bpy.context.scene.sequence_editor.sequences_all[i[2]]
                gap = (strip.frame_start + strip.frame_offset_start) - base
                strip.frame_start -= gap
                base += i[1]

        return {'FINISHED'}


class Strips_Deinterlace_Selected(bpy.types.Operator):
    """Deinterlace selected movie strips"""
    bl_idname = "sequencer.strips_deinterlace"
    bl_label = "Video Strips - Deinterlace Selected"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Ctrl + Shift + I

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):

        for strip in bpy.context.selected_sequences:
            if (strip.type == "MOVIE"):
                if (strip.use_deinterlace is False):
                    strip.use_deinterlace = True

        return {'FINISHED'}


class Strips_Remove_Deinterlace(bpy.types.Operator):
    """Remove deinterlace from selected movie strips"""
    bl_idname = "sequencer.strips_deinterlace_off"
    bl_label = "Video Strips - Remove Deinterlace"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Ctrl + Alt + I

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):

        for strip in bpy.context.selected_sequences:
            if (strip.type == "MOVIE"):
                if (strip.use_deinterlace is True):
                    strip.use_deinterlace = False

        return {'FINISHED'}


class Timeline_Loop_Selected(bpy.types.Operator):
    """Sets Timeline start and end to selected strips"""
    bl_idname = "sequencer.timeline_loop_selected"
    bl_label = "Timeline Loop Selected"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Ctrl + Alt + Shift + L

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        scene = bpy.context.scene
        selectedStrips = bpy.context.selected_sequences

        reference = 0
        for strip in selectedStrips:
            if strip.frame_final_end > reference:
                reference = strip.frame_final_end

        for strip in selectedStrips:
            stripStart = strip.frame_start + strip.frame_offset_start
            if (stripStart < reference):
                reference = stripStart

        scene.frame_start = reference
        scene.frame_preview_start = reference

        for strip in selectedStrips:
            if (strip.frame_final_end > reference):
                reference = strip.frame_final_end - 1

        scene.frame_end = reference
        scene.frame_preview_end = reference

        return {'FINISHED'}


class Timeline_Select_Inside_Preview(bpy.types.Operator):
    """Selects only the strips that start inside Timeline preview"""
    bl_idname = "sequencer.timeline_preview_select"
    bl_label = "Timeline - Select Inside Preview"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcut: Ctrl + Shift + A

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        scene = bpy.context.scene
        sequencer = bpy.ops.sequencer

        sequencer.select_all(action='DESELECT')

        for sequence in scene.sequence_editor.sequences:
            stripStart = sequence.frame_start + sequence.frame_offset_start
            if (stripStart >= scene.frame_preview_start) and \
               (stripStart <= scene.frame_preview_end):
                sequence.select = True

        return {'FINISHED'}


class Timeline_View_Selected_Context(bpy.types.Operator):
    """Alternative to View Selected (context view)"""
    bl_idname = "sequencer.view_selected_context"
    bl_label = "Timeline - View Selected Context"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcuts: End

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        '''sequencer = bpy.ops.sequencer
        sequencer.view_zoom_ratio(ratio=0.02)
        sequencer.view_selected()'''
        
        sequencer = bpy.ops.sequencer
        sequencer.view_all_preview()
        sequencer.view_selected()

        return {'FINISHED'}


class Timeline_ZoomIn_10s(bpy.types.Operator):
    """Zooms in aproximatelly 10s of Timeline"""
    bl_idname = "sequencer.timeline_zoom_in_10s"
    bl_label = "Timeline - Zoom In 10s"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcuts: Shift + Home

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        preferences = bpy.context.preferences
        mouse = False

        if (preferences.inputs.use_zoom_to_mouse is True):
            mouse = True
            preferences.inputs.use_zoom_to_mouse = False

        bpy.ops.view2d.zoom(deltax=150.0, deltay=0.0)

        if (mouse is True):
            preferences.inputs.use_zoom_to_mouse = True

        return {'FINISHED'}


class Timeline_ZoomOut_10s(bpy.types.Operator):
    """Zooms out aproximatelly 10s of Timeline"""
    bl_idname = "sequencer.timeline_zoom_out_10s"
    bl_label = "Timeline - Zoom Out 10s"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcuts: Shift + End; Ctrl + Shift + Right Mouse Click

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        preferences = bpy.context.preferences
        mouse = False

        if (preferences.inputs.use_zoom_to_mouse is True):
            mouse = True
            preferences.inputs.use_zoom_to_mouse = False

        bpy.ops.view2d.zoom(deltax=-150.0, deltay=0.0)

        if (mouse is True):
            preferences.inputs.use_zoom_to_mouse = True

        return {'FINISHED'}


class Timeline_ZoomOutXY(bpy.types.Operator):
    """Zooms out aproximatelly 10s of Timeline + Y Axis"""
    bl_idname = "sequencer.timeline_zoom_out_xy"
    bl_label = "Timeline - Zoom Out XY Axis"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcuts: Ctrl + Shift + End

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        preferences = bpy.context.preferences
        mouse = False

        if (preferences.inputs.use_zoom_to_mouse is True):
            mouse = True
            preferences.inputs.use_zoom_to_mouse = False

        #bpy.ops.view2d.zoom(deltax=-150.0, deltay=-100.0)
        bpy.ops.view2d.zoom(deltax=-150.0, deltay=-2.0)

        if (mouse is True):
            preferences.inputs.use_zoom_to_mouse = True

        return {'FINISHED'}


class Timeline_ZoomToPlayhead(bpy.types.Operator):
    """Zooms timeline to playhead if it is over any strips"""
    bl_idname = "sequencer.timeline_zoom_to_playhead"
    bl_label = "Timeline - Zoom to Playhead"
    bl_options = {'REGISTER', 'UNDO'}
    # Shortcuts: Shift + Right Mouse Click

    @classmethod
    def poll(cls, context):
        return bpy.context.scene is not None

    def execute(self, context):
        currentFrame = bpy.context.scene.frame_current
        sequencer = bpy.ops.sequencer

        sequencer.select_all(action='DESELECT')
        bpy.context.scene.sequence_editor.active_strip = None

        for strip in bpy.context.sequences:
            stripStart = strip.frame_start + strip.frame_offset_start
            if (stripStart < currentFrame < strip.frame_final_end):
                strip.select = True

        sequencer.view_selected()
        #sequencer.view_zoom_ratio(ratio=0.02)

        sequencer.select_all(action='DESELECT')

        return {'FINISHED'}


classes = (
    Audio_Strips_Display_Waveform,
    Audio_Strips_Hide_Waveform,
    Delete_Direct,
    Delete_Direct_Gaps,
    Fade_In_Strip_Start,
    Fade_Out_Strip_End,
    Markers_Delete_Closest,
    Markers_Goto_Left,
    Markers_Goto_Right,
    Scene_Toggle,
    Set_End_Frame_In_Last,
    Set_Start_Frame_In_One,
    Slight_Desync_Adjust,
    Snap_Selected_To_Playhead,
    Snap_Selected_To_TimelineStart,
    Strips_Channel_Up,
    Strips_Channel_Down,
    Strips_Concatenate_Selected,
    Strips_Deinterlace_Selected,
    Strips_Remove_Deinterlace,
    Timeline_Loop_Selected,
    Timeline_Select_Inside_Preview,
    Timeline_View_Selected_Context,
    Timeline_ZoomIn_10s,
    Timeline_ZoomOut_10s,
    Timeline_ZoomOutXY,
    Timeline_ZoomToPlayhead,
)

register, unregister = bpy.utils.register_classes_factory(classes)


if __name__ == "__main__":
    register()
