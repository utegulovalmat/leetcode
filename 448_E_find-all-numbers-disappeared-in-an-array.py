class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for idx, n in enumerate(nums):
            res[n-1] = 1
        
        return [idx+1 for idx,_ in enumerate(res) if _ == 0]