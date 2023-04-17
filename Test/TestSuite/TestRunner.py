from unittest import TestLoader, TestSuite, TextTestRunner
from Pytest_Page_Object_Model.Test.Scripts.test_Home_Page import Google_HomePage
from Pytest_Page_Object_Model.Test.Scripts.test_Google_Search import Google_Search

import testtools as testtools

if __name__ == "__main__":
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(Google_HomePage),
        test_loader.loadTestsFromTestCase(Google_Search),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
