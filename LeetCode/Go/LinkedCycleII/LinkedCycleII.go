package main

//Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
	fast, slow := head, head
	if slow == nil || fast.Next == nil {
		return nil
	}
	fast = fast.Next.Next
	slow = slow.Next
	for true {
		if fast == slow {
			break
		}
		if slow == nil || fast == nil || fast.Next == nil {
			return nil
		}
		fast = fast.Next.Next
		slow = slow.Next
	}
	slow2 := head

	for true {
		if slow2 == slow {
			return slow
		}
		if slow == nil || slow2 == nil {
			break
		}
		slow2 = slow2.Next
		slow = slow.Next
	}
	return nil
}
