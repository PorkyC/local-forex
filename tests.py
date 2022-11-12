import unittest
from datetime import datetime

from local_forex import ForexRates


class ForexData(unittest.TestCase):    
    def test_loaded_data(self):
        self.assertTrue(ForexRates().data)
    
    def test_get_rate(self):
        self.assertEqual(ForexRates().get_rate("USD", datetime(2020, 4, 1)), 1.4217)
    
    # 2020-04-05 is a Sunday and missing from data, so the rate returned should be from 2020-04-03 (1.4142)
    def test_specific_rate_not_found(self):
        self.assertEqual(ForexRates().get_rate("USD", datetime(2020, 4, 5)), 1.4142)

    def test_conversion(self):
        self.assertEqual(ForexRates().get_conversion_rate("USD", "EUR", datetime(2020, 4, 1)), 0.914982623246235)

if __name__ == "__main__":
    unittest.main()