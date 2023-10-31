package main

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func main() {

}

func copyRandomList(head *Node) *Node {
	newMap := make(map[*Node]*Node)
	node := head
	for node != nil {
		newMap[node] = &Node{
			Val:    node.Val,
			Next:   nil,
			Random: nil,
		}
		node = node.Next
	}

	node = head
	for node != nil {
		newNode := newMap[node]
		newNode.Next = newMap[node.Next]
		newNode.Random = newMap[node.Random]

		node = node.Next

	}

	return newMap[head]
}
