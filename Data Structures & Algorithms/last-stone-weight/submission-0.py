import heapq
class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap)>1:
            first =-heapq.heappop(heap)
            second=-heapq.heappop(heap)
            if first!=second:
                diff=first-second
                heapq.heappush(heap,-diff)
        if len(heap)==0:
            return 0
        elif len(heap)==1:
            return -heap[0]
            
