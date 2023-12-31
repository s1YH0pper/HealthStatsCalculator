import unittest
from health_stats_calculator import *


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

    def test_classify_hypertension(self):
        self.assertEqual(classify_hypertension(130, 85), 'Stage 1 Hypertension')
        # Add more test cases for different inputs

    def test_calculate_max_aspartame_bottle(self):
        self.assertEqual(calculate_max_aspartame_bottle(70, 250), 11)
        # Add more test cases for different inputs

    def test_calculate_body_fat_percentage(self):
        self.assertAlmostEqual(calculate_body_fat_percentage('M', 70, 1.75, 30), 18.13, places=2)
        self.assertAlmostEqual(calculate_body_fat_percentage('F', 60, 1.6, 35), 30.77, places=2)
        # Add more test cases for different inputs


if __name__ == "__main__":
    unittest.main()
