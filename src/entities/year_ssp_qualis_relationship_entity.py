from dataclasses import dataclass
from typing import List

from .enums import QualisEnum
from .types import Issn


@dataclass
class YearSspQualisRelationshipEntity:
    """Represents the qualis classification for a Scientific Serial Publisher (SSP) on a specfic year."""

    year: int
    scientific_serial_publishers: List[Issn]
    qualis: QualisEnum

