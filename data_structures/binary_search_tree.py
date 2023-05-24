from dataclasses import dataclass
from typing import Optional
from data_structures.nodes import Node
from collections import deque


@dataclass
class BinarySearchTree:
    root: Optional[Node] = None

    def _find_min(self, node: Node):
        while node.left is not None:
            node = node.left
        return node

    def _get_height(self, node: Node):
        if node is None:
            return -1
        return node.height

    def insert(self, value: int):
        if self.root is None:
            self.root = Node(value, height=0)
        else:
            self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return node

    def remove(self, value: int):
        self.root = self._remove_recursive(self.root, value)

    def _remove_recursive(self, node: Node, value: int):
        if node is None:
            return node
        if value < node.value:
            node.left = self._remove_recursive(node.left, value)
        elif value > node.value:
            node.right = self._remove_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_right = self._find_min(node.right)
            node.value = min_right.value
            node.right = self._remove_recursive(node.right, min_right.value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return node

    @staticmethod
    def from_list(values: list[int]):
        tree = BinarySearchTree()
        for v in values:
            tree.insert(v)
        return tree

    def get_height(self) -> int:
        def _calculate_height_recursive(node: Optional[Node]) -> int:
            if node is None:
                return 0

            left_height = _calculate_height_recursive(node.left)
            right_height = _calculate_height_recursive(node.right)

            return max(left_height, right_height) + 1
        
        return _calculate_height_recursive(self.root)

    def get_pre_ordem_list(self) -> list[int]:
        arr = []
        def _get_ordem_recursive(node: Optional[Node]):
            nonlocal arr

            if node is None:
                return

            arr.append(node.value)

            _get_ordem_recursive(node.left)
            _get_ordem_recursive(node.right)

        _get_ordem_recursive(self.root)

        return arr
    
    def node_by_value(self, x: int) -> Node:
        stack = deque()
        node: Node = self.root
        while stack or node:
            if node != None and node.value == x:
                break
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
        return node
    
    def get_sub_tree_pre_ordem(self, x: int):
        arr: list[int] = []
        def _get_ordem_recursive(node: Optional[Node]):
            nonlocal arr

            if node is None:
                return

            arr.append(node.value)

            _get_ordem_recursive(node.left)
            _get_ordem_recursive(node.right)
        
        node: Node = self.node_by_value(x)
        _get_ordem_recursive(node)
        return arr
       
    def get_ordem_simetrica(self, i:int=-1) -> list[int]:
        arr: list[int] = []
        stack = deque()
        node: Node = self.root
        while (stack or node) and i != 0:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                i -= 1
                arr.append(node.value)
                node = node.right
        return arr

    # --------------------
    # Metodos da atividade
    # --------------------
    def imprimeArvore(self, s: int) -> str:
        h = self.root.height
        def to_string1(node: Node, t: int=0) -> str:
            left = to_string1((node.left), t+1) if node.left else ''
            right = to_string1((node.right), t+1) if node.right else ''
            tab ="\t"
            line = "--------"
            new = f'{t*tab}{node.value}'
            if not left and not right:
                return f'{new}{(h-t+1)*line}\n'
            else:
                return f'{new}{(h-t+1)*line}\n{left}{right}'

        def to_string2(node: Node) -> str:
            left = to_string2((node.left)) if node.left else ''
            right = to_string2((node.right)) if node.right else ''

            if not left and not right:
                return f'({node.value})'
            else:
                return f'({node.value} {left} {right})'

        switch = {
            1: to_string1,
            2: to_string2
        }
        funcao = switch.get(s)

        saida_para_impressao = funcao(self.root)
        # print(saida_para_impressao)
        return saida_para_impressao

    def enesimoElemento(self, n: int) -> int:
        pre_ordem: list[int] = self.get_ordem_simetrica(n)
        return pre_ordem[-1]

    def posicao(self, x: int) -> int:
        ordem_simetrica: list[int] = self.get_ordem_simetrica()
        return ordem_simetrica.index(x) + 1
    
    def search(self, value: int) -> Node:
        return self._search_recursive(value, self.root)

    def _search_recursive(self, value: int, node: Node) -> Node:
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(value, node.left)
        return self._search_recursive(value, node.right)


    def mediana(self) -> int:
        ...

    def media(self, x: int) -> float:
        new_tree_pre_ordem = self.get_sub_tree_pre_ordem(x)
        return sum(new_tree_pre_ordem)/len(new_tree_pre_ordem)
        
    def ehCheia(self) -> bool:
        def _eh_cheia_recursiva(node: Optional[Node]) -> bool:
            if node is None:
                return True
            if node.left is None and node.right is None:
                return True
            if node.left is not None and node.right is not None:
                return (
                    _eh_cheia_recursiva(node.left) and
                    _eh_cheia_recursiva(node.right)
                )
            return False

        return _eh_cheia_recursiva(self.root)

    def ehCompleta(self) -> bool:
        def is_complete_recursive(node: Optional[Node], node_count: int) -> bool:
            if node is None:
                return True

            if node.right is None or node.left is None:
                if node.height + 1 < node_count:
                    return False

            return (is_complete_recursive(node.left,  node_count) and
                    is_complete_recursive(node.right, node_count))

        height_first_node = self.get_height() - 1
        return is_complete_recursive(self.root, height_first_node)

    def pre_ordem(self) -> str:
        pre_ordem_list = self.get_pre_ordem_list()
        return ' '.join(map(str, pre_ordem_list))
