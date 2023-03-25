class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0
        
        for i in range(len(nums)):
            if (nums[i] !=0 ):
                if (i != lastNonZero):
                    nums[i], nums[lastNonZero] = nums[lastNonZero], nums[i]
                lastNonZero +=1