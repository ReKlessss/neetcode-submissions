# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(node: TreeNode | None) -> int:
            if not node: return 0

            l_depth = dfs(node.left)
            r_depth = dfs(node.right)

            if abs(l_depth - r_depth) > 1:
                self.balanced = False

            return 1 + max(l_depth, r_depth)

        dfs(root)
        return self.balanced