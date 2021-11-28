class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        nums_len = len(nums)
        for sum_a in range(0, nums_len):
            for sum_b in range(sum_a + 1, nums_len):
                if nums[sum_a] + nums[sum_b] == target:
                    result.append(sum_a)
                    result.append(sum_b)
                    break
        return result
