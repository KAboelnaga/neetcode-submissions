class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)
            if key in hashmap:
                hashmap[key].append(string)
            else:
                hashmap[key] = [string]
        return(list(hashmap.values()))