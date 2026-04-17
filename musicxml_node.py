from constants import musicxml_head

def get_alter_value(note_name):
    if '#' in note_name:
        return 1
    elif 'b' in note_name:
        return -1
    return None

# Note contents: <pitch> (<step> and <octave> within pitch), alter (flat or sharp),
# duration (length of note in numbers), note type (quarter, half, whole, etc)
def generate_note(step, octave, duration, note_type, alter=None):
    if alter is not None:
        note = f'<note><pitch><step>{step}</step><alter>{alter}</alter><octave>{octave}</octave></pitch>'
    else:
        note = f'<note><pitch><step>{step}</step><octave>{octave}</octave></pitch>'
    note += f'<duration>{duration}</duration><type>{note_type}</type></note>'
    return note

# This is the overall form of the music. Includes elements like key, clef, and time signature
def create_attributes(divisions, fifths, beats, beat_type, sign, clef_line):
    return f'''<attributes><divisions>{divisions}</divisions>
    <key><fifths>{fifths}</fifths></key>
    <time><beats>{beats}</beats><beat-type>{beat_type}</beat-type></time>
    <clef><sign>{sign}</sign><line>{clef_line}</line></clef></attributes>'''


# Each measure needs to be wrapped by the measure tag. The first part of the piece requires the
# attributes section.
def create_measure(notes, measure_number, attributes=None):
    if attributes:
        measure = f'<measure number="{measure_number}">' + attributes + "\n".join(notes) + '</measure>'
    else:
        measure = f'<measure number="{measure_number}">{"\n".join(notes)}</measure>'
    return measure



note1 = generate_note("C", 4, 4, "quarter")
note2 = generate_note("D", 4, 4, "quarter")
note3 = generate_note("E", 4, 4, "quarter")
note4 = generate_note("F", 4, 4, "quarter")

notes_list = [note1, note2, note3, note4]
attrs = create_attributes(4, 0, 4, 4, "G", 2)

print(create_measure(notes_list, 1, attrs))