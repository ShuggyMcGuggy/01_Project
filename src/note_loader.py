# Module to hold each of the tunes as strings
from mingus.midi import fluidsynth
import mingus.core.notes as notes
from mingus.core.value import dots, crotchet
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Track
from mingus.containers import Composition
from mingus.midi import midi_file_out

import music_this_is_my_commandment as timc

#fluidsynth.init("soundfont.SF2")
fluidsynth.init(r'/usr/local/Cellar/fluid-synth/2.2.3/share/fluid-synth/sf2/VintageDreamsWaves-v2.sf2')

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
    



