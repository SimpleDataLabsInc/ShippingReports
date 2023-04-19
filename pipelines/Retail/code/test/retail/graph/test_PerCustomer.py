from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from retail.graph.PerCustomer import *
from retail.config.ConfigStore import *


class PerCustomerTest(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/retail/graph/PerCustomer/in0/schema.json',
            'test/resources/data/retail/graph/PerCustomer/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfIn1 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/retail/graph/PerCustomer/in1/schema.json',
            'test/resources/data/retail/graph/PerCustomer/in1/data/test_unit_test_0.json',
            'in1'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/retail/graph/PerCustomer/out/schema.json',
            'test/resources/data/retail/graph/PerCustomer/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed = PerCustomer(self.spark, dfIn0, dfIn1)

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        Utils.initializeFromArgs(
            self.spark,
            Namespace(
              file = f"configs/resources/config/{fabricName}.json",
              config = None,
              overrideJson = None,
              defaultConfFile = None
            )
        )
