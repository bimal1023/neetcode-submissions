from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        queue=deque()
        found_first_island=False

        # DFS to isolate the island
        def dfs(r,c):
            grid[r][c]=2
            queue.append((r,c))
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    dfs(nr,nc)

        for r in range(rows):
            if found_first_island:
                break
            for c in range(cols):
                if grid[r][c]==1:
                    dfs(r,c)
                    found_first_island=True
                    break
            distance=0
            while queue:
                for _ in range(len(queue)):
                    r,c =queue.popleft()
                    for dr, dc in directions:
                        nr=r+dr
                        nc=c+dc
                        if 0<=nr<rows and 0<=nc<cols:
                            if grid[nr][nc]==1:
                                return distance
                            if grid[nr][nc]==0:
                                grid[nr][nc]=2
                                queue.append((nr,nc))
                distance+=1
        return distance