class Solution:
    def twoSum(self, nums, target: int):
        
        record = {}
        for i in range(len(nums)):
            num = nums[i]
            remainder = target - num
            if record.get(remainder) == None:
                record[num] = i
            else:
                return [i, record.get(remainder)]


sol = Solution()

cases = [([2,7], 9)]

for i in cases:
    print(sol.twoSum(i[0], i[1]))