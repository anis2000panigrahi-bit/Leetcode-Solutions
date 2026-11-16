
class Solution(object):
    def isSameTree(self, p, q):
        # Both nodes are empty
        if p is None and q is None:
            return True

        # Only one node is empty
        if p is None or q is None:
            return False

        # Check node values
        if p.val != q.val:
            return False

        # Recursively compare left and right subtrees
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
