from unittest import TestCase
from data_structures.binary_search_tree import BinarySearchTree

class TreeTest(TestCase):
    def test_impressao2(self):
        tree = BinarySearchTree.from_list([5, 3, 8, 6, 9])
        impressao =  "(5 (3) (8 (6) (9)))"
        self.assertEqual(tree.imprimeArvore(2), impressao)

#     def test_impressao1(self):
#         tree = BinarySearchTree.from_list([5, 3, 8, 6, 9])
#         self.assertEqual(tree.imprimeArvore(2), "(5 (3) (8 (6) (9)))")  # Assert that the result is equal to 2
#
#         impressao = '''5 -----------
# \t3 ---------
# \t\t8 -------
# \t\t\t6 -----
# \t\t\t\t9 ---
#         '''
#
#         self.assertEqual(tree.imprimeArvore(1), impressao)

    def test_eh_completa(self):
        tree = BinarySearchTree.from_list([5, 3, 8, 6, 10, 9, 2, 1, 4])
        self.assertEqual(tree.ehCompleta(), True)

        tree = BinarySearchTree.from_list([5, 3, 8, 6, 10, 9, 2, 1, 4, 0])
        self.assertEqual(tree.ehCompleta(), False)

        tree = BinarySearchTree.from_list([1, 2])
        self.assertEqual(tree.ehCompleta(), True)

        tree = BinarySearchTree.from_list([5, 3, 2, 8, 1, 6, 9])
        self.assertEqual(tree.ehCompleta(), False)

        tree = BinarySearchTree.from_list([5, 3, 2, 8, 1, 6, 9 , 4])
        self.assertEqual(tree.ehCompleta(), True)


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
