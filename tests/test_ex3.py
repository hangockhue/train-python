import unittest
from tests.base import TestExercise

import exercises.ex3_0 as ex3_0
import exercises.ex3_1 as ex3_1
import exercises.ex3_2 as ex3_2
import exercises.ex3_3 as ex3_3
import exercises.ex3_4 as ex3_4
import exercises.ex3_5 as ex3_5
import exercises.ex3_6 as ex3_6
import exercises.ex3_7 as ex3_7
import exercises.ex3_8 as ex3_8
import exercises.ex3_9 as ex3_9
import exercises.ex3_10 as ex3_10


class TestExercise3(TestExercise):
    def test_ex3_0(self):
        res = ex3_0.squared(5)
        self.assertEqual(res, 25, self.MESSAGE_FMT.format(5, 25, res))

    def test_ex3_1(self):
        cases = [(1, 1), (5, 1), (9, 1), (24, 1000), (10, 10)]
        self._test_all(ex3_1.solve, cases)

    def test_ex3_2(self):
        text = "P\nY\nM\nI"
        self.assertEqual(ex3_2.solve(text), "Pymi")
        self.assertEqual(ex3_2.solve(ex3_2.data), "Crossmyheart")
        self.assertEqual(ex3_2.solve(ex3_2.data.lower()), "Crossmyheart")

    def test_ex3_3(self):
        res = ex3_3.solve()
        self.assertIsInstance(
            res, list, "Expect list, got: {0}".format(type(res))
        )
        self.assertEqual(
            len(res), len(range(1, 101)), "Số lượng phần tử không đúng"
        )
        cases = [(1, 1), (2, 2), (3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz")]
        for num, value in cases:
            msg = self.MESSAGE_FMT.format(num, value, res[num - 1])
            self.assertEqual(res[num - 1], value, msg)

    def test_ex3_4(self):
        cases = [
            ("....slsslslsls...sls", "....slsslslsls.."),
            ("maria.data.mp9", "maria.data"),
            ("baitap.py", "baitap"),
        ]
        self._test_all(ex3_4.solve, cases)

    def test_ex3_5(self):
        len_expected = len(ex3_5.data)
        res = ex3_5.solve(ex3_5.data)
        self.assertIsInstance(res, list)
        self.assertEqual(len(res), len_expected, "Số lượng phần tử không đúng")
        self.assertEqual(res[0][0], 1, "Index phần tử đầu tiên không đúng")
        self.assertEqual(
            res[-1][0], len_expected, "Index phần tử cuối cùng không đúng"
        )

    def test_ex3_6(self):
        res = ex3_6.solve(2)
        self.assertIsInstance(res, tuple)
        self.assertEqual(len(res), 2, "Số lượng phần tử không đúng")
        cases = [
            (1, ("January", 31)),
            (2, ("February", 28)),
            (3, ("March", 31)),
            (4, ("April", 30)),
            (7, ("July", 31)),
            (8, ("August", 31)),
            (9, ("September", 30)),
        ]
        for input_data, expect in cases:
            res = ex3_6.solve(input_data)
            msg = self.MESSAGE_FMT.format(input_data, expect, res)
            self.assertEqual(res, expect, msg)

    def test_ex3_7(self):
        len_expected = 19
        res = ex3_7.solve()
        self.assertEqual(len(res), len_expected, "Số lượng phần tử không đúng")
        self.assertEqual(res[0], "5 == 1 * 5", "Phần tử đầu tiên chưa đúng")
        self.assertEqual(res[-1], "95 == 19 * 5", "Phần tử cuối chưa đúng")

    def test_ex3_8(self):
        cases = [
            ("ana", True),
            ("Civic", True),
            ("Python", False),
            ("", False),
            ("nN", False),
            ("P", False),
            (" P  ", False),
            (" P ", False),
            ("Able was I ere I saw Elba", True),
        ]
        self._test_all(ex3_8.solve, cases)

    def test_ex3_9(self):
        len_expected = 23
        res = ex3_9.solve()
        msg = self.MESSAGE_FMT.format(None, len_expected, len(res))
        self.assertEqual(len(res), len_expected, "Số bộ không đủ: " + msg)
        self.assertEqual(res[0], [9, 1, 1], "Bộ số đầu tiên chưa chính xác")
        self.assertEqual(res[-1], [1, 9, 1], "Bộ số cuối cùng chưa chính xác")

    def test_ex3_10(self):
        for test, result in [
            (ex3_10.data, [0, 1]),
            (([3, 3], 6), [0, 1]),
            (([3, 2, 4], 6), [1, 2]),
        ]:
            res = ex3_10.solve(*test)
            self.assertEqual(res, result)


if __name__ == "__main__":
    unittest.main()
