class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums) - 1
        while True:
            mid = (right + left)//2
            if right == left:
                if target == nums[left]:
                    return left
                return -1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid 


            

sol = Solution()

cases= [([-1,0,3,5,9,12], 9)]

cases= [([-1], 2)]

for i in cases:
    print(sol.search(i[0], i[1]))