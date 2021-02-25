# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:    
    def __init__(self):
        self.prev = None
        
    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root

if __name__ == '__main__':
    s = Solution()
    root = [-10,9,20,null,null,15,7]
    print(s.flatten(root))

""" 
class Solution:
    def flatten(self, root):
        cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.right = cur.left
                cur.left = None

            cur = cur.right
            
"""