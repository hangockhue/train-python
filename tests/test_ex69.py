import unittest
from tests.base import TestExercise

import exercises.ex69_1 as ex69_1
import exercises.ex69_2 as ex69_2
import exercises.ex69_3 as ex69_3


class TestExercise69(TestExercise):
    def test_ex69_1(self):
        res = ex69_1.solve(range(10))
        self.assertIsInstance(res, list)
        self.assertEqual(res, [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_ex69_2(self):
        res = ex69_2.solve(range(10))
        self.assertIsInstance(res, list)
        self.assertEqual(res, [1, 3, 5, 7, 9])

    def test_ex69_3(self):
        res = ex69_3.solve(range(1, 6))
        self.assertIsInstance(res, int)
        self.assertEqual(res, 120)


if __name__ == "__main__":
    unittest.main()
