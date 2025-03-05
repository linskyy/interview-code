class Merge:
    temp = []

    @staticmethod
    def sort(nums):
        Merge.temp = [0] * len(nums)
        Merge._sort(nums, 0, len(nums) - 1)
    
    @staticmethod
    def _sort(nums, lo, hi):
        if lo >= hi:
            return
        mid = lo + (hi - lo) // 2
        Merge._sort(nums, lo, mid)
        Merge._sort(nums, mid + 1, hi)
        Merge._merge(nums, lo, mid, hi)
    
    @staticmethod
    def _merge(nums, lo, mid, hi):
        for i in range(lo, hi + 1):
            Merge.temp[i] = nums[i]
        
        i, j = lo, mid + 1
        for p in range(lo, hi):
            if i == mid + 1:
                nums[p] = Merge.temp[j]
                j += 1
            elif j == hi + 1:
                nums[p] = Merge.temp[i]
                i += 1
            elif Merge.temp[i] < Merge.temp[j]:
                nums[p] = Merge.temp[i]
                i += 1
            else:
                nums[p] = Merge.temp[j]
                j += 1

nums = [1,3,4,2,5]
Merge.sort(nums)
print(nums)