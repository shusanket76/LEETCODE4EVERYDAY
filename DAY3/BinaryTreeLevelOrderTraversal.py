# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []
      
        if root is not None:
            queue.append(root)
            while queue:
                qlen = len(queue)
                temp = []
                for x in range(qlen):
                  
                    node = queue.popleft()
                    if node:
                        temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
             
                if len(temp)!=0:
                    res.append(temp)
        return res