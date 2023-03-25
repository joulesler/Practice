class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach: as long as the current sum is positive, it is contributing to the sum of the sub array
        # Start from rear? Should be bi-directional
        # nextSum = 0

        currSum = 0
        maximum = nums[0]
        for i in nums:
            # if i > 0:
            if currSum + i > 0:
                currSum += i
            else:
                currSum = 0
            if maximum < currSum:
                maximum = currSum
            print (currSum)

        if maximum == 0:
            return max(nums)
        return maximum

                    

# maximum sum 
test = [-2,1,-3,4,-1,2,1,-5,4], [-2,1], [-1], [-1, -2]
'''
4 -> -5 = -1 do not add
1 -> 2 -> -1 -> 4 = 6 (sum still positive)
a,b,c,x,y,z

a + b > 0?
a + b + c > 0?
" + d > 0? 
'''

instance = Solution()

for j in test:
    print(
        "the max is: ", instance.maxSubArray(j) 
        )