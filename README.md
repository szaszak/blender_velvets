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

    ::velvet_revolver:: has been developed over Blender 2.69, but it should work on previous versions.

The **::velvet_revolver::** is designed to make mass proxy generating an easy task for those lazy enough to open a terminal. It can create SD intra-frame (meaning 480p ProRes422 or MJPEG) proxies from all your videos using Blender's own interface. Just point it to a folder and dance to the radio for a while. In case you have multiple FPSs in your footage, notoriously crappy to use in Blender, Revolver can also create full-Res copies of your sources, levelling everything to your chosen FPS. *Get your fix twice: during the preparation for video editing and at the end, before color grading or final rendering.*

###### ::velvet_goldmine::

    ::velvet_goldmine:: has been tested and works on Blender versions: 2.69, 2.68a, 2.66b, 2.66a, 
    2.66 and 2.65. There is no reason why it should not work on versions between those.

The **::velvet_goldmine::** is a bunch of new functions and shortcuts aimed to fasten and loosen the overall hard VSE user interface. To be used with lots of glitter and with its companion, the *velvet_shortcuts*, for one can't dance alone, eh? *Get your fix during the video editing phase*.

###### ::blue_velvet::

    ::blue_velvet:: has been developed over Blender 2.69, but it should work on previous versions.

You can edit in Blender, but there's no way you will get decent audio out of it. The program was simply not made for DAW uses, so stop whining. What **::blue_velvet::** does is to get your finished timeline and export the audio cuts directly to Ardour, the correct program to deal with them. *Get your fix when your video is ready for blasting the audio to maximum volume.*

###### ::modified_space_sequencer::

    the modified space_sequencer has been tested and works on Blender versions: 2.69, 2.68a, 2.66b, 
    2.66a, 2.66 and 2.65. There is no reason why it should not work on versions between those.

Blender has an original space_sequencer, which is the VSE user interface. It is loaded every time the program starts. The use of a modified version of this script brings up a number of controls that exist but are hidden, adds some new and useful info for when you are in the middle of a project and gathers the most relevant strip properties in the Viewer window instead the scattered Strip Properties Panel (this is especially good for color grading). *Get your fix everytime.*


<BR>
General install instructions
----------------------------

Go to https://github.com/szaszak/blender_velvets/ and click on the "Downlod ZIP" icon (it is the same as [clicking on this link] (https://github.com/szaszak/blender_velvets/archive/master.zip)). You will download a folder called "blender_velvets-master" - all the Blender Velvets addons will be inside it. Then, follow the specific instructions for each plugin below.

