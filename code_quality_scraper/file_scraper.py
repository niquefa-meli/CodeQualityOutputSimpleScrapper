from bs4 import BeautifulSoup
from code_quality_scraper import utils
from code_quality_scraper import validations
from code_quality_scraper.ScrapedFileDTO import ScrapedFileDTO


def process_file(file_path):
    with open(file_path, "r") as f:
        doc = BeautifulSoup(f, "html.parser")

    tags = doc.find_all("span")
    print("Processing file: " + file_path + ". span tags: " + str(len(tags)))

    if len(tags) > 1:

        issue_count = validations.validate_issue_count(file_path, tags)

        complexity = utils.get_only_digits(str(tags[1]))

        # print("There are " + str(issue_count) + " issues")
        # print("Complexity issues in file: " + str(complexity) + ".")

        issue_map = {}
        tag_number = 1
        for i in range(2, len(tags)):
            non_digits = utils.only_non_digits(str(tags[i].get_text()))
            # print(str(tag_number) + "\t" + str(tags[i]) + "\n" + str(non_digits) + "\n")
            if non_digits in issue_map.keys():
                issue_map[non_digits] += 1
            else:
                issue_map[non_digits] = 1

            tag_number += 1

        return ScrapedFileDTO(file_path, complexity, issue_count, issue_map)
    return ScrapedFileDTO(file_path, 0, 0, {})
