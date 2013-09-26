#import bpy

#for i in bpy.context.sequences:
#    if (i.type == "SOUND"):
#        print(i.channel, i.filepath, i.frame_duration, i.lock, i.mute, i.name, i.pan, i.pitch, i.select, i.sound, i.speed_factor, i.type, i.volume)

print("-------------------------------------------------------------")

from xml.etree.ElementTree import ElementTree, Element, SubElement
import xml.etree.ElementTree as etree
import bpy
import os


### VARIABLES
fileName = bpy.path.basename(bpy.data.filepath)
fileBasename = os.path.splitext(fileName)[0]

context = bpy.context 
system = context.user_preferences.system
scene = context.scene

audioSampleRate = int(system.audio_sample_rate.split("_")[1])
startFrame = scene.frame_start
endFrame = scene.frame_end
fps = scene.render.fps

desktop = os.environ['HOMEPATH'] + os.sep + "Desktop"
sourceAudiosFolder = desktop # change, must come from User choice


def samplesPerSec(fr, ar, fps):
    '''fr = duration in frames, ar = audio rate'''
    return int(fr * ar / fps)
    
ardourStart = startFrame - 1
ardourEnd = samplesPerSec((endFrame-1), audioSampleRate, fps)
idCounter = 0
    

xmlSections = [ "Config", "Metadata", "Sources", "Regions", "Locations", "Bundles",
             "Routes", "Playlists", "UnusedPlaylists", "RouteGroups", "Click",
             "Speakers", "TempoMap", "ControlProtocols", "Extra" ]


### XML BASE ATTRIBUTES
atSession = {'version': 3001,
             'name': fileBasename,
             'sample-rate': audioSampleRate,
             'id-counter': 0,
             'event-counter': 0
             }
                 
atOption = {'name': "audio-search-path",\
            'value': sourceAudiosFolder
            }

#atLocation = {'id': [0, 1, 2],
#              'name': ["Loop", "Punch", "session"], # Loop and Punch may not be necessary for base XML
#              'start': [0, 0, 0], # Start is 0 for everyone - timeline start = 0
#              'end': [24303908, 1, 24303908], # End is 1 for empty project (infinity) or end = endOfTimeline
#              'flags': ["IsAutoLoop,IsHidden", "IsAutoPunch,IsHidden", "IsSessionRange"],
#              'locked': ["no", "no", "no"],
#              'position-lock-style': ["AudioTime", "AudioTime", "AudioTime"]
#              }

atLocation = {'id': idCounter,
              'name': "session",
              'start': ardourStart, # Start is 0 - timeline start = 0
              'end': ardourEnd, # End is 1 for empty project (infinity) or end = endOfTimeline
              'flags': "IsSessionRange",
              'locked': "no",
              'position-lock-style': "AudioTime"
              }

atIO = {'name': "click",
        'id': idCounter,
        'direction': "Output",
        'default-type': "audio",
        'user-latency': 0,
        }
        
atPort = {'type': ["audio", "audio"],
          'name': ["click/audio_out 1", "click/audio_out 2"]
          }
          
atTempo = {'start': "1|1|0",
           'beats-per-minute': "120.000000",
           'note-type': "4.000000",
           'movable': "no"
           }
           
atMeter = {'start': "1|1|0",
           'note-type': "4.000000",
           'divisions-per-bar': "4.000000",
           'movable': "no"
           }

######## ------------------------------------

atSource = {'name': "lala.wav", # audio file with extension
            'type': "audio",
            'flags': "",
            'id': 41, # change id accordingly - this id influentiates atRegion in source-o and master-source-0
            'channel': 0, # ???????
            'origin': "lala.wav",} # audio file with extension - could be an absolute path

atRegion = {'name': "lala", # audio file, without extension
            'muted': 0, # 0 = not muted
            'opaque': 1,
            'locked': 0, # 0 = not locked
            'video-locked': 0, # 0 = not locked? should be locked to video?
            'automatic': 0,
            'whole-file': 1, # 1 = whole file? I'm using whole file for this test
            'import': 0,
            'external': 1, # 1 = not imported to ardour's assets folder?
            'sync-marked': 0,
            'left-of-split': 0,
            'right-of-split': 0,
            'hidden': 0, # 0 = not hidden
            'position-locked': 0, # 0 = not locked
            'valid-transients': 0,
            'start': 0, # position where audio starts in timeline? Mine starts at 0.
            'length': 24303909, # duration of file in samples (seconds * samplerate)
            'position': 0, # position where audio starts in timeline? Mine starts at 0.
            'sync-position': 0,
            'ancestral-start': 0, # can be audio-offset-start?
            'ancestral-length': 0,
            'stretch': 1,
            'shift': 1,
            'positional-lock-style': "AudioTime",
            'layering-index': 0,
            'envelope-active': 0, # envelope in Ardour is same as metastrip in Blender?
            'default-fade-in': 0,
            'default-fade-out': 0,
            'fade-in-active': 1,
            'fade-out-active': 1,
            'scale-amplitude': 1,
            'id': 43, # generic id
            'type': "audio",
            'first-edit': "nothing",
            'source-0': 41, # this is same id as atSource's id
            'master-source-0': 41, # this is same id as atSource's id
            'channels': 1 # mono file
            }

