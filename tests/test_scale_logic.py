from music_logic import generate_major_scale

class TestClass:
    def test_correct_scale():
        c_scale = generate_major_scale('C')
        assert c_scale == ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    def test_return_error_letter():        
        i_scale = generate_major_scale('I')
        assert i_scale == "Invalid scale name, please try again."

    def test_return_error_number():
        number_scale = generate_major_scale('22')
        assert number_scale == "Invalid scale name, please try again."