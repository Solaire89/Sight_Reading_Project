from constants import * # note_names_in_flat_keys, note_names_in_sharp_keys, DIFFICULTY_SETTINGS
from musicxml_node import generate_note, create_attributes
import random

# Takes an input starting_note and returns the scale associated with that root note
def generate_major_scale(starting_note):
    flat_keys = ['C', 'F', 'Bb', 'Eb', 'Ab', 'Gb', 'Cb']
    sharp_keys = ['G', 'D', 'A', 'E', 'B']
    intervals = [2, 2, 1, 2, 2, 2, 1]
    if starting_note in flat_keys:
        scale = note_names_in_flat_keys
    elif starting_note in sharp_keys:
        scale = note_names_in_sharp_keys
    
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

# Returns a list of rhythms to be paired with notes
def generate_rhythm(difficulty):
    possible_rhythms = DIFFICULTY_SETTINGS[difficulty]['rhythms']
    # 'rhythms': ['whole', 'half', 'quarter']
    remaining_duration = 16
    rhythm = []
    current_duration = 0
    available_rhythms = []
    
    while current_duration < remaining_duration:
        available_rhythms = list(filter(
            lambda x: RHYTHM_MAPPING[x]['duration'] <= remaining_duration, 
            possible_rhythms))
        current_rhythm = random.choice(available_rhythms)
        rhythm.append(current_rhythm)
        remaining_duration -= RHYTHM_MAPPING[current_rhythm]['duration']
    return rhythm

# Returns a list of tuples of notes to use in generating a melody (note, octave)
def get_valid_notes_in_range(scale, start_octave, difficulty):
    # build list of (note, octave) tuples
    # return valid_notes
    valid_notes = []
    num_octaves = DIFFICULTY_SETTINGS[difficulty]['range_octave']
    for octave in range(start_octave, start_octave + num_octaves + 1):
        if octave == start_octave + num_octaves:
            valid_notes.append((scale[0], octave))
        else:
            for note in scale:
                valid_notes.append((note, octave))
    return valid_notes

# Create a melody from the key provided (a string) with the number of notes provided
# Difficulty will determine all of the elements to be added to each sequence of notes
def create_melody(key, difficulty):
    # Making a list of note 
    rhythms = generate_rhythm(difficulty)
    scale = generate_major_scale(key)
    pool_of_notes = get_valid_notes_in_range(scale, 4, difficulty)
    print(f"Current pool of notes: {pool_of_notes}")
    pass
    # num_notes = len(rhythms)
    # settings = DIFFICULTY_SETTINGS[difficulty]
    # max_interval = settings['max_interval']
    # max_range = settings['range_octave']

    # # Make it so that if the number in octave changes, the semitones will be at least 12
    # # semitone_total = (octave difference * 12) + semitone
    # for rhythm in rhythms:
    #     # Rhythm object = 'whole', 'half', etc
        
        
    # for note in range(num_notes):
    #     next_note = generate_note(
    #         # Step
    #         random.choice(scale), 
    #         # Octave (need to be mindful of largest interval per difficulty)
    #         random.choice())
    #         # Duration
            # Note_type
            # Alter
        # generate note function signature:
        # generate_note(step, octave, duration, note_type, alter=None)

