package main

import (
	"fmt"
)

func findMin(nums []int) int {
	leftP := 0
	rightP := len(nums) - 1

	for i := 0; i < len(nums); i++ {
		fmt.Println("leftP: ", leftP, "rightP: ", rightP)
		if rightP-leftP <= 1 {
			if nums[leftP] < nums[rightP] {
				return nums[leftP]
			} else {
				return nums[rightP]
			}
		}
		mid := (rightP + leftP) / 2
		if nums[mid] <= nums[rightP] {
			rightP = mid
		} else {
			leftP = mid
		}
		fmt.Println("mid: ", mid)
	}
	return -1
}

func main() {
	findMin([]int{4, 5, 6, 7, 0, 1, 2})
}
