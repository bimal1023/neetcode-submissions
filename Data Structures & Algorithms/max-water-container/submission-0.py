class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        max_water=0
        while left<right:
            width=right-left
            height=min(heights[right],heights[left])
            area=width*height
            max_water=max(area,max_water)
            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1
        return max_water
