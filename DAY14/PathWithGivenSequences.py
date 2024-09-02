#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def findPath(self, root, sequence):
    # TODO: Write your code here
    def dfs(pointer, root):
      if pointer==len(sequence)-1 and root and not root.left and not root.right :
        if sequence[pointer]==root.val:
          return True
        return False
      if pointer==len(sequence) or not root:
        return False
      if sequence[pointer]!=root.val:
        return False
      left = dfs(pointer+1, root.left)
      right = dfs(pointer+1, root.right)
      return (left or right)
    pointer = 0
    res = dfs(pointer, root)
    return res