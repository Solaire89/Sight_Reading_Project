from constants import * # note_names_in_flat_keys, note_names_in_sharp_keys, DIFFICULTY_SETTINGS
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


# Create a melody from the key provided (a string) with the number of notes provided
# Difficulty will determine all of the elements to be added to each sequence of notes
'''def create_melody(key, num_notes, difficulty):
    scale = generate_major_scale(key)
    settings = DIFFICULTY_SETTINGS[difficulty]
    max_interval = settings['max_interval']
    duration = settings[]
    print(max_interval)
    for note in range(num_notes):
        next_note = generate_note(
            # Step
            random.choice(scale), 
            # Octave (need to be mindful of largest interval per difficulty)
            random.choice())'''
            # Duration
            # Note_type
            # Alter
        # generate note function signature:
        # generate_note(step, octave, duration, note_type, alter=None)

def generate_rhythm(difficulty):
    possible_rhythms = DIFFICULTY_SETTINGS[difficulty]['rhythms']
    # 'rhythms': ['whole', 'half', 'quarter']
    remaining_count = 16
    rhythm = []
    current_duration = 0
    available_rhythms = []
    for rhythm_value in possible_rhythms:
        available_rhythms.append(rhythm_value)
    # available_rhythms = list(filter(
    #     lambda x: RHYTHM_MAPPING[x]['duration'] <= remaining_count, 
    #     possible_rhythms))
    while current_duration < remaining_count:
        rhythm.append(random.choice(available_rhythms))
        remaining_count -= current_duration
    return rhythm

print(generate_rhythm('easy'))

