from constants import musicxml_head

def get_alter_value(note_name):
    if '#' in note_name:
        return 1
    elif 'b' in note_name:
        return -1
    return None

print(get_alter_value('Dx'))