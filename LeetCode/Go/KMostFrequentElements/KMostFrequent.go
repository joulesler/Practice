package kmostfrequent

import "fmt"

func topKFrequent(nums []int, k int) []int {
	numMap := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		numMap[nums[i]] += 1
	}

	var kElement = make([]int, k)
	fmt.Print(numMap)
	for i := 0; i < len(nums); i++ {
		for j := 0; j < k; j++ {
			if numMap[nums[i]] > kElement[j] {
				fmt.Println(numMap[nums[i]])
				if j == len (kElement){
					kElement[j] = nums[i]
				} else {
					continue
				}
			}
		}
	}

	return kElement
}
