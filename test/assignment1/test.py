import unittest
from src.assignment1.util import *
class MyTestCase(unittest.TestCase):
    def test_list_command(self):
        Number_of_commands = 3
        commands = [['insert', '3', '2'], ['append', '5'], ['print']]
        output=[2,5]
        result= list_command(Number_of_commands, commands)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
