from collections import deque,defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # building the adjacency list from edge list
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=set()
        components=0

        # iterate over every node
        for i in range(n):
            if i not in visited:
                components+=1

                # run bfs to visit all connected nodes
                visited.add(i)
                queue=deque([i])

                while queue:
                    curr=queue.popleft()
                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        return components
