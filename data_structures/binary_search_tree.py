from dataclasses import dataclass
from typing import Optional
from Nodes import Node

@dataclass
class BinarySearchTree:
    raiz: Optional['Node']

    def insert(self, value: int):
        ...

    def remove(self, value: int):
        ...

    # --------------------
    # Metodos da atividade
    # --------------------
    def enesimoElemento(self, n: int) -> int:
        ...

    def posicao(self, x: int) -> int:
        ...

    def mediana(self) -> int:
        ...

    def media(self, x: int) -> float:
        ...

    def ehCheia(self) -> bool:
        ...

    def ehCompleta(self) -> bool:
        ...

    def pre_ordem(self) -> str:
        ...

    def imprimeArvore(self, s: int) -> None:
        ...

