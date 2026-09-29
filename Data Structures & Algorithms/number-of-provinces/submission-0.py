from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        n=len(isConnected)
        visited=set()
        count=0

        for i in range(n):
            if i not in visited:
                count+=1
                visited.add(i)
                

                queue=deque([i])
                while queue:
                    curr=queue.popleft()
                    for neighbor in range(n):
                        if neighbor not in visited and isConnected[curr][neighbor]==1:
                            visited.add(neighbor)
                            queue.append(neighbor)
        return count
