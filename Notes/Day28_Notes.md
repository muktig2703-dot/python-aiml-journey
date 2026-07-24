# Day 28 Notes - Unit Testing in Python
# Topics Covered
Unit Testing
`unittest` Module
Test Cases
Assertions
Running Tests
Student Age Checker Test Project

# 1. What is Unit Testing?
## Definition
Unit Testing is the process of testing individual parts (units) of a program to ensure they work correctly.
A unit can be:
A function
A method
A class
Instead of manually checking program output every time, unit tests automatically verify whether the code produces the expected results.
Unit testing is an important practice in professional software development because it helps identify bugs early and ensures code reliability.

# 2. Why is Unit Testing Important?
Unit testing provides several benefits:
Detects bugs early in development.
Ensures functions behave as expected.
Makes debugging easier.
Improves code reliability.
Makes future code changes safer.
Saves time by automating repetitive testing.
Most professional Python projects include automated unit tests.

# 3. The `unittest` Module
Python provides a built-in module called `unittest` for writing and running tests.
Import statement:
python
import unittest

No installation is required because it is included with Python.

# 4. Test Cases
A test case is a method that checks whether a function or program produces the expected output.
Example:
python
import unittest
class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(10 + 20, 30)
Each test method should begin with the word `test`.

# 5. Assertions
Assertions compare the expected result with the actual result.
Common assertions include:
### `assertEqual()`
Checks whether two values are equal.
python
self.assertEqual(5 + 5, 10)

### `assertTrue()`
Checks whether an expression is `True`.
python
self.assertTrue(age >= 18)

### `assertFalse()`
Checks whether an expression is `False`.
python
self.assertFalse(age < 18)
Assertions automatically report failures when results do not match expectations.

# 6. Running Tests
Tests are executed using:
python
if __name__ == "__main__":
    unittest.main()
Example Output:
text
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
OK
A dot (`.`) indicates that one test passed successfully.

# 7. Student Age Checker Test Project
Today's mini project tested the following function:
python
def is_adult(age):
    return age >= 18
The project verified two scenarios:
Adult (`True`)
Minor (`False`)
This demonstrated how unit tests can validate application logic automatically.

# 8. Advantages of Unit Testing
Improves software quality.
Finds bugs early.
Increases confidence while modifying code.
Makes maintenance easier.
Supports professional software development practices.
Reduces manual testing effort.

# 9. Keywords Learned Today
Unit Testing
`unittest`
Test Case
Assertion
`assertEqual()`
`assertTrue()`
`assertFalse()`
Test Runner
Automated Testing
Bug Detection