package insertCache

import "fmt"

type Node struct {
	val  int
	next *Node
	prev *Node
}

type LRUCache struct {
	cache map[int]int
	head  *Node
	tail  *Node
	max   int
}

func Constructor(capacity int) LRUCache {
	lru := LRUCache{
		cache: make(map[int]int),
		max:   capacity,
	}

	return lru
}

func (this *LRUCache) Get(key int) int {
	return this.cache[key]
}

func (this *LRUCache) Put(key int, value int) {
	if len(this.cache) == this.max {
		// If only one node left in list
		if len(this.cache) == 1 {
			delete(this.cache, this.head.val)
			this.head = nil
		} else {
			delete(this.cache, this.tail.val)
			penultimate := this.tail.prev
			penultimate.next = nil
		}
	}
	if this.head == nil {
		this.head = &Node{
			val: key,
		}
		this.tail = this.head
	} else {
		tempNode := this.head
		this.head = &Node{
			val:  key,
			next: tempNode,
		}
	}
	// set the reverse pointer
	if this.head.next != nil {
		this.head.next.prev = this.head
	}
	// set the value in the cache
	this.cache[key] = value

}

func main() {
	cache := Constructor(1)
	cache.Put(1, 1)
	fmt.Println(cache.Get(1))
	cache.Put(2, 2)
	cache.Put(3, 3)
	fmt.Println(cache.Get(1))
	fmt.Println(cache.Get(2))
	fmt.Println(cache.Get(3))
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
