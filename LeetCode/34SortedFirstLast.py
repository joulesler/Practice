class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = 0
        right = len(nums) -1
        # Corner case- If not inside array
        if nums[left] > target or nums[right] < target:
            return [-1, -1]
        
        while True:
            pivot = (right - left) //2
            
            # End condition
            if nums[left] == target:
                if nums[right] == target:
                    return [left, right]

            # find left index first
            if nums[pivot] < target:
                left = pivot
            elif nums[pivot] == target:
                #Search both sides
                pass
            else:
                right = pivot

sol = Solution()

print(sol.searchRange([5,7,7,8,8,10],8))