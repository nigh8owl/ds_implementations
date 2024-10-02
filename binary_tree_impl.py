class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
    
    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res = res + self.inorder_traversal(root.right)
        return res    
    
    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right) 
        return res
    





# Unit tests
import unittest

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(12)
        self.tree.insert(18)

    def test_inorder_traversal(self):
        expected_inorder = [3, 5, 7, 10, 12, 15, 18]
        self.assertEqual(self.tree.inorder_traversal(self.tree.root), expected_inorder)

    def test_preorder_traversal(self):
        expected_preorder = [10, 5, 3, 7, 15, 12, 18]
        self.assertEqual(self.tree.preorder_traversal(self.tree.root), expected_preorder)

if __name__ == '__main__':
    unittest.main()