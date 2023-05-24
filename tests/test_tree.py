from unittest import TestCase
from data_structures.binary_search_tree import BinarySearchTree
from data_structures.nodes import Node

class TreeTest(TestCase):
    def test_impressao2(self):
        tree = BinarySearchTree.from_list([5, 3, 8, 6, 9])
        impressao =  "(5 (3) (8 (6) (9)))"
        self.assertEqual(tree.imprimeArvore(2), impressao)

    def test_impressao1(self):
        tree = BinarySearchTree.from_list([5, 3, 8, 6, 9])
        self.assertEqual(tree.imprimeArvore(2), "(5 (3) (8 (6) (9)))")  # Assert that the result is equal to 2
        impressao = "5------------------------\n\t3----------------\n\t8----------------\n\t\t6--------\n\t\t9--------\n"
        self.assertEqual(tree.imprimeArvore(1), impressao)

    def test_eh_completa(self):
        tree = BinarySearchTree.from_list([5, 3, 8, 6, 10, 9, 2, 1, 4])
        self.assertFalse(tree.ehCompleta())

        tree = BinarySearchTree.from_list([5, 3, 8, 6, 10, 9, 2, 1, 4, 0])
        self.assertFalse(tree.ehCompleta())

        tree = BinarySearchTree.from_list([1, 2])
        self.assertTrue(tree.ehCompleta())

        tree = BinarySearchTree.from_list([1, 0, 2])
        self.assertTrue(tree.ehCompleta())

        tree = BinarySearchTree.from_list([5, 3, 2, 8, 1, 6, 9])
        self.assertFalse(tree.ehCompleta())

        tree = BinarySearchTree.from_list([5, 3, 2, 8, 1, 6, 9, 4])
        self.assertFalse(tree.ehCompleta())

    def test_remove(self):
        tree = BinarySearchTree.from_list([5, 3, 8, 6, 10, 9, 2, 1, 4])
        tree.remove(3)
        tree.remove(2)
        self.assertIsNone(tree.search(3))
        self.assertIsNone(tree.search(2))
        tree.insert(2)
        self.assertIsNotNone(tree.search(2))



    def test_search(self):
        tree = BinarySearchTree.from_list([5, 3, 8, 6, 10, 9, 2, 1, 4])
        node = tree.search(9)
        self.assertEqual(node, Node(value=9, left=None, right=None, height=0))


    def test_eh_cheia(self):
        tree = BinarySearchTree.from_list([5, 3, 8, 6, 9])
        self.assertEqual(tree.ehCheia(), True)

        tree = BinarySearchTree.from_list([5, 3, 2, 8, 1, 6, 9])
        self.assertEqual(tree.ehCheia(), False)

    def test_pre_ordem(self):
        tree = BinarySearchTree.from_list([5, 3, 8, 6, 9])
        self.assertEqual(tree.pre_ordem(), "5 3 8 6 9")

        tree = BinarySearchTree.from_list([5, 3, 8, 6, 10, 9, 2, 1, 4])
        self.assertEqual(tree.pre_ordem(), "5 3 2 1 4 8 6 10 9")

    def test_enesimoElemento(self):
        tree = BinarySearchTree.from_list([5, 3, 8, 6, 9])
        self.assertEqual(tree.enesimoElemento(2), 5)

        tree = BinarySearchTree.from_list([5, 3, 8, 6, 10, 9, 2, 1, 4])
        self.assertEqual(tree.enesimoElemento(1), 1)

    def test_media(self):
        tree = BinarySearchTree.from_list([5, 3, 8, 6, 9])
        self.assertEqual(tree.media(9), 9.0)

        self.assertEqual(tree.media(5), 6.2)

        
    def test_posicao(self):
        tree = BinarySearchTree.from_list([5, 3, 8, 6, 9])
        self.assertEqual(tree.posicao(5), 2)

        self.assertEqual(tree.posicao(3), 1)

        self.assertEqual(tree.posicao(9), 5)