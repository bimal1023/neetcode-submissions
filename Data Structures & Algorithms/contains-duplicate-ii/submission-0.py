class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()
        for i in range(len(nums)):
            current_num=nums[i]
            if current_num in window:
                return True
            window.add(current_num)
            if len(window)>k:
                oldest_num=nums[i-k]
                window.remove(oldest_num)
        return False
        