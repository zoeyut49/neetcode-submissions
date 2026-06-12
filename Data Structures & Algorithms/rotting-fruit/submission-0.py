class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        time = 0
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr in range(len(grid))
                    and nc in range(len(grid[0]))
                    and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append([nr, nc])
            time += 1
        
        return time if fresh == 0 else -1
