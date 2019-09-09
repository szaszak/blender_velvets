# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


# Velvet Shortcuts version date: 20190909
# To be used with Blender versions 2.80
# Check documentation at http://blendervelvets.org
# Author: szaszak


import bpy
import os

def kmi_props_setattr(kmi_props, attr, value):
    try:
        setattr(kmi_props, attr, value)
    except AttributeError:
        print("Warning: property '%s' not found in keymap item '%s'" %
              (attr, kmi_props.__class__.__name__))
    except Exception as e:
        print("Warning: %r" % e)

wm = bpy.context.window_manager
kc = wm.keyconfigs.new(os.path.splitext(os.path.basename(__file__))[0])

# Map Window
km = kc.keymaps.new('Window', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('wm.window_duplicate', 'W', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('wm.read_homefile', 'N', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.save_homefile', 'U', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.call_menu', 'O', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'name', 'INFO_MT_file_open_recent')
kmi = km.keymap_items.new('wm.open_mainfile', 'O', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.open_mainfile', 'F1', 'PRESS')
kmi = km.keymap_items.new('wm.link', 'O', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('wm.append', 'F1', 'PRESS', shift=True)
kmi = km.keymap_items.new('wm.save_mainfile', 'S', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.save_mainfile', 'W', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.save_as_mainfile', 'S', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('wm.save_as_mainfile', 'F2', 'PRESS')
kmi = km.keymap_items.new('wm.save_as_mainfile', 'S', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'copy', True)
kmi = km.keymap_items.new('wm.window_fullscreen_toggle', 'F11', 'PRESS', alt=True)
kmi = km.keymap_items.new('wm.quit_blender', 'Q', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.doc_view_manual_ui_context', 'F1', 'PRESS', alt=True)
kmi = km.keymap_items.new('wm.redraw_timer', 'T', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('wm.debug_menu', 'D', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('wm.search_menu', 'SPACE', 'PRESS')
kmi = km.keymap_items.new('wm.call_menu', 'NDOF_BUTTON_MENU', 'PRESS')
kmi_props_setattr(kmi.properties, 'name', 'USERPREF_MT_ndof_settings')
kmi = km.keymap_items.new('wm.context_set_enum', 'F2', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'LOGIC_EDITOR')
kmi = km.keymap_items.new('wm.context_set_enum', 'F3', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'NODE_EDITOR')
kmi = km.keymap_items.new('wm.context_set_enum', 'F4', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'CONSOLE')
kmi = km.keymap_items.new('wm.context_set_enum', 'F5', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'VIEW_3D')
kmi = km.keymap_items.new('wm.context_set_enum', 'F6', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'GRAPH_EDITOR')
kmi = km.keymap_items.new('wm.context_set_enum', 'F7', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'PROPERTIES')
kmi = km.keymap_items.new('wm.context_set_enum', 'F8', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'SEQUENCE_EDITOR')
kmi = km.keymap_items.new('wm.context_set_enum', 'F9', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'OUTLINER')
kmi = km.keymap_items.new('wm.context_set_enum', 'F10', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'IMAGE_EDITOR')
kmi = km.keymap_items.new('wm.context_set_enum', 'F11', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'TEXT_EDITOR')
kmi = km.keymap_items.new('wm.context_set_enum', 'F12', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
kmi_props_setattr(kmi.properties, 'value', 'DOPESHEET_EDITOR')
kmi = km.keymap_items.new('wm.context_scale_float', 'NDOF_BUTTON_PLUS', 'PRESS')
kmi_props_setattr(kmi.properties, 'data_path', 'user_preferences.inputs.ndof_sensitivity')
kmi_props_setattr(kmi.properties, 'value', 1.100000023841858)
kmi = km.keymap_items.new('wm.context_scale_float', 'NDOF_BUTTON_MINUS', 'PRESS')
kmi_props_setattr(kmi.properties, 'data_path', 'user_preferences.inputs.ndof_sensitivity')
kmi_props_setattr(kmi.properties, 'value', 0.9090908765792847)
kmi = km.keymap_items.new('wm.context_scale_float', 'NDOF_BUTTON_PLUS', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'user_preferences.inputs.ndof_sensitivity')
kmi_props_setattr(kmi.properties, 'value', 1.5)
kmi = km.keymap_items.new('wm.context_scale_float', 'NDOF_BUTTON_MINUS', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'user_preferences.inputs.ndof_sensitivity')
kmi_props_setattr(kmi.properties, 'value', 0.6666666865348816)
kmi = km.keymap_items.new('info.reports_display_update', 'TIMER_REPORT', 'ANY', any=True)

# Map Screen
km = kc.keymaps.new('Screen', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('screen.animation_step', 'TIMER0', 'ANY', any=True)
kmi = km.keymap_items.new('screen.region_blend', 'TIMERREGION', 'ANY', any=True)
kmi = km.keymap_items.new('screen.screen_set', 'RIGHT_ARROW', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'delta', 1)
kmi = km.keymap_items.new('screen.screen_set', 'LEFT_ARROW', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'delta', -1)
kmi = km.keymap_items.new('screen.screen_full_area', 'UP_ARROW', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.screen_full_area', 'DOWN_ARROW', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.screen_full_area', 'SPACE', 'PRESS', shift=True)
kmi = km.keymap_items.new('screen.screen_full_area', 'F10', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'use_hide_panels', True)
kmi = km.keymap_items.new('screen.screenshot', 'F3', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.screencast', 'F3', 'PRESS', alt=True)
kmi = km.keymap_items.new('screen.space_context_cycle', 'TAB', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'direction', 'NEXT')
kmi = km.keymap_items.new('screen.space_context_cycle', 'TAB', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'direction', 'PREV')
kmi = km.keymap_items.new('screen.region_quadview', 'Q', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('screen.repeat_history', 'F3', 'PRESS')
kmi = km.keymap_items.new('screen.repeat_last', 'R', 'PRESS', shift=True)
kmi = km.keymap_items.new('screen.region_flip', 'F5', 'PRESS')
kmi = km.keymap_items.new('screen.redo_last', 'F6', 'PRESS')
kmi = km.keymap_items.new('script.reload', 'F8', 'PRESS')
kmi = km.keymap_items.new('file.execute', 'RET', 'PRESS')
kmi = km.keymap_items.new('file.execute', 'NUMPAD_ENTER', 'PRESS')
kmi = km.keymap_items.new('file.cancel', 'ESC', 'PRESS')
kmi = km.keymap_items.new('ed.undo', 'Z', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('ed.redo', 'Z', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('ed.undo_history', 'Z', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('render.render', 'F12', 'PRESS')
kmi_props_setattr(kmi.properties, 'use_viewport', True)
kmi = km.keymap_items.new('render.render', 'F12', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'animation', True)
kmi_props_setattr(kmi.properties, 'use_viewport', True)
kmi = km.keymap_items.new('render.view_cancel', 'ESC', 'PRESS')
kmi = km.keymap_items.new('render.view_show', 'F11', 'PRESS')
kmi = km.keymap_items.new('render.play_rendered_anim', 'F11', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.userpref_show', 'U', 'PRESS', ctrl=True, alt=True)

# Map Frames
km = kc.keymaps.new('Frames', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('screen.frame_offset', 'UP_ARROW', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'delta', 10)
kmi = km.keymap_items.new('screen.frame_offset', 'DOWN_ARROW', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'delta', -10)
kmi = km.keymap_items.new('screen.frame_offset', 'LEFT_ARROW', 'PRESS')
kmi_props_setattr(kmi.properties, 'delta', -1)
kmi = km.keymap_items.new('screen.frame_offset', 'RIGHT_ARROW', 'PRESS')
kmi_props_setattr(kmi.properties, 'delta', 1)
kmi = km.keymap_items.new('screen.frame_offset', 'WHEELDOWNMOUSE', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'delta', 1)
kmi = km.keymap_items.new('screen.frame_offset', 'WHEELUPMOUSE', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'delta', -1)
kmi = km.keymap_items.new('screen.frame_jump', 'UP_ARROW', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'end', True)
kmi = km.keymap_items.new('screen.frame_jump', 'DOWN_ARROW', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'end', False)
kmi = km.keymap_items.new('screen.frame_jump', 'RIGHT_ARROW', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'end', True)
kmi = km.keymap_items.new('screen.frame_jump', 'LEFT_ARROW', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'end', False)
kmi = km.keymap_items.new('screen.keyframe_jump', 'UP_ARROW', 'PRESS')
kmi_props_setattr(kmi.properties, 'next', True)
kmi = km.keymap_items.new('screen.keyframe_jump', 'DOWN_ARROW', 'PRESS')
kmi_props_setattr(kmi.properties, 'next', False)
kmi = km.keymap_items.new('screen.keyframe_jump', 'MEDIA_LAST', 'PRESS')
kmi_props_setattr(kmi.properties, 'next', True)
kmi = km.keymap_items.new('screen.keyframe_jump', 'MEDIA_FIRST', 'PRESS')
kmi_props_setattr(kmi.properties, 'next', False)
kmi = km.keymap_items.new('screen.animation_play', 'SPACE', 'PRESS')
kmi = km.keymap_items.new('screen.animation_play', 'SPACE', 'PRESS', shift=True, alt=True)
kmi_props_setattr(kmi.properties, 'reverse', True)
kmi = km.keymap_items.new('screen.animation_cancel', 'ESC', 'PRESS')
kmi = km.keymap_items.new('screen.animation_play', 'MEDIA_PLAY', 'PRESS')
kmi = km.keymap_items.new('screen.animation_cancel', 'MEDIA_STOP', 'PRESS')

# Map Sequencer
km = kc.keymaps.new('Sequencer', space_type='SEQUENCE_EDITOR', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('sequencer.refresh_all', 'R', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.select_all', 'A', 'PRESS')
kmi_props_setattr(kmi.properties, 'action', 'SELECT')
kmi = km.keymap_items.new('sequencer.select_all', 'A', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'action', 'DESELECT')
kmi = km.keymap_items.new('sequencer.select_all', 'I', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'action', 'INVERT')
kmi = km.keymap_items.new('sequencer.cut', 'K', 'PRESS')
kmi_props_setattr(kmi.properties, 'type', 'SOFT')
kmi = km.keymap_items.new('sequencer.cut', 'K', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'type', 'HARD')
kmi = km.keymap_items.new('sequencer.mute', 'H', 'PRESS')
kmi_props_setattr(kmi.properties, 'unselected', False)
kmi = km.keymap_items.new('sequencer.mute', 'H', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'unselected', True)
kmi = km.keymap_items.new('sequencer.unmute', 'H', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'unselected', False)
kmi = km.keymap_items.new('sequencer.unmute', 'H', 'PRESS', shift=True, alt=True)
kmi_props_setattr(kmi.properties, 'unselected', True)
kmi = km.keymap_items.new('sequencer.lock', 'L', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.unlock', 'L', 'PRESS', shift=True, alt=True)
kmi = km.keymap_items.new('sequencer.reassign_inputs', 'R', 'PRESS')
kmi = km.keymap_items.new('sequencer.reload', 'R', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.reload', 'R', 'PRESS', shift=True, alt=True)
kmi_props_setattr(kmi.properties, 'adjust_length', True)
kmi = km.keymap_items.new('sequencer.offset_clear', 'O', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.duplicate_move', 'D', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.delete', 'X', 'PRESS')
kmi = km.keymap_items.new('sequencer.delete_direct', 'DEL', 'PRESS')
kmi = km.keymap_items.new('sequencer.delete_direct_gaps', 'DEL', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.copy', 'C', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.paste', 'V', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.images_separate', 'Y', 'PRESS')
kmi = km.keymap_items.new('sequencer.meta_toggle', 'TAB', 'PRESS')
kmi = km.keymap_items.new('sequencer.meta_make', 'G', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.meta_separate', 'G', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.view_all', 'HOME', 'PRESS')
kmi = km.keymap_items.new('sequencer.view_all', 'NDOF_BUTTON_FIT', 'PRESS')
kmi = km.keymap_items.new('sequencer.view_all', 'RIGHTMOUSE', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.view_selected', 'NUMPAD_PERIOD', 'PRESS')
kmi = km.keymap_items.new('sequencer.view_selected', 'HOME', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.view_selected', 'DEL', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.strip_jump', 'PAGE_UP', 'PRESS')
kmi_props_setattr(kmi.properties, 'next', True)
kmi_props_setattr(kmi.properties, 'center', False)
kmi = km.keymap_items.new('sequencer.strip_jump', 'PAGE_DOWN', 'PRESS')
kmi_props_setattr(kmi.properties, 'next', False)
kmi_props_setattr(kmi.properties, 'center', False)
kmi = km.keymap_items.new('sequencer.strip_jump', 'PAGE_UP', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'next', True)
kmi_props_setattr(kmi.properties, 'center', True)
kmi = km.keymap_items.new('sequencer.strip_jump', 'PAGE_DOWN', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'next', False)
kmi_props_setattr(kmi.properties, 'center', True)
kmi = km.keymap_items.new('sequencer.swap', 'LEFT_ARROW', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'side', 'LEFT')
kmi = km.keymap_items.new('sequencer.swap', 'RIGHT_ARROW', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'side', 'RIGHT')
kmi = km.keymap_items.new('sequencer.gap_remove', 'BACK_SPACE', 'PRESS')
kmi_props_setattr(kmi.properties, 'all', False)
kmi = km.keymap_items.new('sequencer.gap_remove', 'BACK_SPACE', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'all', True)
kmi = km.keymap_items.new('sequencer.gap_insert', 'EQUAL', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.snap', 'S', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.swap_inputs', 'S', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'ONE', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 1)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'TWO', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 2)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'THREE', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 3)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'FOUR', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 4)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'FIVE', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 5)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'SIX', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 6)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'SEVEN', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 7)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'EIGHT', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 8)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'NINE', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 9)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'ZERO', 'PRESS')
kmi_props_setattr(kmi.properties, 'camera', 10)
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS')
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'linked_handle', False)
kmi_props_setattr(kmi.properties, 'left_right', 'NONE')
kmi_props_setattr(kmi.properties, 'linked_time', True)
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi_props_setattr(kmi.properties, 'linked_handle', False)
kmi_props_setattr(kmi.properties, 'left_right', 'NONE')
kmi_props_setattr(kmi.properties, 'linked_time', False)
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS', shift=True, alt=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi_props_setattr(kmi.properties, 'linked_handle', True)
kmi_props_setattr(kmi.properties, 'left_right', 'NONE')
kmi_props_setattr(kmi.properties, 'linked_time', False)
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'linked_handle', True)
kmi_props_setattr(kmi.properties, 'left_right', 'NONE')
kmi_props_setattr(kmi.properties, 'linked_time', False)
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'linked_handle', False)
kmi_props_setattr(kmi.properties, 'left_right', 'NONE')
kmi_props_setattr(kmi.properties, 'linked_time', False)
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi_props_setattr(kmi.properties, 'linked_handle', False)
kmi_props_setattr(kmi.properties, 'left_right', 'NONE')
kmi_props_setattr(kmi.properties, 'linked_time', True)
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS')
kmi_props_setattr(kmi.properties, 'left_right', 'MOUSE')
kmi = km.keymap_items.new('sequencer.select_more', 'NUMPAD_PLUS', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.select_less', 'NUMPAD_MINUS', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.select_linked_pick', 'L', 'PRESS')
kmi_props_setattr(kmi.properties, 'extend', False)
kmi = km.keymap_items.new('sequencer.select_linked_pick', 'L', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi = km.keymap_items.new('sequencer.select_linked', 'L', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.select_border', 'B', 'PRESS')
kmi_props_setattr(kmi.properties, 'extend', False)
kmi = km.keymap_items.new('sequencer.select_grouped', 'G', 'PRESS', shift=True)
kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'name', 'SEQUENCER_MT_add')
kmi = km.keymap_items.new('wm.call_menu', 'C', 'PRESS')
kmi_props_setattr(kmi.properties, 'name', 'SEQUENCER_MT_change')
kmi = km.keymap_items.new('sequencer.slip', 'S', 'PRESS')
kmi = km.keymap_items.new('wm.context_set_int', 'O', 'PRESS')
kmi_props_setattr(kmi.properties, 'data_path', 'scene.sequence_editor.overlay_frame')
kmi_props_setattr(kmi.properties, 'value', 0)
kmi = km.keymap_items.new('transform.seq_slide', 'G', 'PRESS')
kmi = km.keymap_items.new('transform.seq_slide', 'EVT_TWEAK_S', 'ANY')
kmi = km.keymap_items.new('transform.transform', 'E', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'TIME_EXTEND')
kmi = km.keymap_items.new('marker.add', 'M', 'PRESS')
kmi = km.keymap_items.new('marker.rename', 'M', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.select_border', 'B', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.fade_in_strip_start', 'F', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.fade_out_strip_end', 'F', 'PRESS', alt=True)
#kmi = km.keymap_items.new('sequencer.marker_delete_closest', 'M', 'PRESS', alt=True)
#kmi = km.keymap_items.new('sequencer.marker_goto_left', 'LEFT_ARROW', 'PRESS', ctrl=True)
#kmi = km.keymap_items.new('sequencer.marker_goto_right', 'RIGHT_ARROW', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.scene_toggle', 'TAB', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.slight_desync_adjust', 'D', 'PRESS', shift=True, ctrl=True, alt=True)
kmi = km.keymap_items.new('sequencer.snap_sequence_to_playhead', 'C', 'PRESS', shift=True, ctrl=True, alt=True)
kmi = km.keymap_items.new('sequencer.snap_sequence_to_timelinestart', 'S', 'PRESS', shift=True, ctrl=True, alt=True)
kmi = km.keymap_items.new('sequencer.strip_up', 'UP_ARROW', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.strip_down', 'DOWN_ARROW', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.strips_concatenate_selected', 'C', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.strips_deinterlace', 'I', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('sequencer.strips_deinterlace_off', 'I', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('sequencer.strips_display_waveform', 'W', 'PRESS')
kmi = km.keymap_items.new('sequencer.strips_hide_waveform', 'W', 'PRESS', alt=True)
#kmi = km.keymap_items.new('anim.end_frame_last_set', 'END', 'PRESS', alt=True)
#kmi = km.keymap_items.new('anim.start_frame_one_set', 'HOME', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.timeline_loop_selected', 'L', 'PRESS', shift=True, ctrl=True, alt=True)
kmi = km.keymap_items.new('sequencer.timeline_preview_select', 'A', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('sequencer.view_selected_context', 'END', 'PRESS')
kmi = km.keymap_items.new('sequencer.timeline_zoom_in_10s', 'HOME', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.timeline_zoom_out_10s', 'END', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.timeline_zoom_out_10s', 'RIGHTMOUSE', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('sequencer.timeline_zoom_out_xy', 'END', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('sequencer.timeline_zoom_to_playhead', 'RIGHTMOUSE', 'PRESS', shift=True)
