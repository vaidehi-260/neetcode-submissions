# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.max_dif = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.max_dif = max(self.max_dif, abs(left-right))
            return 1+max(left, right)        ## this is height so agar node pe left ya right nhi hai
        dfs(root)                            ## toh ye 1 return kar dega, that is node itself
        return self.max_dif<=1
        
