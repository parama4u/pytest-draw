import unittest
from parameterized import  parameterized
class Test(unittest.TestCase):

    @parameterized.expand(["1","2","3","4","5","6","7","8","9","10"])
    def test(self,name):
        assert True
