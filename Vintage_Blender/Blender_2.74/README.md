the Blender Velvets
===================

<BR>
![alt text](http://florestavermelha.files.wordpress.com/2014/02/velvet_goldmine_full.jpg "the Blender Velvets")
##### *<p align="center">Glamorous new functions for video editing in Blender VSE. To be used with lots of glitter.</p>*
<BR>

What are the Blender Velvets?
-----------------------------

The **Blender Velvets** are a series of Blender Addons (or plugins, if you prefer) for improving video editing with the VSE. They can be used separately or together, and at differet steps of video production. The velvets are:


###### ::velvet_revolver::

    ::velvet_revolver:: has been tested and works on Blender versions:
    2.74 (ffmpeg 2.7.1); 2.73a and 2.72b (ffmpeg 2.5.3); 2.71, 2.69.
    There is no reason why it should not work on versions between those.

The **::velvet_revolver::** is designed to make mass proxy generating an easy task for those lazy enough to open a terminal. It can create SD intra-frame (meaning 480p ProRes422 or MJPEG) proxies from all your videos using Blender's own interface. Just point it to a folder and dance to the radio for a while. In case you have multiple FPS in your footage, notoriously crappy to use in Blender, Revolver can also create full-Res copies of your sources, levelling everything to your chosen FPS. *Read the full documentation at [Velvet Revolver's webpage](http://blendervelvets.org/en/velvet-revolver/) (in English, Portuguese, Spanish and French).*

###### ::velvet_goldmine::

    ::velvet_goldmine:: has been tested and works on Blender versions:
    2.74, 2.73a, 2.72b, 2.71, 2.7, 2.69, 2.68a, 2.66b, 2.66a, 2.66 and 2.65.
    There is no reason why it should not work on versions between those.

The **::velvet_goldmine::** is a bunch of new functions and shortcuts aimed to fasten and loosen the overall hard VSE user interface. To be used with lots of glitter and with its companion, the *velvet_shortcuts*, for one can't dance alone, eh? *Read the full documentation at [Velvet Goldmine's webpage](http://blendervelvets.org/en/velvet-goldmine/) (in English, Portuguese, Spanish and French).*

###### ::blue_velvet::

    ::blue_velvet:: has been tested and works on Blender versions:
    2.74 (ffmpeg 2.7.1 and Ardour 4.1.0); 2.73a and 2.72b (ffmpeg 2.5.3 and Ardour 3.5.403); 2.69 (Ardour 3.2)
    There is no reason why it should not work on versions between those.

You can edit in Blender, but there's no way you will get decent audio out of it. The program was simply not made for DAW uses, so stop whining. What **::blue_velvet::** does is to get your finished timeline and export the audio cuts directly to Ardour, the correct program to deal with them. *Read the full documentation at [Blue Velvet's webpage](http://blendervelvets.org/en/blue-velvet/) (in English, Portuguese, Spanish and French).*

###### ::modified_space_sequencer::

    the modified space_sequencer has been tested and works on Blender versions:
    2.74, 2.73a, 2.72b, 2.72, 2.71, 2.70, 2.69, 2.68a, 2.66b, 2.66a, 2.66 and 2.65.
    There is no reason why it should not work on versions between those.

Blender has an original space_sequencer, which is the VSE user interface. It is loaded every time the program starts. The use of a modified version of this script brings up a number of controls that exist but are hidden, adds some new and useful info for when you are in the middle of a project and gathers the most relevant strip properties in the Viewer window instead the scattered Strip Properties Panel (this is especially good for color grading). *Read the full documentation at the [Modified Space Sequencer webpage](http://blendervelvets.org/en/space-sequencer/) (in English, Portuguese, Spanish and French).*


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
    # Shortcut:  Ctrl + Alt + P

    "Proxy Editing - Change to Full Resolution"
    """Change filepaths of current strips back to full-resolution files"""
    # Shortcut:  Ctrl + Shift + P


<BR>
::velvet_goldmine:: shortcuts cheatsheet
--------------------------------------------

#### Changes in the standard shortcuts (**velvet_shortcuts**)

Beyond adding the new functions/shortcuts, **velvet_shortcuts** also changes the current standard ones:

<b>"A"</b> now selects all strips;<BR>
<b>"Alt+A"</b> now deselects all strips;<BR>
<b>"Spacebar"</b> now plays the video (animation);<BR>
<b>"Shift+Alt+Spacebar"</b> now plays the video (animation) in reverse;<BR>
<b>"B"</b> - Border select selects what you want (the box) and discards the rest;<BR>
<b>"Alt+B"</b> - Border select adds what you want (the box) to current selected strips;<BR>
<b>"Del"</b> - Deletes without prompting for confirmation (in MacOS: fn + Del);<BR>
<b>"Ctrl+S"</b> - Saves the file without prompting for confirmation;<BR>
<b>"Shift+R"</b> - Refresh Sequencer (cleans cache in RAM);<BR>
<b>"Left Mouse Click"</b> - now selects strips with linked time by default (audio + video);<BR>
<b>"Left Mouse Click" on the timeline</b> - now selects all strips on the left/right of the cursor;<BR>
<b>"Ctrl+Left Mouse Click"</b> - selects strips disregarding linked time;<BR>
<b>"Ctrl+Right Mouse Click"</b> - view all (equivalent to "Home", without having to abandon the mouse);<BR>
<b>"Shift + Home"</b> - Zooms to selected strips (added for MacOS support; MacOS shortcut is Fn + Shift + LeftArrow);


#### New functions - the **::velvet_goldmine::** addon

    "Audio Pan Toggle"
    """Toggles audio pan between 0.0, 1.0 and -1.0 for selected strips"""
    # Shortcut: Ctrl + P
    
    "Audio - Show Waveform"
    """Shows the audio waveform in selected strips"""
    # Shortcut: W
    
    "Audio - Hide Waveform"
    """Hides the audio waveform in selected strips"""
    # Shortcut: Alt + W

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
    # Shortcut for MacOS: Fn + Delete

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

    "Render - Resolution Toggle"
    """Toggle between 30, 60 and 100 values in Resolution Percentage"""
    # Shortcut: Ctrl + Alt + Shift + R

    "Save Direct"
    """Saves current file without prompting for confirmation"""
    # Shortcut: Ctrl + S
    
    "Scene toggle"
    """Toggles between existing Scenes"""
    # Shortcuts: Shift + TAB
    # May not work on Mac

    "Screens - Change to Animation"
    """Changes view to selected screens"""
    # Shortcuts: Ctrl + Shift + F2 - Animation
    # Does not work on Mac

    "Screens - Change to Compositing"
    """Changes view to selected screens"""
    # Shortcuts: Ctrl + Shift + F3 - Compositing
    # Does not work on Mac

    "Screens - Change to Motion Tracking"
    """Changes view to selected screens"""
    # Shortcuts: Ctrl + Shift + F4 - Motion Tracking
    # Does not work on Mac

    "Screens - Change to Video Editing"
    """Changes view to selected screens"""
    # Shortcuts: Ctrl + Shift + F1 - Video Editing
    # Does not work on Mac

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

    "Strips - Concatenate Selected (Same channel)"
    """Concatenates selected strips in channel (only works for 1 channel)"""
    # Shortcut: Shift + C

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
    # Shortcut: Ctrl + Shift + A

    "Timeline - View Selected Context"
    """Alternative to View Selected (context view)"""
    # Shortcuts: End
    # Shortcut for MacOS: Fn + RightArrow

    "Timeline - Zoom In 10s"
    """Zooms in aproximatelly 10s of Timeline"""
    # Shortcuts: Ctrl + Home
    # Shortcut for MacOS: Fn + Ctrl + LeftArrow

    "Timeline - Zoom Out 10s"
    """Zooms out aproximatelly 10s of Timeline"""
    # Shortcuts: Ctrl + End; Ctrl + Shift + Right Mouse Click
    # Shortcut for MacOS: Fn + Ctrl + RightArrow; Ctrl + Shift + Right Mouse Click

    "Timeline - Zoom Out XY Axis"
    """Zooms out aproximatelly 10s of Timeline + Y Axis"""
    # Shortcuts: Ctrl + Shift + End
    # Shortcut for MacOS: Fn + Ctrl + Shift + RightArrow

    "Timeline - Zoom to Cursor"
    """Zooms timeline to green ibeam (cursor) if it is over any strips"""
    # Shortcuts: Shift + Right Mouse Click
   
