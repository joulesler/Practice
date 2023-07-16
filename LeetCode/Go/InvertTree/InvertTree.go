package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func invertTree(root *TreeNode) *TreeNode {
	node := root
	if node != nil {
		invertTree(node.Left)
		invertTree(node.Right)
		node.Left, node.Right = node.Right, node.Left
	}
	return root
}
