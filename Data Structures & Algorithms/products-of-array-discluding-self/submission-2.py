class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, r_product = len(nums), 1
        products = [1] * n

        for i in range(1, n):
            products[i] = products[i-1] * nums[i-1]
        
        for j in range(n-1, 0, -1):
            r_product *= nums[j]
            products[j-1] *= r_product

        return products