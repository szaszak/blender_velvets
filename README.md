blender_velvet
==============

Description:

Glamorous new functions for video editing in Blender VSE, with shortcuts more adapted 
to video editing use and interface changes to eliminate redundancy in Blender's windows.

Aimed for video editors. To be used with lots of glitter.


Interface changes (space_sequencer):
------------------------------------

If you take a look at the screenshots below, you can take a glimpse at the modifications:
http://florestavermelha.files.wordpress.com/2013/05/blender_rios_e_ruas01.jpg
http://florestavermelha.files.wordpress.com/2013/05/blender_rios_e_ruas021.jpg

Notice that the changes aimed at completely eliminating the "Timeline" window, that is
somewhat messy and redundant for video editing - all its controls are now at the VSE window
and all the controls related to the timeline are in the ::velvet_goldmine:: new functions and
shortcuts.

Also, there is new information on the VSE main window and the VSE viewer window related to
the timeline and strip's duration in SMTPE (human-readable) and project render and FPS settings.

I also included on the VSE viewer properties the "Sequencer modifiers" and the most relevant
things that relate to video strips (click on a video strip on the timeline to check it out).
This is because it seemed easier to control the image from the VSE viewer instead of the VSE timeline.


Changes in standard shortcuts:
------------------------------

Beyond adding the new functions/shortcuts, velvet_shortcuts also
changes the current standard shortcuts:

"A" now selects all strips;
"Alt+A" now deselects all strips;
"Spacebar" now plays the video (animation);
"B" - Border select selects what you want (the box) and discards the rest;
"Alt+B" - Border select adds what you want (the box) to current selected strips;
"Del" - Delects without prompting for confirmation;
"G" - Makes meta-strip without prompting for confirmation;
"Ctrl+S" - Saves the file without prompting for confirmation;
"Left Mouse Click" - now selects strips with linked time by default (audio + video);
"Ctrl+Left Mouse Click" - selects strips disregarding linked time;
"Ctrl+Right Mouse Click" - view all (equivalent to "Home", without having to abandon the mouse);


New functions - ::velvet_goldmine::
-----------------------------------

The functions' names and descriptions below should help you understand what they do until I have
time to make a better documentation. If you want a visual but initial documentation on video,
see this link: http://florestavermelha.org/2013/02/28/blender-novas-funcoes-o-video-explicativo/

Highlights go to markers improved controls (easy removal of closest) and navigation; easier audio
control (waveform and panning) and elimination of the need for a "Timeline" window because all
the timeline can now be controlled directly from the VSE window via shortcuts.

