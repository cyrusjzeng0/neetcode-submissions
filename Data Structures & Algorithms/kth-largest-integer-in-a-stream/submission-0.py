class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.nums = k, nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        list_sort = sorted(self.nums, reverse = True)
        return list_sort[self.k-1]
