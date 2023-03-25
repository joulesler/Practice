package main

const chars int = 26

type WordDictionary struct {
	rootNode *Node
}

type Node struct {
	nextChar [chars]*Node
	isEnd    bool
}

func Constructor() WordDictionary {
	return WordDictionary{&Node{}}
}

func (this *WordDictionary) AddWord(word string) {
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

func (this *WordDictionary) Search(word string) bool {
	currNode := this.rootNode
	skips := 0
	for i := 0; i < len(word); i++ {
		if word[i] == '.' {
			skips++
			continue
		} else if skips > 0 {
			// Look for the missing character based on the skips
			for skip :=0; skip < skips; skip ++ {
				for j := 0; j < 26; j++ {
					
				}
			}

		}
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

/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */
