from abc import ABC, abstractmethod

from entities.researcher_entity import ResearcherEntity
from report_parameters import ReportParameters


class IReserchersCollector(ABC):
    """Public interface for reserchers collectors."""

    @abstractmethod
    def collect(self, report_parameters: ReportParameters) -> ResearcherEntity:
        """Extracts reserchers data from an external source."""
        raise NotImplementedError
