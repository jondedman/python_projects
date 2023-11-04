import unittest
from unittest import mock
from practice import calculate_area, temp_converter, string_combiner, calculator, even_or_odd, fibonacci

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

class TestCalculator(unittest.TestCase):

    def test_takes_user_input(self):
        # Test that the function takes user input.
        with unittest.mock.patch('builtins.input', side_effect=[1, 2, '+']):
            result = calculator()
        self.assertIsNotNone(result)

    def test_addition(self):
        # Test that the function correctly adds two numbers.
        with unittest.mock.patch('builtins.input', side_effect=[1, 2, '+']):
            result = calculator()
        self.assertEqual(result, 3)

    def test_subtraction(self):
        # Test that the function correctly subtracts two numbers.
        with unittest.mock.patch('builtins.input', side_effect=[1, 2, '-']):
            result = calculator()
        self.assertEqual(result, -1)

    def test_multiplication(self):
        # Test that the function correctly multiplies two numbers.
        with unittest.mock.patch('builtins.input', side_effect=[1, 2, '*']):
            result = calculator()
        self.assertEqual(result, 2)

    def test_division(self):
        # Test that the function correctly divides two numbers.
        with unittest.mock.patch('builtins.input', side_effect=[1, 2, '/']):
            result = calculator()
        self.assertEqual(result, 0.5)

class TestEvenOrOdd(unittest.TestCase):

    def test_even(self):
        # Test that the function correctly identifies an even number.
        num = 2
        result = even_or_odd(num)
        self.assertEqual(result, "even")

    def test_odd(self):
        # Test that the function correctly identifies an odd number.
        num = 3
        result = even_or_odd(num)
        self.assertEqual(result, "odd")

    def test_zero(self):
        # Test that the function correctly identifies zero.
        num = 0
        result = even_or_odd(num)
        self.assertEqual(result, "even")

    def test_negative_even(self):
        # Test that the function correctly identifies a negative even number.
        num = -2
        result = even_or_odd(num)
        self.assertEqual(result, "even")

    def test_negative_odd(self):
        # Test that the function correctly identifies a negative odd number.
        num = -3
        result = even_or_odd(num)
        self.assertEqual(result, "odd")

    def test_float_even(self):
        # Test that the function correctly identifies a float even number.
        num = 2.0
        result = even_or_odd(num)
        self.assertEqual(result, "even")

    def test_float_odd(self):
        # Test that the function correctly identifies a float odd number.
        num = 3.0
        result = even_or_odd(num)
        self.assertEqual(result, "odd")

    def test_string(self):
        # Test that the function correctly identifies a string as invalid input.
        num = "hello"
        result = even_or_odd(num)
        self.assertEqual(result, "Please enter a number")

class TestFibonacci(unittest.TestCase):

    def test_returns_something(self):
        # Test that the function returns something.
        num = 1
        result = fibonacci(num)
        self.assertIsNotNone(result)

    def test_zero(self):
        # Test that the function handles zero gracefully.
        num = 0
        result = fibonacci(num)
        self.assertEqual(result, [0])

    def test_one(self):
        # Test that the function handles one gracefully.
        num = 1
        result = fibonacci(num)
        self.assertEqual(result, [0, 1])

    def test_two(self):
        # Test that the function handles two gracefully.
        num = 2
        result = fibonacci(num)
        self.assertEqual(result, [0, 1, 1])

    def test_three(self):
        # Test that the function handles three gracefully.
        num = 3
        result = fibonacci(num)
        self.assertEqual(result, [0, 1, 1, 2])

    def test_four(self):
        # Test that the function handles four gracefully.
        num = 4
        result = fibonacci(num)
        self.assertEqual(result, [0, 1, 1, 2, 3])

    def test_five(self):
        # Test that the function handles five gracefully.
        num = 5
        result = fibonacci(num)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5])

    def test_six(self):
        # Test that the function handles six gracefully.
        num = 6
        result = fibonacci(num)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8])

    def test_seven(self):
        # Test that the function handles seven gracefully.
        num = 7
        result = fibonacci(num)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13])

    def test_eight(self):
        # Test that the function handles eight gracefully.
        num = 8
        result = fibonacci(num)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13, 21])

    def test_nine(self):
        # Test that the function handles nine gracefully.
        num = 9
        result = fibonacci(num)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_ten(self):
        # Test that the function handles ten gracefully.
        num = 10
        result = fibonacci(num)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])


















if __name__ == "__main__":
    unittest.main()
