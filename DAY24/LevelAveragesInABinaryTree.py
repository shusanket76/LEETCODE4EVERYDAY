from collections import deque


#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution:
  def findLevelAverages(self, root):
    result = []
    # TODO: Write your code here
    queue = deque()
    queue.append(root)
    while queue:
      qlen = len(queue)
      temp = 0
      for x in range(qlen):
        
        node = queue.popleft()
        if node.val:
          temp+=node.val
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
      avg = temp/qlen
      result.append(avg)
    return result
