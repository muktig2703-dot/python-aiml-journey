#Exercise 1
import unittest
class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(10 + 20, 30)
if __name__ == "__main__":
    unittest.main()

#Exercise 2
import unittest
def square(number):
    return number * number
class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(5), 25)
if __name__ == "__main__":
    unittest.main()

#Exercise 3
import unittest
def add(a, b):
    return a + b
class TestCalculator(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(5, 3), 8)
    def test_add_negative(self):
        self.assertEqual(add(-5, -3), -8)
    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)
if __name__ == "__main__":
    unittest.main()

#Student Ag Checker Test
import unittest
def is_adult(age):
    return age >= 18
class TestStudent(unittest.TestCase):
    def test_adult(self):
        self.assertTrue(is_adult(20))
    def test_minor(self):
        self.assertFalse(is_adult(15))
if __name__ == "__main__":
    unittest.main()