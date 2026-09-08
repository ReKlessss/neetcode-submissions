# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        to_visit = []
        max_depth = 0

        to_visit.append((root, 0))
        while to_visit:
            tmp = to_visit.pop()
            node = tmp[0]
            curr_depth = tmp[1] + 1

            max_depth = max(max_depth, curr_depth)

            if node.right:
                to_visit.append((node.right, curr_depth))
            
            if node.left:
                to_visit.append((node.left, curr_depth))
        
        return max_depth


