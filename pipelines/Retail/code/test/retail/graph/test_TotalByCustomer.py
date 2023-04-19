from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from retail.graph.TotalByCustomer import *
from retail.config.ConfigStore import *


class TotalByCustomerTest(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/retail/graph/TotalByCustomer/in0/schema.json',
            'test/resources/data/retail/graph/TotalByCustomer/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/retail/graph/TotalByCustomer/out/schema.json',
            'test/resources/data/retail/graph/TotalByCustomer/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed = TotalByCustomer(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select("customer_id", "first_name", "last_name", "amounts"),
            dfOutComputed.select("customer_id", "first_name", "last_name", "amounts"),
            self.maxUnequalRowsToShow
        )

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
