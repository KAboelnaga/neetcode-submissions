class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        while k:
            output.append(max(hashmap, key=hashmap.get)) 
            hashmap[max(hashmap, key=hashmap.get)] = 0
            k -= 1
        return output