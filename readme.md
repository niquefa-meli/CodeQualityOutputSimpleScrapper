# Python scrapper to check CodeQuality Report in local directory

To the first commit, the project successfully scarp all the `*.java.html` files in the `code_quality_output_folder` example code quality output. Note: the `code_quality_output_folder` folder is included in the .gitignore file, but there is where the program will search for files with suffix `SUFFIX_TO_DETECT = ".java.html"`

# Python version

This repository is made in Python 3.6.13 and pip3 (version 22.1.2). Make sure you have those installed in your system.

## Use virtual environment
* A good idea for this project, is to use a virtual environment, you could set up one with: [virtualenv](https://virtualenv.pypa.io/en/latest/).
* To create the virtual environment: `virtualenv env`
* To activate it:`source env/bin/activate`
* To install dependencies: `pip3 install -r requirements.txt`
* To deactivate the virtual environment run `deactivate`

## Running the program

After being in the virtual environment and installing all dependencies, to run de program simply run `python3 run.py`. This should look something like:

`(venv) ➜  PythonCodeQualityScraper git:(main) python3 run.py`


## Unit testing and test coverage
To check the test coverage, run `coverage run  -m unittest discover -v` and then run `coverage report`.

Last coverage report run result:

```
Name                                Stmts   Miss  Cover
-------------------------------------------------------
code_quality_scraper/constants.py       3      0   100%
code_quality_scraper/utils.py          25     12    52%
test/__init__.py                        0      0   100%
test/test_utils.py                      9      1    89%
-------------------------------------------------------
TOTAL                                  19      3    84%
```

## Black Prettier

This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.

## Contribution

All MeLi contribution are welcome. Make sure to test everything and run `black . -l 120` before making any pull request. 
