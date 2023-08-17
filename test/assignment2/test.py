import unittest
from src.assignment2.util import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        Record_input ={'harshith': [4.0, 5.0, 6.0], 'Anjitha': [7.0, 8.0, 9.0]}
        Student="Anjitha"
        output=8
        result=avg_marks(Record_input,Student)
        self.assertEqual(result, output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
