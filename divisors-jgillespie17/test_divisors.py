from divisors import divisors

def test_one():
    assert divisors(1) == [1]

def test_two():
    assert divisors(2) == [1, 2]

def test_three():
    assert divisors(3) == [1, 3]

def test_four():
    assert divisors(4) == [1, 2, 4]

def test_five():
    assert divisors(5) == [1, 5]

def test_six():
    assert divisors(6) == [1, 2, 3, 6]

def test_seven():
    assert divisors(7) == [1, 7]

def test_eight():
    assert divisors(8) == [1, 2, 4, 8]

def test_nine():
    assert divisors(9) == [1, 3, 9]

def test_ten():
    assert divisors(10) == [1, 2, 5, 10]

def test_one_hundred():
    assert divisors(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]

def test_two_hundred():
    assert divisors(200) == [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 200]

def test_prime_seventeen():
    assert divisors(17) == [1, 17]

def test_prime_two_hundred_eight_one():
    assert divisors(281) == [1, 281]
