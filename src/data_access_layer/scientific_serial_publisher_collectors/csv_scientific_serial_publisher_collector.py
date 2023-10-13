from typing import Dict, List, Set, Tuple
import pandas

from .interface_scientific_serial_publisher_collector import IScientificSerialPublisherCollector
from entities import ScientificSerialPublisherEntity
from entities.types import Issn
from entities.enums import QualisEnum


class CsvScientificSerialPublisherCollector(IScientificSerialPublisherCollector):
    """Gets ScientificSerialPublisher data from CSV files."""

    def collect(self, years: List[int]) -> Tuple[Dict[Issn, ScientificSerialPublisherEntity], Dict[int, Dict[QualisEnum, Set[Issn]]]]:
        ssp_dict = {}
        year_qualis_issn_dict = {year: {qualis.value: set() for qualis in QualisEnum} for year in years}

        for year in years:
            qualis_df = pandas.read_csv(f'./static_data/qualis/qualis-{year}.csv')

            for scientific_serial_publisher_dict in qualis_df.to_dict('records'):
                ssp = self._create_ssp_from_dict(scientific_serial_publisher_dict)
                qualis = scientific_serial_publisher_dict['Qualis']
                ssp_dict[ssp.issn] = ssp
                try:
                    year_qualis_issn_dict[year][qualis].add(ssp.issn)
                except:
                    year_qualis_issn_dict[year][QualisEnum.NOT_CLASSIFIED.value].add(ssp.issn)


        return ssp_dict, year_qualis_issn_dict

    @staticmethod
    def _create_ssp_from_dict(scientific_serial_publisher_dict: Dict) -> ScientificSerialPublisherEntity:
        return ScientificSerialPublisherEntity(
            issn=scientific_serial_publisher_dict['ISSN'],
            name=scientific_serial_publisher_dict['Nome'])
