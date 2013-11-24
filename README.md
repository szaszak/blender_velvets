blender_velvet
==============

Glamorous new functions for video editing in Blender VSE, with shortcuts more adapted to video editing use and interface changes to eliminate redundancy in Blender's windows. 

Aimed for video editors. To be used with lots of glitter.


Install instructions
------------------------------------

    ::velvet_goldmine:: has been tested and works on Blender versions: 2.69, 2.68a, 2.66b, 2.66a, 
    2.66 and 2.65. There is no reason why it should not work on versions between those.

Download the .py files (there are three) and follow the steps below.

1. The <b>velvet_goldmine.py</b> file is where the new functions are. To enable them, open Blender and go to: <i>File > User Preferences > Addons tab > Install from file > Choose velvet_goldmine.py.</i> The addon <b>::velvet_goldmine::</b> will show up among the addons list - enable it by clicking on the small box to the right.

2. There is a set of suggested shortcuts that both change some of the standard hotkeys (check the list below) and assign new ones to be used with the new functions. They are at the <b>velvet_shortcuts.py</b> file. To import it, go to: <i>File > User Preferences > Input tab > Import Key Configuration > Choose velvet_shortcuts.py.</i> You're done: it will show up in the list and will already be your current shortcut set.

3. If you want to use the modified VSE interface (check the notes below), go to your \scripts\startup\bl_ui folder and replace the <b>space_sequencer.py</b> that is there by the one you just downloaded. It is wise to create a backup before doing so - Ctrl+C and Ctrl+V on the original will do the job.

If you want a screenshot-by-screenshot guide, it is here: https://szaszak.wordpress.com/linux/blender-como-editor-de-video/

Detailed description
------------------------------------

<h3>Interface changes (space_sequencer.py)</h3>


If you take a look at the screenshots below, you can take a glimpse at the modifications:<BR>
http://florestavermelha.files.wordpress.com/2013/05/blender_rios_e_ruas01.jpg<BR>
http://florestavermelha.files.wordpress.com/2013/05/blender_rios_e_ruas021.jpg

Notice that the changes aimed at completely eliminating the "Timeline" window, that is
somewhat messy and redundant for video editing - all its controls are now at the VSE window
and all the controls related to the timeline are in the <b>::velvet_goldmine::</b> addon.

Also, there is new information on the VSE main window and the VSE viewer window related to
the timeline and strips duration in SMTPE (human-readable), project render and FPS settings.

I also included on the VSE viewer properties the "Sequencer modifiers" and the most relevant
things that relate to video strips (click on a video strip on the timeline to check it out).
This is because it seemed easier to control the image from the VSE viewer instead of the VSE timeline.


<h3>Changes in standard shortcuts (velvet_shortcuts.py)</h3>

Beyond adding the new functions/shortcuts, velvet_shortcuts also changes the current standard shortcuts:

<b>"A"</b> now selects all strips;<BR>
<b>"Alt+A"</b> now deselects all strips;<BR>
<b>"Spacebar"</b> now plays the video (animation);<BR>
<b>"B"</b> - Border select selects what you want (the box) and discards the rest;<BR>
<b>"Alt+B"</b> - Border select adds what you want (the box) to current selected strips;<BR>
<b>"Del"</b> - Delects without prompting for confirmation;<BR>
<b>"G"</b> - Makes meta-strip without prompting for confirmation;<BR>
<b>"Ctrl+S"</b> - Saves the file without prompting for confirmation;<BR>
<b>"Shift+R"</b> - Refresh Sequencer;<BR>
<b>"Left Mouse Click"</b> - now selects strips with linked time by default (audio + video);<BR>
<b>"Ctrl+Left Mouse Click"</b> - selects strips disregarding linked time;<BR>
<b>"Ctrl+Right Mouse Click"</b> - view all (equivalent to "Home", without having to abandon the mouse);


<h3>New functions - the ::velvet_goldmine:: addon (velvet_goldmine.py + velvet_shortcuts.py)</h3>

The functions' names and descriptions below should help you understand what they do until I have
time to make a better documentation. If you want a visual but initial documentation on video,
see this link: http://florestavermelha.org/2013/02/28/blender-novas-funcoes-o-video-explicativo/

Highlights go to markers improved controls (easy removal of closest) and navigation; easier audio
control (waveform and panning) and elimination of the need for a "Timeline" window because all
the timeline can now be controlled directly from the VSE window via shortcuts.

It must be said that <b>::velvet_goldmine::</b> normally sets frame_start and frame_preview_start together,
because in almost all the cases, that's what an editor really want - to render the range he has set
for his timeline. Otherwise, it would be a bit confusing.

Observation 1: Panning audio in Blender only works with mono sources, be warned.

Observation 2: The proxy approach on this script is quite personal, due to the way Blender behaves with
different FPS sources. I'd rather equalize all source videos FPSs via script (and make them mono, by the
way) before editing, otherwise it'd be hell. Since I'm at it, I use the same script to make the proxies,
so <b>::velvet_goldmine::</b> just toggles the strips back to their original, full-sized sources, or to their proxies.


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
    # Shortcut: W

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
