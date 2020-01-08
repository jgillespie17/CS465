from encode import encode

def test_encode_nothing():
   assert  encode("") == ""

def test_encode_two_characters():
    assert encode("ab") == "ab"

def test_encode_more_than_one():
    assert encode("aab") == "a2b"

def test_encode_more_than_one_case():
    assert encode("Aabb") == "Aab2"

def test_encode_multiple_letters():
    assert encode("AAaaBBbbCCccDDdd") == "A2a2B2b2C2c2D2d2"
