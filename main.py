from constants import musicxml_head, musicxml_footer
from music_logic import create_melody
from musicxml_node import *

def main():
    print("Welcome to the Site Reading Project!")
    melody_measure = create_melody('F', 'hard')
    for melody in melody_measure:
        note = generate_note(*melody)
    attribute_of_song = create_attributes(16, -1, 4, 4, 'G', 2)
    print(f"Attributes: {attribute_of_song}")
    measure_list = []
    for measure in range(0, 5):
        measure_list.append(create_measure(melody_measure, 1, attribute_of_song))
    print(f"Measure list: {measure_list}")
    # with open("test.musicxml", "w") as f:
    #     f.write(score)

main()