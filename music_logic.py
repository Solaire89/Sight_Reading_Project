from constants import * # note_names_in_flat_keys, note_names_in_sharp_keys, DIFFICULTY_SETTINGS
from musicxml_node import get_alter_value
from typing import Optional
import random


# Takes an input starting_note and returns the scale associated with that root note
def generate_major_scale(starting_note):
    flat_keys = ['C', 'F', 'Bb', 'Eb', 'Ab', 'Gb']
    sharp_keys = ['G', 'D', 'A', 'E', 'B']
    intervals = [2, 2, 1, 2, 2, 2, 1]
    if starting_note in flat_keys:
        notes = note_names_in_flat_keys
    elif starting_note in sharp_keys:
        notes = note_names_in_sharp_keys
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

# Returns a list of tuples of rhythms and durations to be paired with notes
def generate_rhythm(difficulty):
    possible_rhythms = DIFFICULTY_SETTINGS[difficulty]['rhythms']
    # 'rhythms': ['whole', 'half', 'quarter']
    duration = []
    for rhythm in possible_rhythms:
        duration.append((rhythm, RHYTHM_DURATION[rhythm]))
    remaining_duration = 16
    rhythm = []
    current_duration = 0
    available_rhythms = []
    
    while current_duration < remaining_duration:
        available_rhythms = list(filter(
            lambda x: RHYTHM_MAPPING[x]['duration'] <= remaining_duration, 
            possible_rhythms)
            )
        current_rhythm = random.choice(available_rhythms)
        rhythm.append((current_rhythm, RHYTHM_DURATION[current_rhythm]))
        remaining_duration -= RHYTHM_MAPPING[current_rhythm]['duration']
    return rhythm

# Returns a list of tuples of notes to use in generating a melody (note, octave)
def get_valid_notes_in_range(starting_key, start_octave, difficulty):
    # Build list of (note, octave) tuples
    # Return valid_notes
    valid_notes = []
    scale = generate_major_scale(starting_key)
    print(f"Current key: {scale}")
    starting_note = random.choice(scale)
    print(f"Starting note: {starting_note}")
    current_position_index = scale.index(starting_note)
    
    octave_range = DIFFICULTY_SETTINGS[difficulty]['range_octave']
    total_notes = DIFFICULTY_SETTINGS[difficulty]['total_notes']
    for octave in range(start_octave, start_octave + octave_range + 1):
        for note in scale:
            if current_position_index > len(scale):
                current_position_index %= len(scale)
            if 'C' in note:
                octave += 1
            print(f"Note: {note}")
            valid_notes.append((note, octave, get_alter_value(note)))
            if len(valid_notes) == total_notes:
                break
    return valid_notes


print(f"Note pool: {get_valid_notes_in_range('Bb', 4, 'hard')}")
# Create a melody from the key provided (a string) with the number of notes provided
# Difficulty will determine all of the elements to be added to each sequence of notes
def create_melody(starting_note, difficulty):
    rhythms = generate_rhythm(difficulty)
    pool_of_notes = get_valid_notes_in_range(starting_note, 4, difficulty)
    note_list = []
    for rhythm in rhythms:
        note = random.choice(pool_of_notes)
        print(f"Current note: {note}")
        current_note = (*note, *rhythm)
        note_list.append(current_note)
    return note_list
        # generate_note(step, octave, alter, note_type, duration)
