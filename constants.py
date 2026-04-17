note_names_in_flat_keys = {
    'A': 0,
    'Bb': 1,
    'B': 2,
    'C': 3,
    'Db': 4,
    'D': 5,
    'Eb': 6,
    'E': 7,
    'F': 8,
    'Gb': 9,
    'G': 10,
    'Ab': 11
}

note_names_in_sharp_keys = {
    'A': 0,
    'A#': 1,
    'B': 2,
    'C': 3,
    'C#': 4,
    'D': 5,
    'D#': 6,
    'E': 7,
    'F': 8,
    'F#': 9,
    'G': 10,
    'G#': 11
}

fifths_keys_element = {
    'C': 0,
    'F': -1,
    'Bb': -2,
    'Eb': -3,
    'Ab': -4,
    'Db': -5,
    'Gb': -6,
    'B':  5,
    'E': 4,
    'A': 3,
    'D': 2,
    'G': 1
}

musicxml_head = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE score-partwise PUBLIC
   "-//Recordare//DTD MusicXML 4.0 Partwise//EN"
    "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
<part-list>
    <score-part id="P1">
      <part-name>Sight Reading Melody</part-name>
    </score-part>
</part-list>'''

musicxml_footer = '</part>\n</score-partwise>'