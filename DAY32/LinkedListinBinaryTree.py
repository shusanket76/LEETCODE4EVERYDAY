from collections import deque 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def checksimilarity(node, head):
            # print(node, head)
            if node.val==head.val and head.next is None:
                # print("FOUNDFOUNDFOUNDFOUNDFOUNDFOUNDFOUNDFOUNDFOUNDFOUND")
                return True
            # leftcheck, rightcheck = False, False
            if node.val == head.val:
                if node.left:
                    leftcheck = checksimilarity(node.left, head.next)
                    if leftcheck is True:
                        return True
                if node.right:
                    rightcheck = checksimilarity(node.right, head.next)
                    if rightcheck is True:
                        return True
            return False
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.val==head.val:
                # print("CHECKING")
                res = checksimilarity(node, head)
                if res is True:
                    return True
            if node.left: 
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    