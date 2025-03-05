class Solution:
    def cal_factor(self, n):
        self.num2val = {1:1}
        res = 0
        temp = 1
        for i in range(1, n + 1):
            temp = temp * i 
            res += temp
        return res

    # def factor(self, n):
    #     if n in self.num2val:
    #         return self.num2val[n]
    #     else:
    #         self.num2val[n] = n * self.factor(n - 1)
    #         return self.num2val[n]


s = Solution()
res = s.cal_factor(10)
print(res)
