package main

func twoSum(numbers []int, target int) []int {
	i := 0
	j := len(numbers) - 1

	for true {
		// If the left is not big enough
		if target-numbers[i] > numbers[j] {
			i++
		} else if target-numbers[i] == numbers[j] {
			return []int{i + 1, j + 1}
		} else {
			j--
		}
	}
	return []int{}
}
