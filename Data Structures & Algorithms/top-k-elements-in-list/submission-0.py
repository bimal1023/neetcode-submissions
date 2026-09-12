class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        for num in nums:
            counts[num]=counts.get(num,0)+1
        heap=[]
        for num,count in counts.items():
            heapq.heappush(heap,(count,num))
        while len(heap)>k:
            heapq.heappop(heap)
        result=[]
        for value in heap:
            count,num=value
            result.append(num)
        return result
            
        
