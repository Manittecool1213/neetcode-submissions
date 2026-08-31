class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque([])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            cur_i, cur_j = queue.popleft()
            for di, dj in DIRS:
                i, j = cur_i + di, cur_j + dj
                if 0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == 2 ** 31 - 1:
                    grid[i][j] = grid[cur_i][cur_j] + 1
                    queue.append((i, j))