from dataclasses import dataclass
from typing import List
from uuid import UUID

from entities.types import Issn


@dataclass
class PublishedWorkEntity:
    """Represents a published scientific work."""

    id: UUID
    title: str
    authors: List[str]
    year: int
    publisher_issn: Issn
