import unittest

from calculate_tip import calculate_bill_and_tip

class TestTipCalculator(unittest.TestCase):
    """
    Tests tip calculator.
    """

    def test_bill_tip(self):
        bill = 100.0
        tip_percentage = 15
        info = calculate_bill_and_tip(bill, tip_percentage)

        self.assertEqual(info[0], 115.0)
        self.assertEqual(info[1], 15.0)

    def test_bill_tip2(self):
        bill = 123.0
        tip_percentage = 17.0
        info = calculate_bill_and_tip(bill, tip_percentage)

        self.assertEqual(info[0], 143.91)
        self.assertEqual(info[1], 20.91)

unittest.main()