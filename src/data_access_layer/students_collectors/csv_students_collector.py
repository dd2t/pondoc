from uuid import uuid4
import pandas
from typing import Dict, List

from entities.student_entity import StudentEntity
from .interface_students_collector import IStudentsCollector


class CsvStudentsCollector(IStudentsCollector):
    """Gets students data from a CSV file."""

    def collect(self, years: List[int]) -> Dict[int, List[StudentEntity]]:
        year_students_dict = {}

        for year in years:
            students_df = pandas.read_csv(f'./static_data/students/students-{year}.csv')
            normalized_students_df = self._normalize_students_df(students_df)
            students_dicts = normalized_students_df.to_dict('records')
            year_students_dict[year] = [StudentEntity(uuid4().hex, student_dict['nome']) for student_dict in students_dicts]

        return year_students_dict

    def _normalize_students_df(self, students_df: pandas.DataFrame) -> pandas.DataFrame:
        copy_df = students_df.copy()
        copy_df['nome'] = students_df['nome'].str.upper()
        return copy_df
