from abc import ABC, abstractmethod
from typing import Dict, List

from entities.student_entity import StudentEntity


class IStudentsCollector(ABC):
    """Public interface for students collectors."""

    @abstractmethod
    def collect(self, years: List[int]) -> Dict[int, List[StudentEntity]]:
        """Extracts students data from an external source."""
        raise NotImplementedError
