from constants import note_names_in_flat_keys, note_names_in_sharp_keys

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
    
    return major_scale_notes

# Note contents: <pitch> (<step> and <octave> within pitch), alter (flat or sharp),
# duration (length of note in numbers), note type (quarter, half, whole, etc)
def generate_note(note, octave, duration, note_type, alter=None):
    if alter == 1 or alter == -1:
        note = f'<note><pitch><step>{note}</step><alter>{alter}</alter><octave>{octave}</octave></pitch>'
    else:
        note = f'<note><pitch><step>{note}</step><octave>{octave}</octave></pitch>'
    note += f'<duration>{duration}</duration><type>{note_type}</type></note>'
    return note

print(generate_note('C', 4, 4, 'whole', 1))