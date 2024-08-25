from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()
        stack = []
        queue.append(root)
        while queue:
            qlen = len(queue)
            temp = []
            for x in range(qlen):
                node = queue.popleft()
                if node:
                    temp.append(node.val)
                if node and node.left:
                    queue.append(node.left)
                if node and  node.right:
                    queue.append(node.right)
            if len(temp)!=0:
                stack.append(temp)
        res = []
        while stack:
            ele = stack.pop()
            res.append(ele)
        return (res)
                