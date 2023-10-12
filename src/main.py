from pprint import pprint
from data_access_layer.students_collectors import CsvStudentsCollector
from report_parameters import ReportParameters


settings = {'startDate': '2017-02-15', 'endDate': '2018-02-15', 'score_weights': []}
ReportParameters.validate_parameters(settings)
report_parameters = ReportParameters(settings['startDate'], settings['endDate'], settings['score_weights'])

# # Data extractors
students = CsvStudentsCollector().collect([2022])
pprint(students)
# reserchers = get_researchers()
# published_works = get_published_works(reserchers)
# paper_qualis_dict = get_qualis(published_works)
# # save(students, ...)

# # load(students, ...)
# intermediate_report_representation = calculate_score(settings)
# # save(intermediate_report_representation)

# # load(intermediate_report_representation)
# json_report = export_json_report(intermediate_report_representation)
