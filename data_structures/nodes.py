from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    value: int
    size: int = 1
    left: Optional['Node'] = None
    right: Optional['Node'] = None
    parent: Optional['Node'] = None

