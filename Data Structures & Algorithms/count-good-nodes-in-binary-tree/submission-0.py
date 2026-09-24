# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, maxx=-1000) -> int:
        if not root: return 0
        
        good_node = 0
        if root.val >= maxx:
            maxx = root.val
            good_node = 1

        left_goodies = self.goodNodes(root.left, maxx)
        right_goodies = self.goodNodes(root.right, maxx)

        return good_node + left_goodies + right_goodies