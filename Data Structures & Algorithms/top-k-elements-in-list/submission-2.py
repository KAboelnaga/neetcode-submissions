class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        while k:
            best = max(hashmap, key=hashmap.get)
            output.append(best)
            hashmap[best] = 0
            k -= 1
        return output