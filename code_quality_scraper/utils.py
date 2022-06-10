import logging
import re
from pathlib import Path
from datetime import datetime
from string import digits


def get_string_rep_from_map(list_of_tuples):
    answer = ""
    for tuple in list_of_tuples:
        answer += str(tuple[1]) + " : " + tuple[0] + "\n"
    return answer


def get_tuple_list_sorted_by_value(string_to_int_map):
    return sorted(string_to_int_map.items(), key=lambda x: x[1], reverse=True)


def only_non_digits(some_string):
    remove_digits = some_string.maketrans("", "", digits)
    return some_string.translate(remove_digits)


def get_only_digits(some_string):
    numeric_filter = filter(str.isdigit, some_string)
    numeric_string = "".join(numeric_filter)
    return int(numeric_string)


def file_exists(file_relative_path):
    return Path(file_relative_path)


def log_error(error_instance, message):
    logging.error(
        {
            "log_time": datetime.utcnow(),
            "error_instance_type": type(error_instance),
            "error_instance_args": error_instance.args,
            "error_instance": error_instance,
        }
    )


def log_warning(message):
    logging.warning(
        {
            "log_time": datetime.utcnow(),
            "warning_message": message,
        }
    )
