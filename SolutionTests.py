import unittest

from Solution import Solution


class TestSolutionSort(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_standard(self):
        # Test a standard package: not bulky and not heavy
        self.assertEqual(self.solution.sort(50, 50, 50, 10), "STANDARD")

    def test_bulky_edge_case_volume(self):
        # Test a bulky package based on volume exactly at 1,000,000 cm³
        self.assertEqual(self.solution.sort(100, 100, 100, 10), "SPECIAL")
        # Test a package just below bulky volume threshold
        self.assertEqual(self.solution.sort(99.99, 100, 100, 10), "STANDARD")

    def test_bulky_edge_case_dimensions(self):
        # Test a bulky package based on one dimension exactly at 150 cm
        self.assertEqual(self.solution.sort(150, 10, 10, 10), "SPECIAL")
        # Test a package just below the bulky dimension threshold
        self.assertEqual(self.solution.sort(149.99, 10, 10, 10), "STANDARD")

    def test_heavy_edge_case(self):
        # Test a heavy package with mass exactly at 20 kg
        self.assertEqual(self.solution.sort(50, 50, 50, 20), "SPECIAL")
        # Test a package just below the heavy mass threshold
        self.assertEqual(self.solution.sort(50, 50, 50, 19.99), "STANDARD")

    def test_rejected_both_conditions_met(self):
        # Test a package that is both bulky and heavy
        self.assertEqual(self.solution.sort(200, 200, 200, 25), "REJECTED")

    def test_bulky_and_heavy_edge_case(self):
        # Test a package exactly at bulky and heavy thresholds
        self.assertEqual(self.solution.sort(150, 150, 150, 20), "REJECTED")

    def test_large_volume_and_light(self):
        # Test a bulky package with large volume but light weight
        self.assertEqual(self.solution.sort(200, 200, 200, 10), "SPECIAL")

    def test_large_weight_and_small_dimensions(self):
        # Test a heavy package with small dimensions
        self.assertEqual(self.solution.sort(10, 10, 10, 25), "SPECIAL")

    def test_minimal_dimensions_and_mass(self):
        # Test a package with minimal dimensions and mass
        self.assertEqual(self.solution.sort(0.1, 0.1, 0.1, 0.1), "STANDARD")


if __name__ == '__main__':
    unittest.main()
