class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum_numbers = numbers[l] + numbers[r] 
            if sum_numbers > target:
                r -= 1
            elif sum_numbers < target:
                l += 1
            else: return [l + 1, r + 1]
