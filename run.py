from functools import total_ordering
import os
from code_quality_scraper import constants
from code_quality_scraper import file_scraper
from code_quality_scraper import utils


all_issues_map = {}

total_processes_files = 0
for dirpath, _, filenames in os.walk(constants.CODE_QUALITY_OUTPUT_ROOT_DIRECTORY):
    for f in filenames:
        file_to_process = os.path.abspath(os.path.join(dirpath, f))
        if file_to_process.endswith(constants.SUFFIX_TO_DETECT):
            scraped_file = file_scraper.process_file(file_to_process)
            total_processes_files += 1
            print(scraped_file)
            for key in scraped_file.issue_map:
                if key in all_issues_map.keys():
                    all_issues_map[key] += 1
                else:
                    all_issues_map[key] = 1


all_issues_map_tuple_list = utils.get_tuple_list_sorted_by_value(all_issues_map)

print(utils.get_string_rep_from_map(all_issues_map_tuple_list))

print("PROCESSED FILES : " + str(total_processes_files))
print("TOTAL ISSUES IN FILES : " + str(sum(all_issues_map.values())))
print("TOTAL ISSUE TYPES IN FILES : " + str(len(all_issues_map)))
