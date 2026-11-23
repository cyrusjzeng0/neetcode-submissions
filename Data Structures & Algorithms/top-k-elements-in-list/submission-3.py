class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        arr = [set() for _ in range(len(nums) + 1)]
        max_idx = -1

        for num in counts:
            count = counts[num]
            arr[count].add(num)
            if count > max_idx:
                max_idx = count

        k_top = []
        curr_idx = max_idx
        
        while len(k_top) < k:
            k_top.extend(arr[curr_idx])
            curr_idx -= 1
            
        return k_top[:k]
        