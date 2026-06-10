class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        land = 2147483647

        def bfs(r, c):
            seen = set()
            step = 0
            q = collections.deque()
            q.append((r, c, 0))

            while q:
                row, col, step = q.popleft()
                if grid[row][col] == 0:
                    return step
                for d in directions:
                    r = row + d[0]
                    c = col + d[1]
                    if (r in range(ROWS) and c in range(COLS) 
                    and grid[r][c] != -1
                    and (r, c) not in seen):
                        q.append((r, c, step + 1))
                        seen.add((r, c))
                step += 1
            return 2147483647

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == land:
                    grid[r][c] = bfs(r, c)