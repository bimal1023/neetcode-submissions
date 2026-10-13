from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        queue=deque()
        fresh=0

        # lets collect initial rotten fruits and count fresh fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        # edge case : NO fresh fruit to rot
        if fresh==0:
            return 0
        minutes=0
        direction=[(0,1),(0,-1),(1,0),(-1,0)]

        # Multi source BFS

        while queue and fresh>0:
            minutes+=1
            for _ in range(len(queue)):
                r,c =queue.popleft()
                for dr,dc in direction:
                    nr,nc= r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1
                        queue.append((nr,nc))
        return minutes if fresh==0 else -1