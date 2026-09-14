class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        for char in t:
            if char in hashmap:
                if hashmap[char] > 0:
                    hashmap[char] -= 1
                else:
                    return False
            else:
                return False

        for key in hashmap:
            if hashmap[key] > 0:
                return False
        return True

        