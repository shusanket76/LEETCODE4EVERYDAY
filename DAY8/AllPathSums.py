#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def findPaths(self, root, required_sum):
    allPaths = []
    # TODO: Write your code here
    def dfs(root, target, curr):
      print(curr)
      if not root:
        return 
      curr.append(root.val)
      if (not root.left and not root.right) and target==root.val:
        # curr.append(root.val)
        # print(curr)
        allPaths.append(curr[:])
        # return 
        return 
      left = dfs(root.left, target-root.val, curr)
      right = dfs(root.right, target-root.val, curr)
      curr.pop()      
    # dfs(root.left, required_sum-root.val, curr = [root.val])
    # dfs(root.right, required_sum-root.val, curr = [root.val])
    dfs(root, required_sum, curr = [])
    return allPaths
