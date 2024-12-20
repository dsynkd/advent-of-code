grid = []
try:
    while s := input():
        grid.append(s)
except:
    pass

class Solution:

    directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

    def __init__(self, grid):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])

    def dfs(self,i,j,k,di,dj) -> bool:
        if k == len(self.word):
            self.count += 1
            return True
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return False
        if self.grid[i][j] == self.word[k]:
            return self.dfs(i+di,j+dj,k+1,di,dj)
        else:
            return False
    
    def solve(self, word: str):
        self.word = word
        self.count = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == word[0]:
                    for d in self.directions:
                        self.dfs(i+d[0],j+d[1],1,d[0],d[1])

s = Solution(grid)
s.solve("XMAS")
print(s.count)