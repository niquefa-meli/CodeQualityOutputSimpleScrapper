from code_quality_scraper import exceptions
from code_quality_scraper import utils
from code_quality_scraper.constants import SPANS_TAGS_TO_IGNORE


def validate_issue_count(file_path, tags):
    total_issues = utils.get_only_digits(str(tags[0]))
    total_counted_issues = len(tags) - SPANS_TAGS_TO_IGNORE
    if total_counted_issues != total_issues:
        error_message = (
            "In file "
            + str(file_path)
            + ", the issues in first span tag = "
            + str(total_issues)
            + " is different to the counted issues (counted span tags minus "
            + str(SPANS_TAGS_TO_IGNORE)
            + "), which is "
            + str(total_counted_issues)
        )
        raise exceptions.IssuesCountError(error_message)
    return total_counted_issues
