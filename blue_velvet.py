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

system = bpy.context.user_preferences.system
audioSampleRate = system.audio_sample_rate.split("_")[1]

desktop = os.environ['HOMEPATH'] + os.sep + "Desktop"

xmlSections = [ "Config", "Metadata", "Sources", "Regions", "Locations", "Bundles",
             "Routes", "Playlists", "UnusedPlaylists", "RouteGroups", "Click",
             "Speakers", "TempoMap", "ControlProtocols", "Extra" ]


### XML BASE ATTRIBUTES
atSession = {'version': 3001,
             'name': fileBasename,
             'sample-rate': audioSampleRate,
             'id-counter': 4,
             'event-counter': 0
             }
                 
atOption = {'name': "audio-search-path",\
            'value': desktop
            }

atLocation = {'id': [0, 1, 2],
              'name': ["Loop", "Punch", "session"],
              'start': [0, 0, 0],
              'end': [24303908, 1, 24303908],
              'flags': ["IsAutoLoop,IsHidden", "IsAutoPunch,IsHidden", "IsSessionRange"],
              'locked': ["no", "no", "no"],
              'position-lock-style': ["AudioTime", "AudioTime", "AudioTime"]
              }

atIO = {'name': "click",
        'id': 3,
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
IO = SubElement(Session[10], "IO") # Session > Click > IO
Tempo = SubElement(Session[12], "Tempo") # Session > TempoMap > Tempo
Meter = SubElement(Session[12], "Meter")# Session > TempoMap > Meter

createSubElements(Session, atSession)
createSubElements(Option, atOption)
createSubElements(IO, atIO)
createSubElements(Tempo, atTempo)
createSubElements(Meter, atMeter)


# Create Location and Port + Attributes
Location = ""
for counter in range(valLength(atLocation)):
    Location = SubElement(Session[4], "Location")  # Session > Location
    createSubElementsMulti(Location, atLocation, counter)

Port = ""
for counter in range(valLength(atPort)):
    Port = SubElement(IO, "Port") # Session > Click > IO > Port
    createSubElementsMulti(Port, atPort, counter)



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







#------------WRITE TO FILE-----------------------------------


from xml.dom.minidom import parseString

def identXML(element):
    return parseString(etree.tostring(element, "UTF-8")).toprettyxml(indent="  ")

outXML = desktop + os.sep + fileBasename + ".xml"
with open(outXML, 'w') as xmlFile:
    xmlFile.write(identXML(Session))

#os.environ['HOMEPATH'] + os.sep + "Desktop"
