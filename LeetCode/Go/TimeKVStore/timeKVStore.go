package main

import "fmt"

type TimeMap struct {
	times map[string][]StringIntTuple
}

type StringIntTuple struct {
	StringVal string
	IntVal    int
}

func Constructor() TimeMap {
	fmt.Println("New object initialised")
	timeMap := TimeMap{
		times: make(map[string][]StringIntTuple),
	}
	return timeMap
}

func (this *TimeMap) Set(key string, value string, timestamp int) {
	if this.times[key] == nil {
		this.times[key] = []StringIntTuple{}
	}
	this.times[key] = append(this.times[key], StringIntTuple{
		StringVal: value,
		IntVal:    timestamp,
	})
	return
}

func (this *TimeMap) Get(key string, timestamp int) string {
	if this.times[key] != nil {
		return binarySearch(this.times[key], timestamp)
	} else {
		if timestamp == 0 {
			return ""
		}
	}
	return ""
}

func binarySearch(nums []StringIntTuple, target int) string {
	l, r := 0, len(nums)-1

	if target < nums[l].IntVal {
		return ""
	} else if target >= nums[r].IntVal {
		return nums[r].StringVal
	} else {
		for i := 0; i < len(nums); i++ {
			mid := (l + r) / 2
			if l == r {
				// Exit condition if left and right have coincided
				if nums[mid].IntVal == target {
					// If there is an exact match with the mid value
					return nums[mid].StringVal
				} else if target < nums[l].IntVal {
					return nums[l-1].StringVal
				} else { // Return the closest value to the left
					return nums[l].StringVal
				}
			}

			if target <= nums[mid].IntVal {
				r = mid
			} else {
				l = mid + 1
			}
		}
	}
	return ""
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */

func main() {
	// var timeMap = Constructor()
	// timeMap.Set("foo", "bar", 1)
	// fmt.Println(timeMap.Get("foo", 1))
	// timeMap.Set("foo", "bar", 4)
	// fmt.Println(timeMap.Get("bar", 3))

	var timeMap2 = Constructor()
	timeMap2.Set("love", "high", 10)
	timeMap2.Set("love", "low", 20)
	fmt.Println(timeMap2.Get("love", 15))

}
