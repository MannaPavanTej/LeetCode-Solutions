# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root==None:
                return 'null'
            helper(root.left)
            li.append(root.val)
            helper(root.right)
        li=[]
        helper(root)
        if li == sorted(li) and len(li) == len(set(li)):
            return True
        else:
            return False