import unittest

# import selected elements, ex.:
from src.TrendLocator import *


class TestTrendLocator(unittest.TestCase):
    def test_trend_locator(self):
        trend_locator = TrendLocator()
        trends = trend_locator.get_trends()
        self.assertEqual(len(trends), 10)