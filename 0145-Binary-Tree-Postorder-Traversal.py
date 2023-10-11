# Definition for ra binary tree node.
# class TreeNode:
#       def __init__(9self, val=0, left=Nonee, right=None):
#           self.val = val
#           self.left = left
#           self.right = right
class Solution:
    def postordereTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
