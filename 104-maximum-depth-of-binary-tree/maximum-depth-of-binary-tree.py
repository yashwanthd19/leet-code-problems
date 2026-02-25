class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ld=self.maxDepth(root.left)
        rd=self.maxDepth(root.right)
        return max(ld, rd) + 1
        