import unittest
from src.assignment1.util import *
class MyTestCase(unittest.TestCase):
    def test_list_command(self):
        Number_of_commands = 5
        commands = [['insert', '3', '2'], ['append', '5'], ['print']]
        output=[2,5]
        result, printed_result = list_command(Number_of_commands, commands)
        self.assertEqual(result, output)  # Check the modified list
        self.assertEqual(printed_result, [output])  # Check the printed list


if __name__ == '__main__':
    unittest.main()
