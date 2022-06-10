from code_quality_scraper.constants import CODE_QUALITY_OUTPUT_ROOT_DIRECTORY

import unittest
from code_quality_scraper import utils


class UtilsTest(unittest.TestCase):
    def test_utils(self):
        utils.file_exists(CODE_QUALITY_OUTPUT_ROOT_DIRECTORY)
        pass


if __name__ == "__main__":
    unittest.main()
