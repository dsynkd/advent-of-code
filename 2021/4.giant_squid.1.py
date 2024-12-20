boards = []

nums = [int(a) for a in input().split(',')]
input()

try:
    while True:
        board = []
        while s := input():
            board.append([int(a.strip()) for a in s.strip().split(' ')])
        boards.append(board)
        input()
except EOFError:
    pass

