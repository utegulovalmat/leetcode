class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        
        def twosum(nums, i, res):
            lo, hi = i+1, len(nums)-1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s < 0:
                    lo += 1
                elif s > 0:
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
        
        for i in range(n):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                twosum(nums, i, res)
        return res
