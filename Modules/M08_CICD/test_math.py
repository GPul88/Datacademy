def square(number: float) -> float:
    return number * number

def test_square():
    assert square(10) == 100, "10 squared should be 100"

class TestClass:
    def test_square10(self):
        assert square(10) == 100, "10 squared should be 100"

    def test_square20(self):
        assert square(20) == 400, "20 squared should be 400"