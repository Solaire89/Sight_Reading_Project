from constants import musicxml_head, musicxml_footer

# If a note has a sharp or flat, this function will return either 1 (sharp) or -1 (flat)
def get_alter_value(note_name):
    if '#' in note_name:
        return 1
    elif 'b' in note_name:
        return -1
    else:
        return None


# Note contents: <pitch> (<step> and <octave> within pitch), alter (flat or sharp),
# duration (length of note in numbers), note type (quarter, half, whole, etc)
def generate_note(step, octave, alter, note_type, duration):
    pitch_step = f'''<note>
        <pitch>
        <step>{step[0]}</step>'''
    pitch_octave = f'''<octave>{octave}</octave>
        </pitch>'''
    if alter is not None:
        note = f"{pitch_step}" + f"<alter>{alter}</alter>" + pitch_octave
    else:
        note = pitch_step + pitch_octave
    note += f'''<duration>{duration}</duration>
        <type>{note_type}</type>
        </note>'''
    return note

print(generate_note('C#', 5, 1, 'quarter', 4))

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
        measure = f'<measure number="{measure_number}">' + attributes + "".join(notes) + '</measure>'
    else:
        measure = f'<measure number="{measure_number}">' + "".join(notes) + '</measure>'
    return measure

def create_full_score(measures):
    # combine everything
    return musicxml_head + '<part id="P1">' + "".join(measures) + musicxml_footer

