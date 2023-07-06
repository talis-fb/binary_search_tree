from dataclasses import dataclass
from typing import Optional
from data_structures.binary_search_tree import BinarySearchTree
from data_structures.nodes import Node

@dataclass
class AvlTree(BinarySearchTree):
    root: Optional[Node] = None

    def insert(self, value: int):
        self.root = self._insert(self.root, value)
        return f"Elemento {value} adicionado."

    def remove(self, value: int):
        self.root = self._remove(self.root, value)
        return f"Elemento {value} removido."

    def search(self, value: int) -> Optional[Node]:
        return self._search(self.root, value)

    def _insert(self, node: Optional[Node], value: int) -> Optional[Node]:
        if node is None:
            return Node(value, height=1)

        if value < node.value:
            node.left = self._insert(node.left, value)
            node.left.parent = node
        else:
            node.right = self._insert(node.right, value)
            node.right.parent = node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance_factor = self._get_balance_factor(node)

        if balance_factor > 1:
            if value < node.left.value:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

        if balance_factor < -1:
            if value > node.right.value:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def _remove(self, node: Optional[Node], value: int) -> Optional[Node]:
        if node is None:
            return node

        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self._get_min_value_node(node.right)
            node.value = temp.value
            node.right = self._remove(node.right, temp.value)

        if node is None:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance_factor = self._get_balance_factor(node)

        if balance_factor > 1:
            if self._get_balance_factor(node.left) >= 0:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

        if balance_factor < -1:
            if self._get_balance_factor(node.right) <= 0:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def _search(self, node: Optional[Node], value: int) -> Optional[Node]:
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def _get_height(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return node.height

    def _get_balance_factor(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z: Node) -> Node:
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z: Node) -> Node:
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_min_value_node(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current
