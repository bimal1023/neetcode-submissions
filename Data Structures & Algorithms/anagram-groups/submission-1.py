class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for char in strs:
            key="".join(sorted(char))
            if key not in seen:
                seen[key]=[]
            seen[key].append(char)
        return list(seen.values())