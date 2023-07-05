import unittest
from data_structures.avl_tree import AvlTree
from data_structures.nodes import Node

class AvlTreeTests(unittest.TestCase):
    def test_insert_basic(self):
        tree = AvlTree()
        tree.insert(5)
        tree.insert(10)
        tree.insert(8)

        self.assertEqual(tree.root.value, 8)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.right.value, 10)

        tree.insert(3)
        self.assertEqual(tree.root.left.left.value, 3)

        tree.insert(13)
        tree.insert(11)

        self.assertEqual(tree.root.right.value, 11)
        self.assertEqual(tree.root.right.left.value, 10)
        self.assertEqual(tree.root.right.right.value, 13)

    def test_insert_complex1(self):
        tree = AvlTree()
        tree.insert(1)
        tree.insert(2)
        tree.insert(3)
        tree.insert(4)
        tree.insert(5)
        tree.insert(6)
        tree.insert(7)
        tree.insert(8)
        tree.insert(9)
        tree.insert(10)
        tree.insert(11)
        tree.insert(12)
        tree.insert(13)
        tree.insert(14)

        pre_ordem = [
            8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 13, 14
        ]

        self.assertEqual(tree.get_pre_ordem_list(), pre_ordem)


    def test_remove(self):
        tree = AvlTree()
        tree.insert(1)
        tree.insert(2)
        tree.insert(3)
        tree.insert(4)
        tree.insert(5)
        tree.insert(6)
        tree.insert(7)
        tree.insert(8)
        tree.insert(9)
        tree.insert(10)
        tree.insert(11)
        tree.insert(12)
        tree.insert(13)
        tree.insert(14)

        tree.remove(8)

        pre_ordem = [ 9, 4, 2, 1, 3, 6, 5, 7, 12, 10, 11, 13, 14 ]
        self.assertEqual(tree.get_pre_ordem_list(), pre_ordem)

    def test_remove_more_complex(self):
        tree = AvlTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(10)
        tree.insert(2)
        tree.insert(4)
        tree.insert(7)
        tree.insert(11)
        tree.insert(12)
        tree.insert(1)
        tree.insert(6)
        tree.insert(9)
        tree.insert(8)

        pre_ordem = [ 5, 3, 2, 1, 4, 10, 7, 6, 9, 8, 11, 12 ]
        self.assertEqual(tree.get_pre_ordem_list(), pre_ordem)

        tree.remove(5)

        pre_ordem = [ 6, 3, 2, 1, 4, 10, 8, 7, 9, 11, 12 ]
        self.assertEqual(tree.get_pre_ordem_list(), pre_ordem)


    def test_search(self):
        tree = AvlTree()
        tree.insert(5)
        tree.insert(10)
        tree.insert(3)
        tree.insert(8)
        tree.insert(12)
        tree.insert(15)

        self.assertEqual(tree.search(10), tree.root)
        self.assertEqual(tree.search(5), tree.root.left)
        self.assertEqual(tree.search(12), tree.root.right)
        self.assertEqual(tree.search(15), tree.root.right.right)

if __name__ == '__main__':
    unittest.main()
