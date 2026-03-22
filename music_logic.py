from constants import keys_with_flats, keys_with_sharps

def generate_major_scale(starting_note):
    intervals = [2, 2, 1, 2, 2, 2, 1]
    try:
        if starting_note in keys_with_sharps:
            scale = keys_with_sharps
        elif starting_note in keys_with_flats:
            scale = keys_with_flats
    except ValueError:
        print("Scale name out of range, please try again.")
    major_scale = []

    current_position = scale[starting_note]
    for interval in intervals:
        current_position += interval
        if current_position > 11:
            current_position %= 12
        major_scale.append(current_position)
        # add it to scale
        # update current position
    
    return major_scale
