class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #Keep track of the current index, and the number of jumps
        #Approach: Keep track of all the counts of zeros
        #shift each element by that many zeros
        
        lastEntry= 0 
        count = 0
        
        for i in range(len(nums)):
            print(nums)
            if nums[i] ==0:
                count += 1
            else:
                lastEntry +=1
            if (i + count < len(nums)):
                nums[lastEntry] = nums[i+1]
            if (i + count > len(nums)):
                nums[i] = 0 
                