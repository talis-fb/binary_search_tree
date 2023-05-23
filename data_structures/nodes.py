from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    value: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None
    height: int = 0
