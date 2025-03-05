class Solution:
    def combines(self, nums):
        self.res = []
        self.track = []
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums, start):
        if len(self.track) > 0:     
            self.res.append(self.track[:])

        for i in range(start, len(nums)):
            self.track.append(nums[i])
            self.backtrack(nums, i + 1)
            self.track.pop()

nums = [1,2,3]
solution = Solution()
res = solution.combines(nums)
print(res)
