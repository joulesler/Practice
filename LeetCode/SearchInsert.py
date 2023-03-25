class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if (target < nums[0] ):
            return 0
        #If no numbers left
        if (len(nums) == 1):
            if nums[0] == target:
                return 0
            else:
                return 1
        
        # Start index at halfway
        index = (len(nums)/2)
        
        # if number is in first half
        if (nums[index] == target):
            return index
        elif (nums[index] > target):    
            result = self.searchInsert(nums[0:index], target)
            #print(result)
            # add result to the index

        # search second half 
        else: 
            result = self.searchInsert(nums[index:], target)
            #print(result)
            result = index + result
            #print("+", index)
        return result