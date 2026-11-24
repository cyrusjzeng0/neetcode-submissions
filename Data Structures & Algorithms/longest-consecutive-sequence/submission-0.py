class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 in nums: 
                continue
            curr_len, curr_val = 1, num
            while curr_val + 1 in nums:
                curr_len += 1
                curr_val += 1
            max_len = max(max_len, curr_len) # keep only highest length
        
        return max_len