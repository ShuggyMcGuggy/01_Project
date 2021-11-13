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

#fluidsynth.init("soundfont.SF2")
fluidsynth.init(r'/usr/local/Cellar/fluid-synth/2.2.3/share/fluid-synth/sf2/VintageDreamsWaves-v2.sf2')

dot_crotchet=value.dots(value.crotchet)

l_n_greater_love = [["F", 4], ["F", 4],["Ab", 4], ["Gb", 4],
                  ["F", 2], ["F", 2],
                  ["F", 4], ["F", 4],["Ab", 4], ["Gb", 4],
                  ["F", value.dots(value.crotchet)],  ["E", 8],["F", 4], ["Bb", 8],["Bb", 8],
                  ["Gb", 4], ["Gb", 8],["Gb", 8], ["Ab", 8], ["Ab", 4], ["Db", 8],
                  ["Eb", 4], ["Eb", 8],["Eb", 8],  ["F", 2],
                  [None, 1],
                  ["F", 4], ["F", 4],["Ab", 4], ["Gb", 4],
                  ["F", value.dots(value.crotchet)], ["E", 8],["F", 2],
                  ["F", 4], ["F", 4],["Ab", 4], ["Gb", 4],
                  ["F", 8], ["Eb", 8],["Db", 8], ["Eb", 8], ["F", 4], ["Ab", 8], ["Ab", 8],
                  ["Gb", 4], ["Gb", 8],["Gb", 8], ["Ab", dot_crotchet], ["Db", 8],
                  ["Eb", 4], ["Eb", 8], ["Eb", 8],["F", 2],
                    [None, 1],
                    ["F", 4], ["F", 4],["Ab", 4], ["Gb", 4],
                    ["F", 2], ["F", 2],
                    ["F", 4], ["F", 4],["Ab", 4], ["Gb", 4],
                    ["F", 8], ["Eb", 8],["F", 8], ["Gb", 8], ["F", 4], ["Ab", 8], ["Ab", 8],
                    ["Gb", 4], ["Gb", 8],["Gb", 8], ["Ab", dot_crotchet], ["Ab", 8],
                    ["Bb",3 ], ["Bb", 3],["Eb", 3],
                    ["Bb-3", 1]
                ]
# ****************************
def convert_l_notes_to_bars(l_notes):
    """ Take a list of [Notes] and seperate them into bars
    use the place notes to fill a bar
    once the bar is full sabe the list of notes as a list in a
    list of list of notes fro each bar
    Then retunr the track
    """
    my_track = Track()
    l_l_notes_in_bar = []
    l_notes_in_bar = []
    b = Bar()
    for note in l_notes:
        cuml_duration = float(0.0) 
        
        if b.place_notes(note[0], note[1]) == False:
            print(' Cannot add the note to bar: ' + note[0])
            b
            
        else:
            print("Adding notes to the bar")
            print(note)
            l_notes_in_bar.append([note[0], note[1]])
            
        if b.current_beat == float(1):
            print("the bar is full: save to list and empty bar")
            print(l_notes_in_bar)
            l_l_notes_in_bar.append(l_notes_in_bar)
            l_notes_in_bar = []
            b = Bar()
        
            
    print("the fill list of bars is:")
    print(l_l_notes_in_bar)

    my_track = convert_l_l_notes_in_bar_to_track(l_l_notes_in_bar)
    return my_track  

# **********************
def convert_l_l_notes_in_bar_to_track(l_l_notes_in_bar):
    """ converst a list of lists of notes, split into bars of list of notes
    and convert them into a track.
    return the track
    """
    t = Track()
    for a_bar in l_l_notes_in_bar:
        print("the bar is:")
        print(a_bar)
        b_bar = Bar()
        for a_note in a_bar:
            print("The note is :")
            print(a_note)
            b_bar.place_notes(a_note[0], a_note[1])
            print(b_bar)
        t.add_bar(b_bar)

    return t
    
"""        
my_track = convert_l_notes_to_bars(l_n_greater_love)
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
"""
