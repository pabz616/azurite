# azurite

### Structure
The automation framework is built upon PyTest and consists of the following file structure:

* venv - the virtual environment that features all the necessary libraries used by the test framework (included)
* ./drivers - houses chrome and firefox (gecko) drivers for testing in different browsers (default= chrome)
* ./locators/page_elements - where the element identifiers are located
* ./pages- where the functions are
* ./results - where test reports, screenshots, etc. will go
* ./tests - self-explanatory
* ./utils - holds test data
* conftest.py - holds the configurations for the framework (browser options, resize window, etc.)
* pytest.ini - initial file that gets looked at when a test is started; where custom pytest marks are located

### Setup
```
Set up environment in PyCharm IDE (Professional / Community)
https://www.jetbrains.com/pycharm/download/

update 3/30/22
If using VS Code: visit https://code.visualstudio.com/docs/python/python-tutorial and follow the instructions
```
### Foundational Requirements
```
1. install homebrew: /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
- Run these two commands in your terminal to add Homebrew to your PATH:
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/pablovergara/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
- Run brew help to get started
2. brew install python3
3. brew cask install chromedriver
4. pip3 install virtualenv
5. virtualenv -p python3 venv
6. pip3 install -r requirements.txt
```
### Test Runs in Chrome
By default, the tests run headless in chrome. To open the browser, just enter the following command in the terminal:
```bash
$ pytest tests/ --browser=chrome
$ pytest test_name.py --browser=chrome
```
### Test with Reporting
requires: pytest-html
```
pytest tests/ -v -m custom_tag --html=results/TestName_Test_Results_custom_identifier.html --self-contained-html
```
