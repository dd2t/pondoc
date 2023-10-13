from abc import ABC, abstractmethod
from typing import Dict, List, Set, Tuple

from entities import ScientificSerialPublisherEntity
from entities.types import Issn
from entities.enums import QualisEnum


class IScientificSerialPublisherCollector(ABC):
    """Public interface for qualis collectors."""

    @abstractmethod
    def collect(self, years: List[int]) -> Tuple[Dict[Issn, ScientificSerialPublisherEntity], Dict[int, Dict[QualisEnum, Set[Issn]]]]:
        """Returns a dictionary that maps ISSN to ScientificSerialPublisher and dictionary 
        that maps year to a dictionary QualisEnum to ISSNs."""
        raise NotImplementedError
