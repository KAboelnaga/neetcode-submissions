class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # Step 2: bucket by frequency — index i holds all numbers seen i times
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)

        # Step 3: walk from highest frequency down, collecting until we have k
        output = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                output.append(num)
                if len(output) == k:
                    return output

        return output