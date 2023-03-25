class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Two pointer solution
        # Since input is sorted, start index at zero, then increment
        startPoint = 0
        endPointer = len(numbers) - 1

        while True:
            if startPoint > endPointer:
                return [0,0]
            if numbers[startPoint] + numbers[endPointer] > target:
                endPointer -= 1
            elif numbers[startPoint] + numbers[endPointer] < target:
                startPoint += 1
            else:
                if startPoint == endPointer:
                    return False
                else:
                    return [ startPoint+1, endPointer+1]
                
sol = Solution()

cases = [([2,7], 9), ([2,7,11,15], 9), ([2,3,4], 6)]

for i in cases:
    print(sol.twoSum(i[0], i[1]))

