class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        max_area=0

        def dfs(r,c):
            if r<0 or r>=rows:
                return 0
            elif c<0 or c>=cols:
                return 0
            elif (r,c) in visited:
                return 0
            elif grid[r][c]==0:
                return 0
            else:
                visited.add((r,c))
            return 1+dfs(r+1, c)+dfs(r-1, c)+dfs(r, c+1)+dfs(r, c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    area=dfs(r,c)
                    max_area=max(max_area,area)

        return max_area
        