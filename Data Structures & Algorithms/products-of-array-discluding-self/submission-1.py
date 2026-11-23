class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [1] * n, [1] * n
        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]
            right[n-i-1] = nums[n-i] * right[n-i]
        
        products = [a * b for a, b in zip(left, right)]
        return products
