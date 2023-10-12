from typing import Dict, List
from data_access_layer.researchers_collectors import IReserchersCollector
from entities import ResearcherEntity
from report_parameters import ReportParameters


class ScrapperResearchersCollector(IReserchersCollector):
    """Gets EIC reaserchers scrapping the eic web site.
    
    https://eic.cefet-rj.br/lattes/ppcic-YYYY/membros.html
    """

    def collect(self, report_parameters: ReportParameters) -> Dict[int, List[ResearcherEntity]]:
        year_researchers_dict = {}
        years = range(report_parameters.start_date.year, report_parameters.end_date.year + 1)

        for year in years:
            researchers = self._get_researchers(year)
            year_researchers_dict[year] = researchers

        print(years)