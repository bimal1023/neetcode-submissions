from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        enque=deque(i for i in range(numCourses) if indegree[i]==0)
        order=[]
        while enque:
            node=enque.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    enque.append(nei)
        return order if numCourses==len(order) else []