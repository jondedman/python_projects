import unittest
from practice import calculate_area, temp_converter, string_combiner

class Testarea(unittest.TestCase):

    def test_returns_something(self):
    # Test that the function returns something.
        length = 3
        width = 4
        calculated_area = calculate_area(length, width)
        self.assertIsNotNone(calculated_area)

    def test_no_dimensions(self):
    # Test that the function handles no dimensions gracefully.
        length = ""
        width = ""
        calculated_area = calculate_area(length, width)
        self.assertEqual(calculated_area, 0)

    def test_area_calculation(self):
        length = 3
        width = 4
        expected_area = 12
        calculated_area = (calculate_area(length, width))
        self.assertEqual(calculated_area, expected_area)

    def test_negative_dimensions(self):
    # Test that the function handles negative dimensions gracefully.
        length = -3
        width = 4
        calculated_area = calculate_area(length, width)
        self.assertEqual(calculated_area, 0)

    def test_zero_dimensions(self):
    # Test that the function handles zero dimensions gracefully.
        length = 0
        width = 4
        calculated_area = calculate_area(length, width)
        self.assertEqual(calculated_area, 0)

    def test_float_dimensions(self):
    # Test that the function handles float dimensions gracefully.
        length = 3.5
        width = 4.5
        calculated_area = calculate_area(length, width)
        self.assertEqual(calculated_area, 15.75)

    def test_string_dimensions(self):
    # Test that the function handles string dimensions gracefully.
        length = "3"
        width = "4"
        calculated_area = calculate_area(length, width)
        self.assertEqual(calculated_area, 12)

    def test_large_dimensions(self):
    # Test that the function handles large dimensions gracefully.
        length = 1000000
        width = 1000000
        calculated_area = calculate_area(length, width)
        self.assertEqual(calculated_area, 1000000000000)

    def test_square(self):
    # Test that the function handles square dimensions gracefully.
        length = 4
        width = 4
        calculated_area = calculate_area(length, width)
        self.assertEqual(calculated_area, 16)

class TestTempConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        # Test that the function correctly converts Celsius to Fahrenheit.
        temp = 0  # The freezing point of water in Celsius.
        type = "c"
        converted_temp = temp_converter(temp, type)
        self.assertEqual(converted_temp, '32.0 f')  # The freezing point of water in Fahrenheit.

    def test_fahrenheit_to_celsius(self):
        # Test that the function correctly converts Fahrenheit to Celsius.
        temp = 32
        type = "f"
        converted_temp = temp_converter(temp, type)
        self.assertEqual(converted_temp, '0.0 c')

    def test_no_temp(self):
        # Test that the function raises a ValueError when no temp is provided.
        temp = ""
        type = "c"
        with self.assertRaises(ValueError):
            temp_converter(temp, type)

    def test_no_type(self):
        # Test that the function raises a ValueError when no type is provided.
        temp = 0
        type = ""
        with self.assertRaises(ValueError):
            temp_converter(temp, type)

class TestStringCombiner(unittest.TestCase):

    def test_combines_strings(self):
        # Test that the function correctly combines two strings.
        a = "hello"
        b = "world"
        combined_string = string_combiner(a, b)
        self.assertEqual(combined_string, "helloworld")

    def test_combines_numbers(self):
        # Test that the function correctly combines two numbers.
        a = 1
        b = 2
        combined_string = string_combiner(a, b)
        self.assertEqual(combined_string, "12")

    def test_combines_string_and_number(self):
        # Test that the function correctly combines a string and a number.
        a = "hello"
        b = 2
        combined_string = string_combiner(a, b)
        self.assertEqual(combined_string, "hello2")

    def test_combines_number_and_string(self):
        # Test that the function correctly combines a number and a string.
        a = 1
        b = "world"
        combined_string = string_combiner(a, b)
        self.assertEqual(combined_string, "1world")












if __name__ == "__main__":
    unittest.main()
