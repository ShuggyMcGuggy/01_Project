# Module to hold each of the tunes as strings
from mingus.midi import fluidsynth
import mingus.core.notes as notes
import mingus.core.value as value
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Track
from mingus.containers import Composition
from mingus.midi import midi_file_out



from src.note_loader import convert_l_notes_to_bars
from src.note_loader import convert_l_l_notes_in_bar_to_track

#fluidsynth.init("soundfont.SF2")
fluidsynth.init(r'/usr/local/Cellar/fluid-synth/2.2.3/share/fluid-synth/sf2/VintageDreamsWaves-v2.sf2')


dot_crotchet = value.dots(value.crotchet)
dot_minim = value.dots(value.minim)

# *******
# Have a lplay with the lilipond output
l_n_for_the_fallen = [["D",value.dots(value.crotchet)], ["D",8], ["D",4],["D",4],
                      ["G", dot_minim], ["G", 4],
                      ["F#",2], ["E", 4], ["D", 4],
                      ["C#", 2], ["A-3", 2],
                      ["B-3", dot_minim], [None, 4],
                      ["B-3", 2], ["B-3", 4],["B-3", 4],
                      ["B", value.dots(value.crotchet)], ["B", 8], ["B",2],
                      ["B", value.dots(value.crotchet)], ["B", 8], ["A",4],["A",4],
                      ["G",2],["F#",2],
                      ["E", dot_minim], ["E",4],
                      ["A",2],["G",2],
                      ["F#",2], ["E",4],["E",4],
                      ["D",2],["C#",2],
                      ["B-3",2], ["E",4],["E",4],
                      ["G",2],["G",2],
                      ["F#",2],["D",4],["C#",4],
                      ["B-3",value.dots(value.crotchet)],["B-3",8], ["B-3",2],
                      ["A-3",2],["A-3",4],["A-3",4],
                      ["A-3",2],["A-3",2],
                      ["D-3",1]
                      ]
                        
print(l_n_for_the_fallen)
new_track = convert_l_notes_to_bars(l_n_for_the_fallen)

fluidsynth.set_instrument(1, 12)
fluidsynth.play_Track(new_track, channel=1, bpm=120)
