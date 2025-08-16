class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # if no left child, go right
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # if no right child, go left
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # both children exist → take min
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
