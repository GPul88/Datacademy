def square(number: float) -> float:
    return number * number

def test_square():
    correct_outputs = {
        -2: 4,
        -1: 1,
        0: 0,
        1: 1,
        2: 4
        }

    for input in correct_outputs:
        output = square(number=input)
        assert output == correct_outputs[input]

test_square()