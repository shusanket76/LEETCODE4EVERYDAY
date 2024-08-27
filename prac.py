#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

def findPaths(root, required_sum):
    allPaths = []
    def dfs(root,curr, targetSum):
      print(targetSum)
      print(curr)
      print("---------------")
      if not root or targetSum<0:
        return 
      targetSum-=root.val
      curr.append(root.val)
      if (not root.left and not root.right) and targetSum==0:
        print("answer dow=>", curr)
        allPaths.append(curr[:])
        return
      left = dfs(root.left, curr, targetSum)
      # curr.pop()
      right = dfs(root.right, curr, targetSum)
      # curr.pop()

    print("required_sum=>", required_sum)
    dfs(root,curr=[], targetSum=required_sum)
    # TODO: Write your code here
    print("answer=>", allPaths)
    return allPaths

a  = findPaths()