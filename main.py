from constants import musicxml_head, musicxml_footer
from music_logic import create_melody
from musicxml_node import *

def main():
    print("Welcome to the Sight Reading Project!")
    
    attribute_of_song = create_attributes(16, 5, 4, 4, 'G', 2)
    measure_list = []
    
    for measure_num in range(1, 17):
        note_list = []
        melody_per_measure = create_melody('B', 'easy')
        for note in melody_per_measure:
            note_xml = generate_note(*note)
            note_list.append(note_xml)
        measure_form = create_measure(note_list, measure_num, attribute_of_song)
        attribute_of_song = None
        measure_list.append(measure_form)

    score = create_full_score(measure_list)
    with open("test.musicxml", "w") as f:
        f.write(score)

    return f

main()