from unittest import TestCase

import BdayCalc

class TestZeller_function(TestCase):

    def test_zeller_function(self):
        self.assertEqual(zeller_function(3, 10, 1984), "Saturday")
        self.assertEqual(zeller_function(10, 19, 2017), "Thursday")
        self.assertEqual(zeller_function(10, 20, 2017), "Friday")
        self.assertEqual(zeller_function(7, 4, 1792), "Wednesday")
        self.assertEqual(zeller_function(12, 31, 1999), "Friday")
        self.assertEqual(zeller_function(1, 1, 2000), "Saturday")
