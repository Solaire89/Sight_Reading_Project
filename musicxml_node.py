from constants import musicxml_head, musicxml_footer

# If a note has a sharp or flat, this function will return either 1 (sharp) or -1 (flat)
def get_alter_value(note_name: str) -> int:
    if '#' in note_name:
        return 1
    elif 'b' in note_name:
        return -1
    else:
        return None


# Note contents: <pitch> (<step> and <octave> within pitch), alter (flat or sharp),
# duration (length of note in numbers), note type (quarter, half, whole, etc)
def generate_note(step: str, octave: int, alter, note_type: str, duration: int) -> str:
    pitch_step = f'''<note>
        <pitch>
        <step>{step[0]}</step>'''
    pitch_octave = f'''<octave>{octave}</octave>
        </pitch>'''
    if alter:
        note = pitch_step 
        + f"<alter>{alter}</alter>"
        + pitch_octave
    else:
        note = pitch_step + pitch_octave
    note += f'''<duration>{duration}</duration>
        <type>{note_type}</type>
        </note>'''
    return note

print(f"Generated note: {generate_note('B', 4, 0, 'whole', 16)}")

# This is the overall form of the music. Includes elements like key, clef, and time signature
def create_attributes(divisions: int, fifths: int, beats: int, beat_type: int, sign: str, clef_line: int) -> str:
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

