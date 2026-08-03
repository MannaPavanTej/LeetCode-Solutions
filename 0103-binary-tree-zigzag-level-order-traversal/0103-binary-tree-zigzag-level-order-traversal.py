# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        d=deque([root])
        ans=[]
        left_to_right = True
        while d:
            li=[]
            for i in range(len(d)):
                node=d.popleft()
                li.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            if not left_to_right:
                li.reverse()
                
            ans.append(li)

            left_to_right = not left_to_right
        return ans