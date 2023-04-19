import unittest

from test.retail.graph.test_PerCustomer import *
from test.retail.graph.test_TotalByCustomer import *

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite())
