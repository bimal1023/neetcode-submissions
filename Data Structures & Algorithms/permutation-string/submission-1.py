
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        need={}
        k=len(s1)
        for ch in s1:
            need[ch]=need.get(ch,0)+1
        
        window={}
        for ch in s2[:k]:
            window[ch]=window.get(ch,0)+1
        if window==need:
            return True
        for right in range(k,len(s2)):
            window[s2[right]]=window.get(s2[right],0)+1
            left_char=s2[right-k]
            window[left_char]-=1
            if window[left_char]==0:
                del window[left_char]
            
            if window==need:
                return True
        return False





        