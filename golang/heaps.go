package main

import "fmt"

type MaxHeap struct {
	array []int
}

func (h *MaxHeap) insert(key int) {
	h.array = append(h.array, key)
	h.heapifyUp(len(h.array) - 1)
}

func (h *MaxHeap) removeTop(key int) {
	h.heapifyDown(key)
}

func parent(child int) int {
	return (child - 1) / 2
}

func left(parent int) int {
	return parent*2 + 1
}

func right(parent int) int {
	return parent*2 + 2
}

func (h *MaxHeap) heapifyUp(index int) {
	for h.array[index] > h.array[parent(index)] {
		h.swap(index, parent(index))
	}
}

// Assume that the number has already been swapped
func (h *MaxHeap) heapifyDown(index int) {
	for h.array[index] < h.array[right(index)] {
		if h.array[index] < h.array[left(index)] {
			h.swap(index, left(index))
		} else {
			h.swap(index, right(index))
		}
	}
}

func (h *MaxHeap) checkLargerChild(index int) int {
	if len(h.array) < right(index) {
		if len(h.array) < left(index) {
			return 0
		}
		return left(index)
	}
	if h.array[left(index)] < h.array[right(index)] {
		return left(index)
	}
	return right(index)
}

func (heap *MaxHeap) swap(indexA int, indexB int) {
	heap.array[indexA], heap.array[indexB] = heap.array[indexB], heap.array[indexA]
}

func main() {
	heap := &MaxHeap{}
	fmt.Println(heap)

	build := []int{10, 20, 30}
	for _, v := range build {
		heap.insert(v)
		fmt.Println(heap)
	}

}
