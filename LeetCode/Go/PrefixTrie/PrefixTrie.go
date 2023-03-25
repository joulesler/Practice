package main

import "fmt"

func main() {
	trie := Constructor()

	trie.Insert("test")
	fmt.Println(trie)
	fmt.Println(trie.rootNode.nextChar)
	fmt.Print(trie.Search("test"))
	fmt.Print(trie.Search("tes"))
	fmt.Print(trie.StartsWith("test"))
	fmt.Print(trie.StartsWith("tes"))

}

type Trie struct {
	rootNode *Node
}

type Node struct {
	nextChar [chars]*Node
	isEnd    bool
}

// Have to mark end of words
func Constructor() Trie {
	trie := &Trie{rootNode: &Node{}}
	return *trie
}

func (this *Trie) Insert(word string) {
	currNode := this.rootNode
	for i := 0; i < len(word); i++ {
		// If the node does not exist, add new node
		// Otherwise, add on to the node
		idx := word[i] - 'a'
		if currNode.nextChar[idx] == nil {
			currNode.nextChar[idx] = &Node{}
		}
		// Move to the new node
		currNode = currNode.nextChar[idx]

		// Check if node is last for the given word
		if i == len(word)-1 {
			currNode.isEnd = true
		}
	}
	return
}

// To avoid checking last node before checking full character
func (this *Trie) Search(word string) bool {
	currNode := this.rootNode
	for i := 0; i < len(word); i++ {
		idx := word[i] - 'a'
		// On first loop, this is the first character
		if currNode.nextChar[idx] == nil {
			return false
		} else {
			currNode = currNode.nextChar[idx]
		}
	}

	if currNode.isEnd {
		return true
	} else {
		return false
	}
}

func (this *Trie) StartsWith(prefix string) bool {
	currNode := this.rootNode
	for i := 0; i < len(prefix); i++ {
		idx := prefix[i] - 'a'
		// On first loop, this is the first character
		if currNode.nextChar[idx] == nil {
			return false
		} else {
			currNode = currNode.nextChar[idx]
		}
	}
	return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
