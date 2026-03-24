from constants import keys_with_flats, keys_with_sharps

def generate_major_scale(starting_note):
    intervals = [2, 2, 1, 2, 2, 2, 1]
    if starting_note in keys_with_sharps:
        scale = keys_with_sharps
    elif starting_note in keys_with_flats:
        scale = keys_with_flats
    
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

print(generate_major_scale('Db'))