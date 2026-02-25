
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        ld=self.minDepth(root.left)
        rd=self.minDepth(root.right)
        return min(ld, rd)+1
        