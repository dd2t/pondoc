from abc import ABC, abstractmethod

from entities.published_work_entity import PublishedWorkEntity
from report_parameters import ReportParameters


class IPublishedWorksCollector(ABC):
    """Public interface for published works collectors."""

    @abstractmethod
    def collect(self, report_parameters: ReportParameters) -> PublishedWorkEntity:
        """Extracts published works data from an external source."""
        raise NotImplementedError
