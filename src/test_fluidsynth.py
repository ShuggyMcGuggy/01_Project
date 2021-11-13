"""
FluidSynth is a MIDI synthesizer which uses SoundFont (.SF2) files to
generate audio. To work with this module, you’ll need the FluidSynth
library (usually packaged with the stand-alone program) and a nice
instrument collection (look here: http://www.hammersound.net, go to
Sounds -> Soundfont Library -> Collections).
"""
#import sys
#sys.path.insert(0,r'/Users/markshury-smith/Development/PyCharmProjects/01_Project/venv/lib/python3.6/site-packages')

""" Refrences
https://programmerall.com/article/9815902917/  Tells how to set up the music

fluidsynth files in /usr/local/Cellar/fluid-synth/2.2.3
"""





print('got past sys')
from mingus.midi import fluidsynth
import mingus.core.notes as notes
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Track
from mingus.containers import Composition
from mingus.midi import midi_file_out

import music_this_is_my_commandment as timc
import note_loader as nl

import threading
import time

"""
Loading a SoundFont
To load the SoundFont and initialize FluidSynth we will only have to call init.
"""

#fluidsynth.init("soundfont.SF2")
fluidsynth.init(r'/usr/local/Cellar/fluid-synth/2.2.3/share/fluid-synth/sf2/VintageDreamsWaves-v2.sf2')

#fluidsynth.play_Note(Note("C-5"))
#fluidsynth.play_NoteContainer(NoteContainer(["C", "E"]))

"""
for i in range(5):
    print('play it')
    time.sleep(1)
    fluidsynth.play_NoteContainer(NoteContainer(["C", "E", "A"]))
    time.sleep(1)
    fluidsynth.play_Note(Note("G"))
"""
b = Bar()
l_bars = [b,b,b]
print(b.meter)
b.place_notes("A-4", 4)
b.place_notes("C-5", 4)
b.place_notes(["E-5", "G-5"], 2)

print(b)
fluidsynth.set_instrument(1, 24)


"""
for my_bar in l_bars:
    fluidsynth.play_Bar(my_bar, 1, 80)
"""

# Lets have a go at a tume
l_tune = ["F", "F", "Ab", "Gb", "F","F","F","F"]
l_note_bars = []
l_note_bars2 = []

l_note_bars.append([["F", 4], ["F", 4],["Ab", 4], ["Gb", 4]])
l_note_bars.append([["F", 2], ["F", 2]])
l_note_bars.append([["F", 4], ["F", 4],["Ab", 4], ["Gb", 4]])
l_note_bars.append([["F", 3], ["E", 8],["F", 4], ["Bb", 8],["Bb", 8]] )
l_note_bars.append([["Gb", 4], ["Gb", 8],["Gb", 8], ["Ab", 8], ["Ab", 4], ["Db", 8] ])
l_note_bars.append([["Eb", 4], ["Eb", 8],["Eb", 8],  ["F", 2] ])
l_note_bars.append([[None, 1]])
l_note_bars.append([["F", 4], ["F", 4],["Ab", 4], ["Gb", 4]])
l_note_bars.append([["F", 3], ["E", 8],["F", 2]] )
l_note_bars.append([["F", 4], ["F", 4],["Ab", 4], ["Gb", 4]])
l_note_bars.append([["F", 8], ["Eb", 8],["Db", 8], ["Eb", 8], ["F", 4], ["Ab", 8], ["Ab", 8]])
l_note_bars.append([["Gb", 4], ["Gb", 8],["Gb", 8], ["Ab", 3], ["Db", 8] ])
l_note_bars.append([["Eb", 4], ["Eb", 8], ["Eb", 8],["F", 2]] )

l_note_bars2.append([[None, 1]])
l_note_bars2.append([["F", 4], ["F", 4],["Ab", 4], ["Gb", 4]])
l_note_bars2.append([["F", 2], ["F", 2]])
l_note_bars2.append([["F", 4], ["F", 4],["Ab", 4], ["Gb", 4]])
l_note_bars2.append([["F", 8], ["Eb", 8],["F", 8], ["Gb", 8], ["F", 4], ["Ab", 8], ["Ab", 8]])
l_note_bars2.append([["Gb", 4], ["Gb", 8],["Gb", 8], ["Ab", 3], ["Ab", 8] ])
l_note_bars2.append([["Bb",3 ], ["Bb", 3],["Eb", 3]])
l_note_bars2.append([["Bb-3", 1]])                    

l_notes = []
l_bars = []


"""


# Iterate the list of not bars into a single track to be played

t = Track()

for a_bar in l_note_bars2:
    b_bar = Bar()
    for a_note in a_bar:
        b_bar.place_notes(a_note[0], a_note[1])
        print(b_bar)
    t.add_bar(b_bar)
    
fluidsynth.play_Track(t, channel=1, bpm=120)
"""

#*******************
my_track = nl.convert_l_notes_to_bars(timc.l_n_greater_love)
#fluidsynth.set_instrument(1, 24)
fluidsynth.set_instrument(1, 12)

fluidsynth.play_Track(my_track, channel=1, bpm=120)

b_play_again = True
while b_play_again == True:
    response = input("want to play again?")
    if "y" in response.lower():
        fluidsynth.play_Track(my_track, channel=1, bpm=120)
    else:
        b_play_again = False
midi_file_out.write_Track('this_is_my.mid', my_track)


    



