from url_shortener_backend.shortener import generate_code, ALPHABET


def test_generate_code_has_correct_length():
    assert len(generate_code(7)) == 7

def test_generate_code_uses_only_given_characters():
    code = generate_code(7)
    assert all(char in ALPHABET for char in code)

def test_generate_code_is_random():
    assert generate_code(7) != generate_code(7)