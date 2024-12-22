boards = []
marker = dict()

nums = [int(a) for a in input().split(',')]
input()
s = ''

try:
    while not s:
        board = []
        # I use the marker to keep track of marked words in a dict
        # so I don't have to loop through the entire board
        marker = dict()
        while s := input():
            if s == '-':
                break
            row = []
            for a in s.split(' '):
                a = a.strip()
                if not a:
                    continue
                n = int(a)
                row.append(n)
            board.append(row)
        boards.append(board)
except EOFError:
    pass

m = len(boards[0])
n = len(boards[0][0])

def isWin(board: list[list[int]]) -> bool:
    # check rows
    for i in range(m):
        rowWin = True
        for j in range(n):
            if board[i][j] not in marker:
                rowWin = False
                break
        if rowWin:
            return True
    # check rows
    for j in range(n):
        colWin = True
        for i in range(m):
            if board[i][j] not in marker:
                colWin = False
                break
        if colWin:
            return True
    return False

def boardSum(board: list[list[int]]) -> int:
    unmarked = 0
    for i in range(m):
        for j in range(n):
            num = board[i][j]
            if num not in marker:
                unmarked += num
    return unmarked

skip = []

def bingo() -> int:
    for num in nums:
        marker[num] = True
        for i in range(len(boards)):
            if i in skip:
                continue
            board = boards[i]
            if isWin(board):
                if len(boards) - len(skip) == 1:
                    return boardSum(board) * num
                else:
                    skip.append(i)
    return 0

print(bingo())