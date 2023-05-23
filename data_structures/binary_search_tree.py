from dataclasses import dataclass
from typing import Optional
from data_structures.nodes import Node

@dataclass
class BinarySearchTree:
    root: Optional[Node] = None

    # def insert(self, value: int):
    #     ...

    def insert(self, value: int):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: Node, value: int):
        if value <= node.value:
            if node.left is None:
                new_node = Node(value)
                node.left = new_node
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                new_node = Node(value)
                node.right = new_node
            else:
                self._insert_recursive(node.right, value)

    def remove(self, value: int):
        ...

    @staticmethod
    def from_list(values: list[int]):
        tree = BinarySearchTree()
        for v in values:
            tree.insert(v)
        return tree

    # --------------------
    # Metodos da atividade
    # --------------------
    def imprimeArvore(self, s: int) -> str:
        def to_string1(node: Node) -> str:
            return ""

        def to_string2(node: Node) -> str:
            left = to_string2((node.left)) if node.left else ''
            right = to_string2((node.right)) if node.right else ''
            if not left and not right:
                return f'({node.value})'
            else:
                return f'({node.value} {left} {right})'

        funcao = to_string1 if s == 1 else to_string2
        impressao = funcao(self.root)
        print(impressao)
        return impressao

    def enesimoElemento(self, n: int) -> int:
        ...

    def posicao(self, x: int) -> int:
        ...

    def mediana(self) -> int:
        ...

    def media(self, x: int) -> float:
        ...

    def ehCheia(self) -> bool:
        return self._eh_cheia_recursiva(self.root)

    def _eh_cheia_recursiva(self, node: Node) -> bool:
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return (
                self._eh_cheia_recursiva(node.left) and
                self._eh_cheia_recursiva(node.right)
            )
        return False

    def ehCompleta(self) -> bool:
        if self.root is None:
            return True

        queue = []
        queue.append(self.root)
        has_gap = False

        while queue:
            current_node = queue.pop(0)

            if current_node.left:
                if has_gap:
                    return False
                queue.append(current_node.left)
            else:
                has_gap = True

            if current_node.right:
                if has_gap:
                    return False
                queue.append(current_node.right)
            else:
                has_gap = True

        return True


    def pre_ordem(self) -> str:
        ...

