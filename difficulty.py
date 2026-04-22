# Parameters: step, octave, duration, note_type, alter=None

def difficulty_parameters(difficulty):
    note_type = ["whole", "half", "quarter"]
    step = [1, 2, 3]
    rest = '<rest measure="yes"/>'
    if difficulty == "Easy":
        # Octave?
        divisions = 
        rest = None
    elif difficulty == "Medium":
        note_type.append("eighth")