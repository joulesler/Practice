package main

func maxSubArray(nums []int) int {
	var maxSum int = nums[0]
	currSum := 0

	for i := 0; i < len(nums); i++ {
		// Assigns the first number in the array as currSum on initialisation
		currSum += nums[i]

		// Ordering matters for the case of [-1, -2]

		if maxSum < currSum {
			maxSum = currSum
		}
		// Part of the reset if there are two consecutive non-positive numbers
		if currSum < 0 {
			currSum = 0
		}

	}
	return maxSum
}
