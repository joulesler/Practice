package main

func findDuplicate(nums []int) int {
	slow, fast := 0, 0

	if len(nums) == 2 {
		return nums[0]
	}
	slow = nums[slow]
	fast = nums[nums[fast]]
	for slow != fast {
		slow = nums[slow]
		fast = nums[nums[fast]]
	}

	slow2 := 0
	for slow != slow2 {
		slow = nums[slow]
		slow2 = nums[slow2]
	}
	return slow
}

func main() {
	findDuplicate([]int{1, 3, 4, 2, 2})
}
