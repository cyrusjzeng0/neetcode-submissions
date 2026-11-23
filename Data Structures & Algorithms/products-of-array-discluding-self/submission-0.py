class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initial approach
        """n = len(nums)
        prod_left, prod_right = [1 for _ in range(n)], [1 for _ in range(n)]

        for i in range(1, n):
            prod_left[i] = prod_left[i-1] * nums[i-1]
            prod_right[n-i-1] = prod_right[n-i] * nums[n-i]

        out = [prod_left[i] * prod_right[i] for i in range(n)]
        return out"""

        # optimized O(1) space approach
        n, currProduct = len(nums), nums[-1]
        out = [1 for _ in range(n)]

        for i in range(1, n):
            out[i] = out[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            out[i] *= currProduct
            currProduct *= nums[i]

        return out