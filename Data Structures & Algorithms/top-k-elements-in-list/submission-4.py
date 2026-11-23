class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums) # counts appearances of each number in nums
        arr = [set() for _ in range(len(nums) + 1)] # stores all potential counts at each index - value 3 at index 2 => two apps. of integer 3

        for num, count in counts.items():
            arr[count].add(num) # append integers to arr

        k_top = []
        curr_idx = len(arr) - 1
        
        while len(k_top) < k:
            k_top.extend(arr[curr_idx]) # merge new integers and flatten
            curr_idx -= 1  # move to next lower count

        return k_top[:k] # remove any excess elements from end of array
        