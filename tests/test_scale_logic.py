from music_logic import generate_major_scale

def test():
    correct_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
    function_call_scale = generate_major_scale('C')
    print(f"Correct scale is {correct_scale}")
    print(f"Function call result: {function_call_scale}")

if __name__ == "__main__":
    test()