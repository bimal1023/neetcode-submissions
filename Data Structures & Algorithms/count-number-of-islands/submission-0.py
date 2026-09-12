class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        cols=len(grid[0])
        visited=set()
        
        def dfs(r,c):
            if r<0 or r>=row:
                return
            elif c<0 or c>=cols:
                return
            elif (r,c) in visited:
                return
            elif grid[r][c]=='0':
                return 
            else:
                visited.add((r,c))
            dfs(r+1, c)   # down
            dfs(r-1, c)   # up
            dfs(r, c+1)   # right
            dfs(r, c-1)   # left
        island_count=0
        for r in range(row):
            for c in range(cols):
                if grid[r][c]=="1"and (r,c)not in visited:
                    island_count+=1
                    dfs(r,c)
        return island_count

            