from music_logic import generate_major_scale

def test():
    assert generate_major_scale('C') == ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

if __name__ == "__main__":
    test()