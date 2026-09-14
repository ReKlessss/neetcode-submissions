# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subtrees = set()

        def dfs(node: TreeNode) -> str:
            if not node: return "None"

            left_tree = dfs(node.left)
            right_tree = dfs(node.right)

            subtree = f"{node.val}{left_tree}{right_tree}"

            subtrees.add(subtree)

            return subtree

        dfs(root)
        print(subtrees)

        def dfs(node: TreeNode) -> str:
            if not node: return "None"

            left_tree = dfs(node.left)
            right_tree = dfs(node.right)

            subtree = f"{node.val}{left_tree}{right_tree}"

            return subtree
        
        if dfs(subRoot) in subtrees:
            return True
        else:
            return False

