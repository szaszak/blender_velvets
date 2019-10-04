the Blender Velvets
===================
![Blender Velvets](https://florestavermelha.files.wordpress.com/2014/02/velvet_goldmine_full.jpg)

<BR>
<p align="center">Glamorous new functions for video editing in Blender VSE. To be used with lots of glitter.</p>
<BR>

What are the Blender Velvets?
-----------------------------

The **Blender Velvets** are a series of Blender Addons (or plugins, if you prefer) for improving video editing with the VSE. They can be used separately or together, and at differet steps of video production. The velvets are:


###### ::velvet_revolver::

    ::velvet_revolver:: has been tested and works on Blender versions:
    2.80 (ffmpeg 4.2.1).
    There is no reason why it should not work on versions between those.
    For previous versions check README in Vintage_Blender/Blender_2.79.

The **::velvet_revolver::** is designed to make mass proxy generating an easy task for those lazy enough to open a terminal. It can create low definition intra-frame (meaning 360p ProRes422 or MJPEG) proxies from all your videos using Blender's own interface. Just point it to a folder and dance to the radio for a while. In case you have multiple FPS in your footage, notoriously crappy to use in Blender, Revolver can also create full-Res copies of your sources, levelling everything to your chosen FPS. *Read the full documentation at [Velvet Revolver's webpage](http://blendervelvets.org/en/velvet-revolver/) (in English, Portuguese, Spanish and French).*

###### ::velvet_goldmine::

    ::velvet_goldmine:: has been tested and works on Blender versions:
    2.80.
    There is no reason why it should not work on versions between those.
    For previous versions check README in Vintage_Blender/Blender_2.79.

The **::velvet_goldmine::** is a bunch of new functions and shortcuts aimed to fasten and loosen the overall hard VSE user interface. To be used with lots of glitter and with its companion, the *velvet_shortcuts*, for one can't dance alone, eh? *Read the full documentation at [Velvet Goldmine's webpage](http://blendervelvets.org/en/velvet-goldmine/) (in English, Portuguese, Spanish and French).*

###### ::blue_velvet::

    ::blue_velvet:: has been tested and works on Blender versions:
    2.80 (ffmpeg 4.2.1 and Ardour 5.12.0).
    There is no reason why it should not work on versions between those.
    For previous versions check README in Vintage_Blender/Blender_2.79.

You can edit in Blender, but there's no way you will get decent audio out of it. The program was simply not made for DAW uses, so stop whining. What **::blue_velvet::** does is to get your finished timeline and export the audio cuts directly to Ardour, the correct program to deal with them. *Read the full documentation at [Blue Velvet's webpage](http://blendervelvets.org/en/blue-velvet/) (in English, Portuguese, Spanish and French).*

###### ::modified_space_sequencer::

    the modified space_sequencer has been tested and works on Blender versions:
    2.80.
    There is no reason why it should not work on versions between those.
    For previous versions check README in Vintage_Blender/Blender_2.79.

Blender has an original space_sequencer, which is the VSE user interface. It is loaded every time the program starts. The use of a modified version of this script brings up a number of controls that exist but are hidden and adds some new and useful info for when you are in the middle of a project. *Read the full documentation at the [Modified Space Sequencer webpage](http://blendervelvets.org/en/space-sequencer/) (in English, Portuguese, Spanish and French).*
<BR>

General install instructions
----------------------------

Detailed instructions for installing the addons can be found on [this dedicated page](http://blendervelvets.org/en/blender-config/) (see [this section](http://blendervelvets.org/en/blender-config/#addons_install)). Instructions on how to use each addon can be seen on their respective pages at [blendervelvets.org](http://blendervelvets.org/) (in English, Portuguese, Spanish and French).
<BR>

::velvet_revolver:: shortcuts cheatsheet
--------------------------------------------

Shortcuts for ::velvet_revolver:: are:

    "Proxy Editing - Change to Proxies"
    """Change filepaths of current strips to proxy files (_proxy.mov)"""
    # Shortcut:  Ctrl + Alt + Shift + P (Blender 2.80 onwards)

    "Proxy Editing - Change to Full Resolution"
    """Change filepaths of current strips back to full-resolution files"""
    # Shortcut:  Ctrl + Shift + P (Blender 2.80 onwards)

    For previous versions check README in Vintage_Blender/Blender_2.79.

<BR>

::velvet_goldmine:: shortcuts cheatsheet
--------------------------------------------

#### Changes in the standard shortcuts (**velvet_shortcuts**)

Beyond adding the new functions/shortcuts, **velvet_shortcuts** also changes the current standard ones:

<b>"A"</b> now selects all strips (non toggle);<BR>
<b>"Alt+A"</b> now deselects all strips (non toggle);<BR>
<b>"Del"</b> - Deletes without prompting for confirmation (in MacOS: fn + Del);<BR>
<b>"Ctrl+S"</b> - Saves the file without prompting for confirmation;<BR>
<b>"Shift+R"</b> - Refresh Sequencer (cleans cache in RAM);<BR>
<b>"Left Mouse Click"</b> (strip) - now selects strips with linked time by default (audio + video);<BR>
<b>"Shift+Left Mouse"</b> (strip) - selects strips disregarding linked time (adds to selection for more than one strip);<BR>
<b>"Ctrl+Left Mouse"</b> (timeline) - now selects all strips on the left/right of the cursor;<BR>


#### New functions - the **::velvet_goldmine::** addon

    "Audio - Show Waveform"
    """Shows the audio waveform in selected strips"""
    # Shortcut: W
    
    "Audio - Hide Waveform"
    """Hides the audio waveform in selected strips"""
    # Shortcut: Alt + W

    "Delete Direct"
    """Deletes without prompting for confirmation"""
    # Shortcut: Delete
    # Shortcut for MacOS: Fn + Delete

    "Delete Direct - Remove Gaps"
    """Deletes removing gaps without prompting for confirmation"""
    # Shortcut: Ctrl + Delete

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

    "Scene toggle"
    """Toggles between existing Scenes"""
    # Shortcuts: Shift + TAB
    # May not work on Mac

    "Set End Frame in Last"
    """Sets Timeline end to last video frame"""
    # Shortcut: Alt + End

    "Set Start Frame in 1"
    """Sets Timeline start to frame one"""
    # Shortcut: Alt + Home

    "Slight Desync Adjust"
    """Adjust selected audio strips that are 1 frame bigger than its movies"""
    # Shortcut: Ctrl + Alt + Shift + D

    "Snap Selected to Playhead"
    """Adjusts selected strips to playhead in the timeline"""
    # Shortcut: Ctrl + Alt + Shift + C

    "Snap Selected to Timeline Start"
    """Adjusts selected strips to the beginning of the timeline"""
    # Shortcut: Ctrl + Alt + Shift + S

    "Strips - Channel Up"
    """Moves selected strips one channel up"""
    # Shortcut: Alt + UpArrow

    "Strips - Channel Down"
    """Moves selected strips one channel down"""
    # Shortcut: Alt + DownArrow

    "Strips - Concatenate Selected (Same channel)"
    """Concatenates selected strips in channel (only works for 1 channel)"""
    # Shortcut: Shift + C

    "Video Strips - Deinterlace Selected"
    """Deinterlace selected movie strips"""
    # Shortcut: Ctrl + Shift + I

    "Video Strips - Remove Deinterlace"
    """Remove deinterlace from selected movie strips"""
    # Shortcut: Ctrl + Alt + I

    "Timeline Loop Selected"
    """Sets Timeline start and end to selected strips"""
    # Shortcut: Ctrl + Alt + Shift + L

    "Timeline - Select Inside Preview"
    """Selects only the strips inside Timeline preview"""
    # Shortcut: Ctrl + Shift + A

    "Timeline - View Selected Context"
    """Alternative to View Selected (context view)"""
    # Shortcuts: End
    # Shortcut for MacOS: Fn + RightArrow

    "Timeline - Zoom In 10s"
    """Zooms in aproximatelly 10s of Timeline"""
    # Shortcuts: Shift + Home
    # Shortcut for MacOS: Fn + Ctrl + LeftArrow

    "Timeline - Zoom Out 10s"
    """Zooms out aproximatelly 10s of Timeline"""
    # Shortcuts: Shift + End; Ctrl + Shift + Right Mouse Click
    # Shortcut for MacOS: Fn + Ctrl + RightArrow; Ctrl + Shift + Right Mouse Click

    "Timeline - Zoom Out XY Axis"
    """Zooms out aproximatelly 10s of Timeline + Y Axis"""
    # Shortcuts: Ctrl + Shift + End
    # Shortcut for MacOS: Fn + Ctrl + Shift + RightArrow

    "Timeline - Zoom to Playhead"
    """Zooms timeline to playhead if it is over any strips"""
    # Shortcuts: Shift + Right Mouse Click
   
