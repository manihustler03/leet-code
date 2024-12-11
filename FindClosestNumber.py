class Solution(object):
    def findClosestNumber(self, nums):
        num = float("inf")
        for i in nums:
            if abs(i) < abs(num):
                num = i
            elif abs(i) == abs(num):
                if i > num:
                    num = i
        return num


nums = [-100000, -100000]
obj = Solution()
print(obj.findClosestNumber(nums))
