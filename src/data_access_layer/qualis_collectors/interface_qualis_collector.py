from abc import ABC, abstractmethod
from typing import Dict

from entities.scientific_serial_publisher_entity import Qualis
from report_parameters import ReportParameters


class IQualisCollector(ABC):
    """Public interface for qualis collectors."""

    @abstractmethod
    def collect(self, report_parameters: ReportParameters) -> Dict[str, Qualis]:
        """Returns a map issn to qualis."""
        raise NotImplementedError
