import unittest
from main import calculate_sum_and_average, get_numbers_from_user

class TestCalculateFunctions(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(calculate_sum_and_average([1, 2, 3]), (6, 2.0))

    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            calculate_sum_and_average([])
        self.assertEqual(str(context.exception), "Dãy số không được rỗng nha.")

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average([1, -2, 3])

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average(["a", "b", "c"])

    # Additional test for sum_two_numbers function
    def test_sum_two_numbers(self):
        from main import sum_two_numbers
        self.assertEqual(sum_two_numbers(2, 3), 5)
        self.assertEqual(sum_two_numbers(-1, 1), 0)
        self.assertEqual(sum_two_numbers(0, 0), 0)

    # Additional test for multiply_two_numbers function
    def test_multiply_two_numbers(self):
        from main import multiply_two_numbers
        self.assertEqual(multiply_two_numbers(2, 3), 6)
        self.assertEqual(multiply_two_numbers(-1, 1), -1)
        self.assertEqual(multiply_two_numbers(0, 5), 0)


if __name__ == '__main__':
    unittest.main()
