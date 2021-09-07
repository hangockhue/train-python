from tests.base import TestExercise

import exercises.ex35_1 as ex35_1
import exercises.ex35_2 as ex35_2
import exercises.ex35_3 as ex35_3
import exercises.ex35_4 as ex35_4
import exercises.ex35_5 as ex35_5
import exercises.ex35_6 as ex35_6
import exercises.ex35_7 as ex35_7
import exercises.ex35_8 as ex35_8
import exercises.ex35_9 as ex35_9


class TestExercise35(TestExercise):
    def test_ex35_1(self):
        result = ex35_1.solve(10)
        self.assertEqual(len(result), 10)
        self.assertEqual(list(set(result))[0], 2)

    def test_ex35_2(self):
        result = ex35_2.solve(5)
        self.assertEqual(len(result), 5)
        new_result = ex35_2.solve(5)
        # They are random, should be different
        self.assertNotEqual(result, new_result)
        self.assertIn(result[0], range(0, 10))

        # do the same with 10
        result = ex35_2.solve(10)
        self.assertEqual(len(result), 10)
        new_result = ex35_2.solve(10)
        self.assertNotEqual(result, new_result)

    def test_ex35_3(self):
        result = ex35_3.solve(10)
        self.assertEqual(result[:2], [2, 4])
        self.assertEqual(len(result), 10)

    def test_ex35_4(self):
        result = ex35_4.solve(5)
        self.assertEqual(len(result), 5)
        new_result = ex35_4.solve(5)
        self.assertNotEqual(result, new_result, "Output should be random")

    def test_ex35_5(self):
        result = ex35_5.solve(12)
        self.assertEqual(result[-1], "111111111111")
        self.assertEqual(result[0], "111111")

    def test_ex35_6(self):
        result = ex35_6.solve(1000)
        self.assertEqual(result, sum(int(i) for i in str(2 ** 1000)))

    def test_ex35_7(self):
        result = ex35_7.solve(10)
        self.assertEqual(result, 23)
        result = ex35_7.solve(1000)
        self.assertEqual(result, 233168)

    def test_ex35_8(self):
        result = ex35_8.solve(10)
        self.assertEqual(result[:2], "0*")
        self.assertEqual(result[-2:], "*9")

        N = 10
        matrix = [list(range(N)) for i in range(N)]
        for rowidx, row in enumerate(matrix):
            for idx, _ in enumerate(row):
                if idx == rowidx or idx == N - rowidx - 1:
                    row[idx] = str(rowidx)
                else:
                    row[idx] = "*"
        matrix = "\n".join(["".join(line) for line in matrix])

        self.assertEqual(result, matrix)

    def test_ex35_9(self):
        res = ex35_9.solve(([], ""))
        self.assertIsInstance(res, list)
        self.assertIn("__setitem__", res)
        self.assertNotIn("extend", res)
