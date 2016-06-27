import unittest
from sattestdata import TestData


class Test(unittest.TestCase):

    #def setUp(self):
    #    self.testdata = TestData()
    #    self.path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sattestdata'))

    def test_list_data(self):
        self.assertEquals(TestData.list_scenes(), ['raster', 'vector'])
