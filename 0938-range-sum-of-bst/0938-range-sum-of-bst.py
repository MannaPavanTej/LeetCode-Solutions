# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        # If node's value is less than low, left subtree can be skipped
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        # If node's value is greater than high, right subtree can be skipped
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        
        # Node's value is within range, include it and search both sides
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        return sum