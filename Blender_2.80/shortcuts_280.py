keyconfig_data = \
[("Animation",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("wm.context_toggle",
     {"type": 'T', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("data_path", 'space_data.show_seconds'),
       ],
      },
     ),
    ("anim.previewrange_set", {"type": 'P', "value": 'PRESS'}, None),
    ("anim.previewrange_clear", {"type": 'P', "value": 'PRESS', "alt": True}, None),
    ("anim.start_frame_set", {"type": 'HOME', "value": 'PRESS', "ctrl": True}, None),
    ("anim.start_frame_one_set", {"type": 'HOME', "value": 'PRESS', "alt": True}, None),
    ("anim.end_frame_set", {"type": 'END', "value": 'PRESS', "ctrl": True}, None),
    ("anim.end_frame_last_set", {"type": 'END', "value": 'PRESS', "alt": True}, None),
    ("anim.change_frame", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
    ],
   },
  ),
 ("Sequencer",
  {"space_type": 'SEQUENCE_EDITOR', "region_type": 'WINDOW'},
  {"items":
   [("sequencer.select_all",
     {"type": 'A', "value": 'PRESS'},
     {"properties":
      [("action", 'SELECT'),
       ],
      },
     ),
    ("sequencer.select_all",
     {"type": 'A', "value": 'PRESS', "alt": True},
     {"properties":
      [("action", 'DESELECT'),
       ],
      },
     ),
    ("sequencer.select_all",
     {"type": 'I', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("action", 'INVERT'),
       ],
      },
     ),
    ("sequencer.select_all",
     {"type": 'A', "value": 'DOUBLE_CLICK'},
     {"properties":
      [("action", 'DESELECT'),
       ],
      },
     ),
    ("sequencer.cut",
     {"type": 'K', "value": 'PRESS'},
     {"properties":
      [("type", 'SOFT'),
       ],
      },
     ),
    ("sequencer.cut",
     {"type": 'K', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'HARD'),
       ],
      },
     ),
    ("sequencer.mute",
     {"type": 'H', "value": 'PRESS'},
     {"properties":
      [("unselected", False),
       ],
      },
     ),
    ("sequencer.mute",
     {"type": 'H', "value": 'PRESS', "shift": True},
     {"properties":
      [("unselected", True),
       ],
      },
     ),
    ("sequencer.unmute",
     {"type": 'H', "value": 'PRESS', "alt": True},
     {"properties":
      [("unselected", False),
       ],
      },
     ),
    ("sequencer.unmute",
     {"type": 'H', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("unselected", True),
       ],
      },
     ),
    ("sequencer.lock", {"type": 'L', "value": 'PRESS', "shift": True}, None),
    ("sequencer.unlock", {"type": 'L', "value": 'PRESS', "shift": True, "alt": True}, None),
    ("sequencer.reassign_inputs", {"type": 'R', "value": 'PRESS'}, None),
    ("sequencer.reload", {"type": 'R', "value": 'PRESS', "alt": True}, None),
    ("sequencer.reload",
     {"type": 'R', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("adjust_length", True),
       ],
      },
     ),
    ("sequencer.refresh_all", {"type": 'R', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.offset_clear", {"type": 'O', "value": 'PRESS', "alt": True}, None),
    ("sequencer.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
    ("sequencer.delete", {"type": 'X', "value": 'PRESS'}, None),
    ("sequencer.delete", {"type": 'DEL', "value": 'PRESS'}, None),
    ("sequencer.copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.paste", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.images_separate", {"type": 'Y', "value": 'PRESS'}, None),
    ("sequencer.meta_toggle", {"type": 'TAB', "value": 'PRESS'}, None),
    ("sequencer.meta_make", {"type": 'G', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.meta_separate", {"type": 'G', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("sequencer.view_all", {"type": 'HOME', "value": 'PRESS'}, None),
    ("sequencer.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
    ("sequencer.view_selected", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
    ("sequencer.view_frame", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
    ("sequencer.strip_jump",
     {"type": 'PAGE_UP', "value": 'PRESS'},
     {"properties":
      [("next", True),
       ("center", False),
       ],
      },
     ),
    ("sequencer.strip_jump",
     {"type": 'PAGE_DOWN', "value": 'PRESS'},
     {"properties":
      [("next", False),
       ("center", False),
       ],
      },
     ),
    ("sequencer.strip_jump",
     {"type": 'PAGE_UP', "value": 'PRESS', "alt": True},
     {"properties":
      [("next", True),
       ("center", True),
       ],
      },
     ),
    ("sequencer.strip_jump",
     {"type": 'PAGE_DOWN', "value": 'PRESS', "alt": True},
     {"properties":
      [("next", False),
       ("center", True),
       ],
      },
     ),
    ("sequencer.swap",
     {"type": 'LEFT_ARROW', "value": 'PRESS', "alt": True},
     {"properties":
      [("side", 'LEFT'),
       ],
      },
     ),
    ("sequencer.swap",
     {"type": 'RIGHT_ARROW', "value": 'PRESS', "alt": True},
     {"properties":
      [("side", 'RIGHT'),
       ],
      },
     ),
    ("sequencer.gap_remove",
     {"type": 'BACK_SPACE', "value": 'PRESS'},
     {"properties":
      [("all", False),
       ],
      },
     ),
    ("sequencer.gap_remove",
     {"type": 'BACK_SPACE', "value": 'PRESS', "shift": True},
     {"properties":
      [("all", True),
       ],
      },
     ),
    ("sequencer.gap_insert", {"type": 'EQUAL', "value": 'PRESS', "shift": True}, None),
    ("sequencer.snap", {"type": 'S', "value": 'PRESS', "shift": True}, None),
    ("sequencer.swap_inputs", {"type": 'S', "value": 'PRESS', "alt": True}, None),
    ("sequencer.cut_multicam",
     {"type": 'ONE', "value": 'PRESS'},
     {"properties":
      [("camera", 1),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'TWO', "value": 'PRESS'},
     {"properties":
      [("camera", 2),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'THREE', "value": 'PRESS'},
     {"properties":
      [("camera", 3),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'FOUR', "value": 'PRESS'},
     {"properties":
      [("camera", 4),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'FIVE', "value": 'PRESS'},
     {"properties":
      [("camera", 5),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'SIX', "value": 'PRESS'},
     {"properties":
      [("camera", 6),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'SEVEN', "value": 'PRESS'},
     {"properties":
      [("camera", 7),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'EIGHT', "value": 'PRESS'},
     {"properties":
      [("camera", 8),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'NINE', "value": 'PRESS'},
     {"properties":
      [("camera", 9),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'ZERO', "value": 'PRESS'},
     {"properties":
      [("camera", 10),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'LEFTMOUSE', "value": 'PRESS'},
     {"properties":
      [("extend", False),
       ("deselect_all", True),
       ("linked_handle", False),
       ("left_right", 'NONE'),
       ("linked_time", True),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},
     {"properties":
      [("extend", True),
       ("linked_handle", False),
       ("left_right", 'NONE'),
       ("linked_time", False),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True},
     {"properties":
      [("extend", False),
       ("linked_handle", True),
       ("left_right", 'NONE'),
       ("linked_time", False),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("extend", True),
       ("linked_handle", True),
       ("left_right", 'NONE'),
       ("linked_time", False),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True},
     {"properties":
      [("extend", False),
       ("linked_handle", False),
       ("left_right", 'MOUSE'),
       ("linked_time", True),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
     {"properties":
      [("extend", True),
       ("linked_handle", False),
       ("left_right", 'MOUSE'),
       ("linked_time", True),
       ],
      },
     ),
    ("sequencer.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.select_linked_pick",
     {"type": 'L', "value": 'PRESS'},
     {"properties":
      [("extend", False),
       ],
      },
     ),
    ("sequencer.select_linked_pick",
     {"type": 'L', "value": 'PRESS', "shift": True},
     {"properties":
      [("extend", True),
       ],
      },
     ),
    ("sequencer.select_linked", {"type": 'L', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.select_box",
     {"type": 'EVT_TWEAK_L', "value": 'ANY'},
     {"properties":
      [("mode", 'SET'),
       ("tweak", True),
       ],
      },
     ),
    ("sequencer.select_box",
     {"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},
     {"properties":
      [("mode", 'ADD'),
       ("tweak", True),
       ],
      },
     ),
    ("sequencer.select_box",
     {"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},
     {"properties":
      [("mode", 'SUB'),
       ("tweak", True),
       ],
      },
     ),
    ("sequencer.select_box", {"type": 'B', "value": 'PRESS'}, None),
    ("sequencer.select_grouped", {"type": 'G', "value": 'PRESS', "shift": True}, None),
    ("wm.call_menu",
     {"type": 'A', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'SEQUENCER_MT_add'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'C', "value": 'PRESS'},
     {"properties":
      [("name", 'SEQUENCER_MT_change'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'SEQUENCER_MT_context_menu'),
       ],
      },
     ),
    ("sequencer.slip", {"type": 'S', "value": 'PRESS'}, None),
    ("wm.context_set_int",
     {"type": 'O', "value": 'PRESS'},
     {"properties":
      [("data_path", 'scene.sequence_editor.overlay_frame'),
       ("value", 0),
       ],
      },
     ),
    ("transform.seq_slide", {"type": 'G', "value": 'PRESS'}, None),
    ("transform.seq_slide", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
    ("transform.transform",
     {"type": 'E', "value": 'PRESS'},
     {"properties":
      [("mode", 'TIME_EXTEND'),
       ],
      },
     ),
    ("marker.add", {"type": 'M', "value": 'PRESS'}, None),
    ("marker.rename", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
    ],
   },
  ),
 ]


if __name__ == "__main__":
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data
    keyconfig_import_from_data(os.path.splitext(os.path.basename(__file__))[0], keyconfig_data)
