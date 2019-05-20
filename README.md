# Selenium_Python_PyCharm_Sample_POM_project
Sample Page Object Model Project (booking.com taken as example)

## Introduction:
This is my demo project to show how Page Object Model can be implemented to build simple framework for website test automation.
I chose booking.com website as not so complicated but still "real life" example.

## Prerequisites:
- Python 3.7.3
- Selenium 3.141.0
- Webdriver for browser you would like to use
- html-testRunner 1.2
- JetBrains PyCharm Community Edition 2019.1.1 (optional but strongly recommended)

## Installing:
- Python installation package can be download from [here](https://www.python.org/downloads/) - remember to choose option "Add to PATH" during instalation
- Instructions for Selenium and Webdriver configuration are [here](https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium) - I recommend adding Selenium and Webdriver files to Python installation folder, otherwise PATH variable has to be set also for them 
- html-testRunner can be installed by simple command in cmd: `pip install html-testRunner`
- PyCharm is available [here](https://www.jetbrains.com/pycharm/download/)

## Running:
I've uploaded my whole project with its internal structure. It should be downloaded or created in same way. You can simply put it into you PyCharm PycharmProjects folder or wherever you want. "venv" folder is created by PyCharm as isolated Python environment.
I don't know how it will act when copied to someone else but it can be set up later in PyCharm or deleted when project is executed from cmd only.

*Steps to run:*

*CMD*:
1. *Go to Selenium Folder*
2. *Shift + right-click - click on "Open command window here" (It's "Otwórz okno polecenia tutaj" in Polish) to open cmd with current path selected*
3. *Type python and path to the file you want to execute (e.g. below) and press enter (only files from Tests and TestSuites folders should be executed):* 
```
...\Selenium>python Projects\SamplePOMProject_Booking_com\Tests\TestSearchResult.py
``` 

*PyCharm*
1. *Open Pycharm and Project*
2. *Right-click on file you want to run*
3. *Click on "Run..." or "Debug..."*

**Note: Tests can be run separately or as test suite but if you ran test file directly from PyCharm no report would be generated as there is line:**
```python
if __name__ == '__main__':
    folder = StaticMethods.report_folder()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=folder), verbosity=2)
```
**which means that test runner will be run only when file is executed directly from cmd. That doesn't apply to test suite file.**

**Example of report and automated screenshot:**

Report pass:
![Image](https://github.com/mmgawlowski/Selenium_Python_PyCharm_Sample_POM_project/blob/master/Selenium/Projects/SamplePOMProject_Booking_com/Reports/Reports20190519/Sample%20report%20pass.png?raw=true)

Report fail:
![Image](https://github.com/mmgawlowski/Selenium_Python_PyCharm_Sample_POM_project/blob/master/Selenium/Projects/SamplePOMProject_Booking_com/Reports/Reports20190519/Sample%20report%20failed.png?raw=true)

**Important Note: those reports are generated as HTML files. They use external sources for displaying result in right way so internet connection has to be available.** 

Sample screenshot:
![Image](https://github.com/mmgawlowski/Selenium_Python_PyCharm_Sample_POM_project/blob/master/Selenium/Projects/SamplePOMProject_Booking_com/Reports/Reports20190519/test_search_for_place_by_query%2020190519_205151.png?raw=true)

## Suggestions - to do list:
- HTMLTestRunner could be implemented instead of html-testRunner as it is more elegant for generation of test suites reports but it is not compatible with newer version of Python. There are people who work on that but their newest version is compatible only up to Python 3.5. Look [here](https://github.com/dash0002/HTMLTestRunner) for details.

- Test from TestSearchResult should be divided to smaller tests or soft assertion should be implemented but "softtest" package is not compatible with version of Python I used. Those assertion are dependent on each other so before dividing them I need to find a way to run them one by one, not parallel and skip them when earlier test fail.

- I want to add test case name to test name while creating screenshot.
Changing:
```python
def screen_shot(self):
        # This line allows addition of test name to the name of screenshot file.
        # I would use self.id() to get also Test Case name but it does't work when Test Case is loaded in Test Suite from different file...
        test_method_name = self._testMethodName
        for method, error in self._outcome.errors:
            if error:
                StaticMethods.save_screenshot_picture(self.driver, test_method_name)
```
to:
```python
def screen_shot(self):
        # This line allows addition of test name to the name of screenshot file.
        # I would use self.id() to get also Test Case name but it does't work when Test Case is loaded in Test Suite from different file...
        test_method_name = self._id()
        for method, error in self._outcome.errors:
            if error:
                StaticMethods.save_screenshot_picture(self.driver, test_method_name)
```
works fine but only for test cases directly executed and cannot be applied for test suites...

- I want to find a way to create additional report folder with name of executed file for better reports and screenshots organization. It is not easy to make them both being created in one folder.

- Code optimization.

## Authors:
- Maciek Gawłowski [LinkedIn](https://www.linkedin.com/in/maciek-gaw%C5%82owski-a69a9483/)

## Licence:
This project is licensed under the MIT License

## Acknowledgments:
This project would not have been created if I had not found inspirations and ideas from sources listed below:

- https://automatetheboringstuff.com/
- https://stackoverflow.com/
- https://atechnovel.com/2018/01/13/from-messy-automation-script-to-page-object-pattern-in-python/
- Youtube tutorials
- Python's and Selenium's documentation
- etc.



