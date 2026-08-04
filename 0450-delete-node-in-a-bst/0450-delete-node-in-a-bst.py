# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root==None:
            return None
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            if root.left==None and root.right==None:
                return None
            elif root.left==None:
                return root.right
            elif root.right==None:
                return root.left
            else:
                cur=root.right
                while cur.left!=None:
                    cur=cur.left
                root.val=cur.val
                root.right=self.deleteNode(root.right,cur.val)
                return root
        return root