atRoute = {'id': 52, # generic id, BUT will be the referenced by atPlaylist
           'name': "boo_track_name", # track name (channel in Blender), boo_track_name
           'default-type': "audio",
           'active': "yes",
           'phase-invert': 0,
           'denormal-protection': "no",
           'meter-point': "MeterPostFader",
           'meter-type': "MeterPeak",
           'order-keys': "EditorSort=0:MixerSort=0",
           'self-solo': "no",
           'soloed-by-upstream': 0,
           'soloed-by-downstream': 0,
           'solo-isolated': "no",
           'solo-safe': "no",
           'monitoring': "",
           'saved-meter-point': "MeterPostFader",
           'mode': "Normal"
           }

atRouteIO = {'name': ["boo_track_name", "boo_track_name"], # track name (channel in Blender), boo_track_name
             'id': [69, 70], # generic id
             'direction': ["Input", "Output"],
             'default-type': ["audio", "audio"],
             'user-latency': [0, 0]
             }

atRouteIOPort = {'type': ["audio", "audio"],
                 'name': ["boo_track_name/audio_in 1", "boo_track_name/audio_out 1"] # track name (channel in Blender), boo_track_name
                 }

atDiskstream = {'flags': "Recordable",
                'playlist': "lala", # audio file, without extension
                'name': "lala", # audio file, without extension
                'id': 9, # generic id
                'speed': "1.000000",
                'capture-alignment': "Automatic",
                'channels': 1 # mono file
                }

atPlaylist = {'id': 80, # generic id
              'name': "lala", # audio file, without extension
              'type': "audio",
              'orig-track-id': 52, # generic id of atRoute!
              'frozen': "no",
              'combine-ops': 0
              }

# atPlaylistRegion seems to have the same attributes of atRegion, except for #name, #whole-file and #id (generic id)
atPlaylistRegion = {'name': "lala.1",
                    'muted': 0, # muted = 1 = muted; muted = 0 = not-muted
                    'opaque': 1,
                    'locked': 0, # locked = 1 = locked, locked = 0 = not-locked
                    'video-locked': 0,
                    'automatic': 0,
                    'whole-file': 0,
                    'import': 0,
                    'external': 1, # external probably refers to audio not in ardour's sources folders
                    'sync-marked': 0,
                    'left-of-split': 0,
                    'right-of-split': 0,
                    'hidden': 0,
                    'position-locked': 0,
                    'valid-transients': 0,
                    'start': 0, # = offset_start (onde, com relação à timeline, começa o arquivo de audio)
                    'length': 24303909, # = duração (considera alterações de offset start e offset end; é o quanto vemos realmente na timeline)
                    'position': 0, # é onde a visualização (bloco com onda sonora) começa na timeline
                    'sync-position': 0, # é onde começa a visualização da onda sonora, com relação ao áudio original (arquivo.wav)
                    'ancestral-start': 0,
                    'ancestral-length': 0,
                    'stretch': 1,
                    'shift': 1,
                    'positional-lock-style': "AudioTime",
                    'layering-index': 0,
                    'envelope-active': 0,
                    'default-fade-in': 0,
                    'default-fade-out': 0,
                    'fade-in-active': 1,
                    'fade-out-active': 1,
                    'scale-amplitude': 1,
                    'id': 87, # generic id
                    'type': "audio",
                    'first-edit': "nothing",
                    'source-0': 41, # this is same id as atSource's id
                    'master-source-0': 41, # this is same id as atSource's id
                    'channels': 1 # mono file
                    }


######## ------------------------------------

def createSubElements(el, att):
    for key, value in att.items():
        el.set(key, str(value))

def createSubElementsMulti(el, att, count):
    for key, value in att.items():
        el.set(key, str(value[count]))

