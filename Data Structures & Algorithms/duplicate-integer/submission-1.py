class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        passed = []
        for val in range(len(nums)):
            if nums[val] in passed:
                return True
            passed.append(nums[val])
        return False