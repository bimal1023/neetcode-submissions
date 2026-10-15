class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(i):
            str_num=str(i)
            i=sum(int(d)**2 for d in str_num)
            return i
        slow=fast=n
        while slow!=1:
            slow=get_next(slow)
            fast=get_next(fast)
            fast=get_next(fast)
            if slow==fast and slow!=1:
                return False
        return True