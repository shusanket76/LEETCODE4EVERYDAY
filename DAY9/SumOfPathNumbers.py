#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def findSumOfPathNumbers(self, root):
    # TODO: Write your code here
    res = [0]
    def dfs(root, st):
      if not root:
        return 
      st+=str(root.val)
      if (not root.left and not root.right):
        res[0]+=int(st)
      left = dfs(root.left, st)
      right = dfs(root.right, st)
    dfs(root,  "")
    return res[0]