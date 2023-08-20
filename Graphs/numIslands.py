from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS each island, mark it as a single island.
        # maintain a 2D list of booleans, marking explored gridboxes.
        # BFS until each island is explored. 
        explored = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        countIslands = 0
        for row in range(len(grid[0])):
            for col in range(len(grid)):
                if explored[col][row] is True:
                    pass
                elif grid[col][row] == "0":
                    explored[col][row] = True
                elif grid[col][row] == "1":
                    countIslands += 1
                    self.bfs(row, col, grid, explored)
        return countIslands
     
    def bfs(self, row: int, col: int, grid: List[List[str]], explored: List[List[bool]]):
        queue = []
        visited = set()
        queue.append((row,col))
        while len(queue) > 0 :
            row, col = queue.pop(0)
            if (row,col) in visited or grid[col][row] == "0":
                continue
            visited.add((row,col))
            explored[col][row] = True
            if row > 0: # Left bound
                queue.append((row-1,col))
            if row < len(grid[0]) - 1:
                queue.append((row+1,col))
            if col > 0:
                queue.append((row,col-1))
            if col < len(grid) - 1:
                queue.append((row,col+1))


islands = Solution().numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
print("Islands:", islands)