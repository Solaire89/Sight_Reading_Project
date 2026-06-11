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
    if alter is not None:
        note = f'''<note>
        <pitch>
        <step>{step}</step>
        <alter>{alter}</alter>
        <octave>{octave}</octave>
        </pitch>'''
    else:
        note = f'''<note>
        <pitch>
        <step>{step}</step>
        <octave>{octave}</octave>
        </pitch>'''
    note += f'''<duration>{duration}</duration>
        <type>{note_type}</type>
        </note>'''
    return note

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

# Test to generate a musicxml file
# note1 = generate_note("C", 4, 4, "quarter")
# note2 = generate_note("D", 4, 4, "quarter")
# note3 = generate_note("E", 4, 4, "quarter")
# note4 = generate_note("F", 4, 4, "quarter")
# note5 = generate_note("B", 4, 4, "quarter")
# note6 = generate_note("F", 4, 4, "quarter")
# note7 = generate_note("G", 4, 4, "quarter")
# note8 = generate_note("C", 5, 4, "quarter")

# notes_list1 = [note1, note2, note3, note4]
# notes_list2 = [note5, note6, note7, note8]
# attrs = create_attributes(4, 0, 4, 4, "G", 2)

# measure1 = create_measure(notes_list1, 1, attrs)
# measure2 = create_measure(notes_list2, 2)

# first_two_measures = [measure1, measure2]

# score = create_full_score(first_two_measures)