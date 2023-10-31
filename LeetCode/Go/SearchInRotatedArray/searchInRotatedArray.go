package main

import "fmt"

func search(nums []int, target int) int {
	l, r := 0, len(nums)-1

	for i := 0; i <= len(nums); i++ {
		mid := ((l + r) / 2)
		fmt.Println("left: ", l, "right: ", r, "mid: ", mid)
		if r-l <= 1 {
			fmt.Println(nums[l], nums[r], nums[mid])
			if nums[l] == target {
				return l
			} else if nums[r] == target {
				return r
			} else {
				return (-1)
			}
		}

		if target < nums[mid] {
			// L | Mid > T | R
			if target < nums[l] {
				fmt.Println("case 1")
				// Search right
				l = mid
				// L | T | Mid > R
			} else {
				fmt.Println("case 2")
				// search left
				r = mid - 1
			}
		} else {
			// Target >= mid
			// L | Mid | T | R
			if target < nums[l] {
				fmt.Println("case 3")
				// Search right
				l = mid
			} else {
				// search right
				fmt.Println("case 4")
				l = mid
			}
		}

	}
	return -1
}

func main() {
	fmt.Print(search([]int{5, 1, 3}, 5))
}
