from constants import musicxml_head, musicxml_footer

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
        note = f'<note>\n<pitch>\n<step>{step}</step>\n<alter>{alter}</alter>\n<octave>{octave}</octave>\n</pitch>'
    else:
        note = f'<note>\n<pitch>\n<step>{step}</step>\n<octave>{octave}</octave>\n</pitch>'
    note += f'\n<duration>{duration}</duration>\n<type>{note_type}</type>\n</note>'
    return note

# This is the overall form of the music. Includes elements like key, clef, and time signature
def create_attributes(divisions, fifths, beats, beat_type, sign, clef_line):
    return f'''<attributes>\n<divisions>{divisions}</divisions>
    <key>\n<fifths>{fifths}</fifths>\n</key>
    <time>\n<beats>{beats}</beats>\n<beat-type>{beat_type}</beat-type>\n</time>
    <clef>\n<sign>{sign}</sign>\n<line>{clef_line}</line>\n</clef>\n</attributes>'''


# Each measure needs to be wrapped by the measure tag. The first part of the piece requires the
# attributes section.
def create_measure(notes, measure_number, attributes=None):
    if attributes:
        measure = f'<measure number="{measure_number}">' + attributes + "\n".join(notes) + '</measure>'
    else:
        measure = f'<measure number="{measure_number}">{"\n".join(notes)}</measure>'
    return measure

def create_full_score(measures):
    # combine everything
    return musicxml_head + '<part id="P1">' + "\n".join(measures) + musicxml_footer

note1 = generate_note("C", 4, 4, "quarter")
note2 = generate_note("D", 4, 4, "quarter")
note3 = generate_note("E", 4, 4, "quarter")
note4 = generate_note("F", 4, 4, "quarter")
note5 = generate_note("B", 4, 4, "quarter")
note6 = generate_note("F", 4, 4, "quarter")
note7 = generate_note("G", 4, 4, "quarter")
note8 = generate_note("C", 5, 4, "quarter")

notes_list1 = [note1, note2, note3, note4]
notes_list2 = [note5, note6, note7, note8]
attrs = create_attributes(4, 0, 4, 4, "G", 2)

measure1 = create_measure(notes_list1, 1, attrs)
measure2 = create_measure(notes_list2, 2)

first_two_measures = [measure1, measure2]

score = create_full_score(first_two_measures)

with open("test.musicxml", "w") as f:
    f.write(score)