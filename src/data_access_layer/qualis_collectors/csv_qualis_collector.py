from typing import List
import pandas

from report_parameters import ReportParameters

from .interface_qualis_collector import IQualisCollector
from entities.scientific_serial_publisher_entity import Qualis


class CsvQualisCollector(IQualisCollector):
    """Gets Qualis data from a CSV file."""

    def collect(self, report_parameters: ReportParameters) -> List[Qualis]:
        return pandas.read_csv('./static/qualis.csv')
