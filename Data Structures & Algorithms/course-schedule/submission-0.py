from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]* numCourses
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        queue=deque(i for i in range(numCourses) if indegree[i]==0)
        order=[]
        while queue:
            node=queue.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        return True if len(order)==numCourses else False