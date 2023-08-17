from src.assignment1.util import *
if __name__ == '__main__':
    Number_of_command = int(input())
    commands = [input().split() for i in range(Number_of_command)]
    list_command(Number_of_command, commands)
