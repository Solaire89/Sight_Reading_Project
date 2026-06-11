from constants import musicxml_head, musicxml_footer
from music_logic import create_melody
from musicxml_node import *

def main():
    print("Welcome to the Site Reading Project!")
    
    attribute_of_song = create_attributes(16, -1, 4, 4, 'G', 2)
    measure_list = []
    note_list = []
    for measure in range(1, 5):
        melody_per_measure = create_melody('F', 'easy')
        for melody in melody_per_measure:
            note = generate_note(*melody)
            note_list.append(note)
        measure_form = create_measure(note_list, measure, attribute_of_song)
        attribute_of_song = None
        measure_list.append(measure_form)

    score = create_full_score(measure_list)
    with open("test.musicxml", "w") as f:
        f.write(score)

    return f

main()