import random

class Quick:
    @staticmethod
    def sort(nums):
        random.shuffle(nums)
        Quick._sort(nums, 0, len(nums) - 1)

    @staticmethod
    def _sort(nums, lo, hi):
        if lo > hi:
            return
        p = Quick.partition(nums, lo, hi)
        Quick._sort(nums, lo, p - 1)
        Quick._sort(nums, p + 1, hi)
    
    @staticmethod
    def partition(nums, lo, hi):
        pivot = nums[lo]
        i, j = lo + 1, hi
        while i <= j:
            while i < hi and nums[i] <= pivot:
                i += 1
            while j > lo and nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[lo], nums[j] = nums[j], nums[lo]
        return j

nums = [1,3,5,2,4]
Quick.sort(nums)
print(nums)
        