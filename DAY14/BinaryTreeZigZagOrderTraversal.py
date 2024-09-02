from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        right = True
        res = []
        while queue:
            qlen = len(queue)
            temp = []
            for x in range(len(queue)):
                if right:
                    node = queue.popleft()
                    if node:
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                        temp.append(node.val)

                else:
                    node = queue.pop()
                    if node:
                        if node.right:
                            queue.appendleft(node.right)
                        if node.left:
                            queue.appendleft(node.left)
                        temp.append(node.val)
            right= not right
            if len(temp)!=0:
                res.append(temp)
        return (res)