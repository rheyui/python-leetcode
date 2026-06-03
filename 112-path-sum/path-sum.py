# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):

        # If tree is empty
        if root is None:
            return False

        # Check if current node is a leaf node
        if root.left is None and root.right is None:

            # Check if leaf value equals targetSum
            return root.val == targetSum

        # Remaining sum after using current node value
        remaining = targetSum - root.val

        # Check left side or right side
        left_path = self.hasPathSum(root.left, remaining)
        right_path = self.hasPathSum(root.right, remaining)

        return left_path or right_path