It must be said that ::velvet_goldmine:: normally sets frame_start and frame_preview_start together,
because in almost all the cases, that's what an editor really want - to render the range he has set
for his timeline. Otherwise, it would be a bit confusing.


    "Audio Pan Toggle"
    """Toggles audio pan between 0.0, 1.0 and -1.0 for selected strips"""
    # Shortcut: Ctrl + P

    "Cut and delete - Left"
    """Cuts selected strips, deletes to the left"""
    # Shortcut: Ctrl + K

    "Cut and delete - Left, Select"
    """Cuts selected strips, deletes to the left, selects remaining"""
    # Shortcut: Ctrl + Shift + K

    "Cut and delete - Right"
    """Cuts selected strips, deletes to the right"""
    # Shortcut: Alt + K

    "Cut and delete - Right, Select"
    """Cuts selected strips, deletes to the right, selects remaining"""
    # Shortcut: Ctrl + Alt + K

    "Delete Direct"
    """Deletes without prompting for confirmation"""
    # Shortcut: Delete

    "Fade In - Strip Start"
    """Creates a one second fade in (for audio and/or video) at strip start"""
    # Shortcut: Ctrl + F

    "Fade Out - Strip End"
    """Creates a one second fade out (for audio and/or video) at strip end"""
    # Shortcut: Alt + F

    "Markers - Delete Closest"
    """Deletes the closest marker to the cursor"""
    # Shortcut: Alt + M

    "Markers - Go to Left Marker"
    """Moves cursor to left marker position"""
    # Shortcut: Ctrl + LeftArrow

    "Markers - Go to Right Marker"
    """Moves cursor to right marker position"""
    # Shortcut: Ctrl + RightArrow

    "MetaStrip - Make Direct"
    """Makes Meta Strip without prompting for confirmation"""
    # Shortcut: Ctrl + G

    "Proxy Editing Toggle"
    """Toggle filepath of current strips between Proxies / Original folders"""
    # Shortcuts: Ctrl + Alt + Shift + P

    "Render - Resolution Toggle"
    """Toggle between 30, 60 and 100 values in Resolution Percentage"""
    # Shortcut: Ctrl + Alt + Shift + R

    "Save Direct"
    """Saves current file without prompting for confirmation"""
    # Shortcut: Ctrl + S

    "Screens - Change to Animation"
    """Changes view to selected screens"""
    # Shortcuts: Ctrl + Shift + F2 - Animation

    "Screens - Change to Compositing"
    """Changes view to selected screens"""
    # Shortcuts: Ctrl + Shift + F3 - Compositing

    "Screens - Change to Motion Tracking"
    """Changes view to selected screens"""
    # Shortcuts: Ctrl + Shift + F4 - Motion Tracking

    "Screens - Change to Video Editing"
    """Changes view to selected screens"""
    # Shortcuts: Ctrl + Shift + F1 - Video Editing

    "Scene toggle"
    """Toggles between existing Scenes"""
    # Shortcuts: Ctrl + '

    "Strips - Adjust to Cursor"
    """Adjusts selected strips to where the cursor is in the timeline"""
    # Shortcut: Ctrl + Alt + Shift + C

    "Strips - Adjust to Start"
    """Adjusts selected strips to the beginning of the timeline"""
    # Shortcut: Ctrl + Alt + Shift + S

    "Strips - Channel Up"
    """Moves selected strip one channel up"""
    # Shortcut: Alt + UpArrow

    "Strips - Channel Down"
    """Moves selected strip one channel down"""
    # Shortcut: Alt + DownArrow

    "Strips - Jump to Next"
    """Jumps cursor to next beginning/end of strip"""
    # Shortcut: Ctrl + PgUp

    "Strips - Jump to Previous"
    """Jumps cursor to previous beginning/end of strip"""
    # Shortcut: Ctrl + PgDown

    "Strips - Concatenate Selected (Same channel)"
    """Concatenates selected strips in channel (only works for 1 channel)"""
    # Shortcut: Shift + C

    "Strips - Show Waveform"
    """Shows the audio waveform in selected strips (toggle)"""
    # Shortcut: Ctrl + Alt + Shift + W

    "Timeline - Adjust End"
    """Adjusts VSE Timeline according to last video"""
    # Shortcut: Alt + E

    "Timeline End to Current"
    """Sets Timeline end to current frame"""
    # Shortcut: Shift + E

    "Timeline Start to Current"
    """Sets Timeline start to current frame"""
    # Shortcut: Shift + Alt + S

    "Timeline Start to One"
    """Sets Timeline start to frame one"""
    # Shortcut: Alt + S

    "Timeline Loop Selected"
    """Sets Timeline start and end to selected strips"""
    # Shortcut: Ctrl + Alt + Shift + L

    "Timeline - Select Inside Preview"
    """Selects only the strips inside Timeline preview"""
    # Shortcut: Ctrl + Alt + Shift + A

    "Timeline - View Selected Closer"
    """Alternative to View Selected (closer view)"""
    # Shortcuts: End

    "Timeline - Zoom In 10s"
    """Zooms in aproximatelly 10s of Timeline"""
    # Shortcuts: Ctrl + Home

    "Timeline - Zoom Out 10s"
    """Zooms out aproximatelly 10s of Timeline"""
    # Shortcuts: Ctrl + End; Ctrl + Shift + Right Mouse Click

    "Timeline - Zoom Out XY Axis"
    """Zooms out aproximatelly 10s of Timeline + Y Axis"""
    # Shortcuts: Ctrl + Shift + End

    "Timeline - Zoom to Cursor"
    """Zooms timeline to green ibeam (cursor) if it is over any strips"""
    # Shortcuts: Shift + Right Mouse Click