| The easiest way to properly configure Blender for video editing and install <BR>the Blender Velvets is by following [this screenshot-by-screenshot guide] (https://szaszak.wordpress.com/linux/blender-como-editor-de-video/). |
|:------------:|


<BR>
Detailed description for ::velvet_revolver::
--------------------------------------------

### TODO.


<BR>
Detailed description for ::velvet_goldmine::
--------------------------------------------

#### To install **::velvet_goldmine::** with the shortcuts:

Open Blender and go to: *File > User Preferences > Addons tab > Install from file > Choose velvet_goldmine.py.* The addon **::velvet_goldmine::** will show up in the list - enable it by clicking on the small box to the right.

To import the set of suggested shortcuts (that also change some of the standard hotkeys), go to: *File > User Preferences > Input tab > Import Key Configuration > Choose velvet_shortcuts.py.* You're done: it will show up in the list and will already be your current shortcut set.


#### Changes in the standard shortcuts (**velvet_shortcuts**)

Beyond adding the new functions/shortcuts, **velvet_shortcuts** also changes the current standard ones:

<b>"A"</b> now selects all strips;<BR>
<b>"Alt+A"</b> now deselects all strips;<BR>
<b>"Spacebar"</b> now plays the video (animation);<BR>
<b>"B"</b> - Border select selects what you want (the box) and discards the rest;<BR>
<b>"Alt+B"</b> - Border select adds what you want (the box) to current selected strips;<BR>
<b>"Del"</b> - Delects without prompting for confirmation;<BR>
<b>"G"</b> - Makes meta-strip without prompting for confirmation;<BR>
<b>"Ctrl+S"</b> - Saves the file without prompting for confirmation;<BR>
<b>"Shift+R"</b> - Refresh Sequencer (cleans cache in RAM);<BR>
<b>"Left Mouse Click"</b> - now selects strips with linked time by default (audio + video);<BR>
<b>"Ctrl+Left Mouse Click"</b> - selects strips disregarding linked time;<BR>
<b>"Ctrl+Right Mouse Click"</b> - view all (equivalent to "Home", without having to abandon the mouse);


#### New functions - the **::velvet_goldmine::** addon

The functions' names and descriptions below should help you understand what they do until I have
time to make a better documentation. If you want a visual but initial documentation on video,
see this link: http://florestavermelha.org/2013/02/28/blender-novas-funcoes-o-video-explicativo/

Highlights go to markers improved controls (easy removal of closest) and navigation; easier audio
control (waveform and panning) and elimination of the need for a "Timeline" window because all
the timeline can now be controlled directly from the VSE window via shortcuts.

It must be said that <b>::velvet_goldmine::</b> normally sets frame_start and frame_preview_start together,
because in almost all the cases, that's what an editor really want - to render the range he has set
for his timeline. Otherwise, it would be a bit confusing.

Observation: Panning audio in Blender only works with mono sources, be warned.


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
    

<BR>
Detailed description for the modified space_sequencer
-----------------------------------------------------

<BR>
<p align="center"><a href="http://florestavermelha.files.wordpress.com/2013/12/projeto_edicao_making_of.jpg" target="_blank"><img src="http://florestavermelha.files.wordpress.com/2013/12/projeto_edicao_making_of.jpg?w=470" alt="projeto_edicao_making_of" width="470" height="263" class="aligncenter size-large wp-image-2032" /></a></p>

To use the modified VSE interface, go to your *\scripts\startup\bl_ui*, that can be found searching the directories of your Blender installation, and replace the **space_sequencer.py** there by the one that comes with the Blender Velvets. It may be wise to create a backup of the original before doing so (Ctrl+C and Ctrl+V will do the job).

The space sequencer modifications aimed at completely eliminating Blender's "Timeline" window, because it just gets messy and redundant when you're using the program for video editing. Everything on its interface that is useful has been copied to the VSE window (the actual timeline); all the relevant controls are now to be accessed via the **::velvet_goldmine::** addon shortcuts.

There is new information displayed on the VSE Main and Viewer windows, related to the project render and FPS settings. It is also easy to check now the duration of strips or of the whole project's timeline in human-readable SMTPE, instead of Blender's original framecount.

The most useful strips properties are now gathered on the VSE Viewer Properties Panel. Click on a strip in your timeline and look at the Viewer to check this out. This way it seems easier to find everything instead of having to search for scattered information hidden in unthinkable places.


<BR>
Detailed description for ::blue_velvet::
----------------------------------------

### TODO.

<p align="center"><a href="http://florestavermelha.files.wordpress.com/2013/12/projeto_edicao_making_of_para_ardour.jpg" target="_blank"><img src="http://florestavermelha.files.wordpress.com/2013/12/projeto_edicao_making_of_para_ardour.jpg?w=470" alt="projeto_edicao_making_of_para_ardour" width="470" height="264" class="aligncenter size-large wp-image-2031" /></a></p>
<p align="center"><a href="http://florestavermelha.files.wordpress.com/2013/12/projeto_edicao_making_of_no_ardour.jpg" target="_blank"><img src="http://florestavermelha.files.wordpress.com/2013/12/projeto_edicao_making_of_no_ardour.jpg?w=470" alt="projeto_edicao_making_of_no_ardour" width="470" height="264" class="aligncenter size-large wp-image-2033" /></a></p>
