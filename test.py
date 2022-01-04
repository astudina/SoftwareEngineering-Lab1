import converter


def run_test(input_data):
    output = []

    def _input(item):
        output.append(item)
        return input_data.pop(0)

    converter.input = _input
    converter.print = lambda item: output.append(item)
    converter.main()
    return output


def test_correct():
    output = run_test(['12 F'])
    assert output[0] == "Enter the temperature you want to convert (e.g. 12 F or 24 C): "
    assert output[1] == "The temperature in Celsius is -11 degrees."


def test_correct_2():
    output = run_test(['12345 C'])
    assert output[0] == "Enter the temperature you want to convert (e.g. 12 F or 24 C): "
    assert output[1] == "The temperature in Fahrenheit is 22253 degrees."


def test_incorrect_number_of_args():
    output = run_test(['12 F F'])
    assert output[0] == "Enter the temperature you want to convert (e.g. 12 F or 24 C): "
    assert output[1] == "You should write two arguments"


def test_incorrect_measurement_unit():
    output = run_test(['12 A'])
    assert output[0] == "Enter the temperature you want to convert (e.g. 12 F or 24 C): "
    assert output[1] == "Incorrect measurement unit"


def test_incorrect_input():
    output = run_test(['F F'])
    assert output[0] == "Enter the temperature you want to convert (e.g. 12 F or 24 C): "
    assert output[1] == "Incorrect input"


def test_incorrect_input_2():
    output = run_test(['12.5 F'])
    assert output[0] == "Enter the temperature you want to convert (e.g. 12 F or 24 C): "
    assert output[1] == "Incorrect input"
