from constants import note_names_in_flat_keys, note_names_in_sharp_keys
from musicxml_node import generate_note, create_attributes
import random

# Takes an input starting_note and returns the scale associated with that root note
def generate_major_scale(starting_note):
    intervals = [2, 2, 1, 2, 2, 2, 1]
    if starting_note in note_names_in_sharp_keys:
        scale = note_names_in_sharp_keys
    elif starting_note in note_names_in_flat_keys:
        scale = note_names_in_flat_keys
    
    else:
        return "Invalid scale name, please try again."
    major_scale_index = []

    current_position = scale[starting_note]

    # Building the indices of the major scales
    for interval in intervals:
        current_position += interval
        if current_position > 11:
            current_position %= 12
        major_scale_index.append(current_position)
    
    major_scale_notes = []
    for note, i in scale.items():
        if i in major_scale_index:
            major_scale_notes.append(note)
    
    # Returns a list of the notes in the scale
    return major_scale_notes


# Create a melody from the 
def create_melody(key, num_notes):
    scale = generate_major_scale(key)
    print(f"Scale: {scale}")
    for note in range(num_notes):
        next_note = random.choice(scale)
        print(f"Next note: {next_note}")

print(create_melody("Db", 10))