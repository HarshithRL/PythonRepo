from src.assignment1.util import *
if __name__ == '__main__':
    N = int(input())
    commands = [input().split() for i in range(N)]
    list_command(N, commands)