class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        for i in range(len(nums)):
            n = nums[i]
            comp = target - n
            if comp in comps:
                return [i, comps[comp]]
            comps[n] = i