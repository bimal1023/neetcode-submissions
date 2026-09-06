import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for point in points:
            x,y=point
            dist=x**2+y**2
            heapq.heappush(heap,(-dist,point))
        while len(heap)>k:
            heapq.heappop(heap)
        result=[]
        for entry in heap:
            dist,point=entry
            result.append(point)
        return result
