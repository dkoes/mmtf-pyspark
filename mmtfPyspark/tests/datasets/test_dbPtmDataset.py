#!/usr/bin/env python

import unittest
import pytest

from pyspark.sql import SparkSession

from mmtfPyspark.datasets import dbPtmDataset as pm
from mmtfPyspark.datasets.dbPtmDataset import PtmType


class DbPtmDatasetTest(unittest.TestCase):

    def setUp(self):
        self.spark = SparkSession.builder.master("local[*]") \
            .appName("DbPtmDatasetTest") \
            .getOrCreate()

    @pytest.mark.skip(reason="Webservice obsolete.")
    def test1(self):
        ds = pm.download_ptm_dataset(PtmType.S_LINKEDGLYCOSYLATION)
        self.assertGreater(ds.count(), 4)

    @pytest.mark.skip(reason="Webservice obsolete.")
    def test2(self):
        ds = pm.get_ptm_dataset()
        self.assertGreater(ds.count(), 900000)

    def tearDown(self):
        self.spark.stop()


if __name__ == '__main__':
    unittest.main()
