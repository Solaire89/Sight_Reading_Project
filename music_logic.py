from constants import * # note_names_in_flat_keys, note_names_in_sharp_keys, DIFFICULTY_SETTINGS
from musicxml_node import generate_note, create_attributes
import random

# Takes an input starting_note and returns the scale associated with that root note
def generate_major_scale(starting_note: str) -> list[str]:
    flat_keys = ['C', 'F', 'Bb', 'Eb', 'Ab', 'Gb', 'Cb']
    sharp_keys = ['G', 'D', 'A', 'E', 'B']
    intervals = [2, 2, 1, 2, 2, 2, 1]
    if starting_note in flat_keys:
        notes = note_names_in_flat_keys
    elif starting_note in sharp_keys:
        notes = note_names_in_sharp_keys
    
    else:
        raise KeyError("Invalid scale name, please try again.")
    major_scale_index = []
    current_position_int = notes[starting_note]

    # Building the indices of the major scales
    for interval in intervals:
        major_scale_index.append(current_position_int)
        current_position_int += interval
        if current_position_int > 11:
            current_position_int %= 12
        
    
    major_scale_notes = []
    for note, i in notes.items():
        if i in major_scale_index:
            major_scale_notes.append(note)
    
    # Returns a list of the notes in the scale
    return major_scale_notes

# Returns a list of rhythms to be paired with notes
def generate_rhythm(difficulty: str) -> list[str]:
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
def get_valid_notes_in_range(starting_key: str, start_octave: int, difficulty: str) -> list[tuple[str, int]]:
    # Build list of (note, octave) tuples
    # Return valid_notes
    valid_notes = []
    scale = generate_major_scale(starting_key)
    starting_note = random.choice(scale)
    current_position_index = scale.index(starting_note)
    octave_range = DIFFICULTY_SETTINGS[difficulty]['range_octave']
    total_notes = DIFFICULTY_SETTINGS[difficulty]['total_notes']
    for octave in range(start_octave, start_octave + octave_range + 1):
        if octave == start_octave + octave_range and len(valid_notes) == total_notes - 1:
            valid_notes.append((scale[current_position_index], octave))
        if len(valid_notes) < total_notes:
            for note in scale[current_position_index:] + scale[:current_position_index]:
                if current_position_index == scale[current_position_index]:
                    valid_notes.append((scale[current_position_index], octave))
                elif current_position_index > len(scale):
                    current_position_index %= len(scale)
                else:
                    valid_notes.append((note, octave))
    return valid_notes

# Create a melody from the key provided (a string) with the number of notes provided
# Difficulty will determine all of the elements to be added to each sequence of notes
def create_melody(starting_note: str, difficulty: str):
    print(f"Current starting_note: {starting_note}")
    rhythms = generate_rhythm(difficulty)
    pool_of_notes = get_valid_notes_in_range(starting_note, 4, difficulty)
    print(f"Current pool of notes: {pool_of_notes}")

    note = []
    # num_notes = len(rhythms)
    first = True
    for rhythm in rhythms:
        # Rhythm object = 'whole', 'half', etc
        if first:
            note.append((starting_note, 4, rhythm))
            first = False
        else:
            note.append((random.choice(pool_of_notes), rhythm))
        print(f"current note: {note}")
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

print(create_melody('F', 'hard'))