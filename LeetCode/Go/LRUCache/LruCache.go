package main

import "fmt"

type Node struct {
	val  int
	next *Node
	prev *Node
}

type LRUCache struct {
	cache map[int]Node
	head  *Node
	tail  *Node
	max   int
}

func Constructor(capacity int) LRUCache {
	lru := LRUCache{
		cache: make(map[int]Node),
		max:   capacity,
	}
	lru.head = &Node{}
	lru.tail = &Node{}
	return lru
}

func (this *LRUCache) Insert(someNode *Node) {
	
}

func (this *LRUCache) Remove(someNode *Node) {

}

func (this *LRUCache) Get(key int) int {
	// update pointer
	someNode, exists := this.cache[key]
	if exists {
		this.Remove(&someNode)
		this.Insert(&someNode)
		return this.cache[key].val
	} else {
		return -1
	}
}

func (this *LRUCache) Put(key int, value int) {
	someNode, exists := this.cache[key]
	if exists {
		this.Remove(&someNode)
		this.Insert(&someNode)
	} else {
		this.Insert(&Node{
			val: value,
		})
	}
	if len(this.cache) > this.max {
		delete(this.cache, this.tail.prev.val)
		this.Remove(this.tail.prev)
	}
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
