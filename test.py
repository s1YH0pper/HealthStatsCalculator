import unittest
from health_stats_calculator import calculate_bmi, calculate_bmr, calculate_max_heart_rate, assess_resting_heart_rate, get_expected_resting_heart_rate_range

class HealthStatsCalculatorTest(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)
        self.assertAlmostEqual(calculate_bmi(80, 1.80), 24.69, places=2)
        # Add more test cases for different inputs

    def test_calculate_bmr(self):
        self.assertAlmostEqual(calculate_bmr('M', 70, 175, 30), 1648.75, places=1)
        self.assertAlmostEqual(calculate_bmr('F', 60, 160, 35), 1264.0, places=1)
        # Add more test cases for different inputs

    def test_calculate_max_heart_rate(self):
        self.assertEqual(calculate_max_heart_rate(30), 190)
        self.assertEqual(calculate_max_heart_rate(40), 180)
        # Add more test cases for different inputs

    def test_assess_resting_heart_rate(self):
        self.assertEqual(assess_resting_heart_rate(70, 30), 'Normal')
        self.assertEqual(assess_resting_heart_rate(85, 30), 'High')
        # Add more test cases for different inputs

    def test_get_expected_resting_heart_rate_range(self):
        self.assertEqual(get_expected_resting_heart_rate_range(30), (60, 80))
        self.assertEqual(get_expected_resting_heart_rate_range(40), (65, 85))
        # Add more test cases for different inputs

if __name__ == '__main__':
    unittest.main()