def valLength(dic):
    '''Returns length of dictionary values'''
    return len(next(iter(dic.values())))



# XML root = Session
Session = Element("Session")
tree = ElementTree(Session)

# Create Session Elements + Attributes
for section in xmlSections:
    Session.append(Element(section))

# Create Option, IO, Tempo and Meter + Attributes
Option = SubElement(Session[0], "Option") # Session > Config > Option
Location = SubElement(Session[4], "Location")
IO = SubElement(Session[10], "IO") # Session > Click > IO
Tempo = SubElement(Session[12], "Tempo") # Session > TempoMap > Tempo
Meter = SubElement(Session[12], "Meter")# Session > TempoMap > Meter

createSubElements(Session, atSession)
createSubElements(Option, atOption)
createSubElements(Location, atLocation)
idCounter += 1
print(idCounter)
createSubElements(IO, atIO)
idCounter += 1
print(idCounter)
createSubElements(Tempo, atTempo)
createSubElements(Meter, atMeter)


# Create Location and Port + Attributes
#Location = ""
#for counter in range(valLength(atLocation)):
#    Location = SubElement(Session[4], "Location")  # Session > Location
#    createSubElementsMulti(Location, atLocation, counter)

Port = ""
for counter in range(valLength(atPort)):
    Port = SubElement(IO, "Port") # Session > Click > IO > Port
    createSubElementsMulti(Port, atPort, counter)








######## ------------------------------------
#xmlSections = [ "Config", "Metadata", "Sources", "Regions", "Locations", "Bundles",
#             "Routes", "Playlists", "UnusedPlaylists", "RouteGroups", "Click",
#             "Speakers", "TempoMap", "ControlProtocols", "Extra" ]

Source = SubElement(Session[2], "Source")
Region = SubElement(Session[3], "Region")
Route = SubElement(Session[6], "Route")

createSubElements(Source, atSource)
idCounter += 1
createSubElements(Region, atRegion)
idCounter += 1
createSubElements(Route, atRoute)
idCounter += 1

#RouteIO = ""
#for counter in range(valLength(atRouteIO)):
#    RouteIO = SubElement(Route, "IO")
#    createSubElementsMulti(RouteIO, atRouteIO, counter)
    
#RouteIOPort = ""
#for counter in range(valLength(atRouteIOPort)):
#    RouteIOPort = SubElement(RouteIO, "Port")
#    createSubElementsMulti(RouteIOPort, atRouteIOPort, counter)

RouteIO = ""
RouteIOPort = ""
for counter in range(valLength(atRouteIO)):
    RouteIO = SubElement(Route, "IO")
    RouteIOPort = SubElement(RouteIO, "Port")
    createSubElementsMulti(RouteIO, atRouteIO, counter)
    idCounter += 1
    createSubElementsMulti(RouteIOPort, atRouteIOPort, counter)


Diskstream = SubElement(Route, "Diskstream")
Playlist = SubElement(Session[7], "Playlist")
PlaylistRegion = SubElement(Playlist, "Region")

createSubElements(Diskstream, atDiskstream)
idCounter += 1
createSubElements(Playlist, atPlaylist)
idCounter += 1
createSubElements(PlaylistRegion, atPlaylistRegion)
idCounter += 1

####### ------------------------------------



# atLocation['flags'][0] = "IsAutoLoop,IsHidden"
# atLocation['flags'][1] = "IsAutoPunch,IsHidden"
# len(atLocation['flags']) = 3 - valor igual o de itens

#Location.set('name', "Loop")
#Location2.set('name', "Punch")

#Option.set('name', "audio-search-path")
#Option.set('value', os.environ['HOMEPATH'] + os.sep + "Desktop")

#print(Session.findall('Config'))
#print(Session.attrib)

#for child in Session:
#    print(child.tag, child.attrib)

#Extra = Element("Extra")
#Config = Element("Config") # Config
#Session.append(Config)

#root = Element("root")
#root.append(Element("one"))
#SubElement(config, "one")


Session.set('id-counter', str(idCounter))




#------------WRITE TO FILE-----------------------------------


from xml.dom.minidom import parseString

def identXML(element):
    return parseString(etree.tostring(element, "UTF-8")).toprettyxml(indent="  ")

outXML = desktop + os.sep + fileBasename + ".xml" # should be similar to #sourceAudiosFolder, get from UI
with open(outXML, 'w') as xmlFile:
    xmlFile.write(identXML(Session))

#os.environ['HOMEPATH'] + os.sep + "Desktop"
