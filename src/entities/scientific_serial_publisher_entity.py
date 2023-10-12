from dataclasses import dataclass

from entities.types import Issn


@dataclass
class ScientificSerialPublisherEntity:
    """Represents a unique scientific publisher, such as journals, magazines, conferences etc."""

    issn: Issn
    name: str
