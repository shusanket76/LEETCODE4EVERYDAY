# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, targetSum):
            print(targetSum)
            if not root:
                return False
            targetSum-=root.val
            if not root.right and not root.left:
                if targetSum==0:
                    return True
            left  = dfs(root.left, targetSum)
            if left is True:
                return True
            
            right = dfs(root.right, targetSum)
            if right is True:
                return True
            return False
            
        return dfs(root, targetSum)
        