from dataclasses import dataclass
from typing import Final


@dataclass
class Links:
    query: Final[str] = "query"
    position_num: Final[int] = "position_num"
    link: Final[str] = "link"
    link_title: Final[str] = "link_title"
