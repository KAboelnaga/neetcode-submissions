
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i, string in enumerate(strs):
            sort = str(sorted(string))
            if sort in hashmap:
                hashmap[sort].append(string)
            else:
                hashmap[sort] = [string]
        res =[]
        for key in hashmap:
            res.append(hashmap[key])
        return res
        
        