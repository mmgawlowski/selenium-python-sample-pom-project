import unittest
import HtmlTestRunner
import os
import sys

# This line returns path to the folder contains this file, then adds to it "../../.." which means going three folders up to "Selenium".
# Finally whole path is marked as additional path for searching modules.
# That's unnecessary to import below modules when start script from command line.
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))

from Projects.SamplePOMProject_Booking_com.Tests.TestHomePage import TestHomePage
from Projects.SamplePOMProject_Booking_com.Tests.TestSearchResult import TestSearchResult
from Projects.SamplePOMProject_Booking_com.Templates.StaticMethods import StaticMethods

# Example suite method which load all tests from selected Test Cases.
def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestHomePage))
    suite.addTests(loader.loadTestsFromTestCase(TestSearchResult))
    return suite


report_file = StaticMethods.report_folder()

# Below code for execution of test suite by chosen Test Runner.
runner = HtmlTestRunner.HTMLTestRunner(output=report_file)
runner.run(suite())
