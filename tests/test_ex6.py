import unittest

from tests.base import TestExercise

import exercises.ex6_1 as ex6_1
import exercises.ex6_2 as ex6_2
import exercises.ex6_3 as ex6_3
import exercises.ex6_4 as ex6_4
import exercises.ex6_5 as ex6_5
import exercises.ex6_6 as ex6_6
import exercises.ex6_7 as ex6_7


class TestExercise6(TestExercise):
    @unittest.skip
    def test_ex6_0(self):
        pass

    def test_ex6_1(self):
        expected = [
            ("Nam", "1,230"),
            ("Pikalong", "35,670"),
            ("Phan Quan", "2,165,110"),
            ("Maria", "90,570"),
            ("Trump", "138,000"),
        ]
        len_expected = len(expected)
        res = ex6_1.solve(
            {
                "usages": [
                    ("nam", "1"),
                    ("pikalong", "29"),
                    ("phan quan", "1235"),
                    ("maria", "69"),
                    ("trump", "100"),
                ],
                "prices": ex6_1.data,
            }
        )
        self.assertIsInstance(res, list)
        self.assertEqual(len(res), len_expected, "Số lượng phần tử không đúng")
        self.assertEqual(res, expected)

    def test_ex6_2(self):
        data = ["meo", "bo", "ga", "cho", "chim", "gau", "voi"]
        # https://docs.python.org/3/library/functions.html#zip
        expected = list(zip(*[iter(data)] * 2))
        res = ex6_2.solve(data, 2)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], tuple)
        self.assertEqual(res, expected)

        self.assertEqual(ex6_2.solve(data, 3), list(zip(*[iter(data)] * 3)))

    def test_ex6_3(self):
        expected = ("2017-05-25", 76454277.83)
        res = ex6_3.solve()
        self.assertEqual(res, expected)

    def test_ex6_4(self):
        res = ex6_4.solve()
        expected = sum(range(1, 7)) + 0.5, sum(range(1, 7)) + 9 + 0.5

        self.assertEqual(res, expected)

    def test_ex6_5(self):
        res = ex6_5.solve(ex6_5.data)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], dict)

        self.assertIn("hvnsweeting", [n["login"] for n in res])

        self.assertIn(
            "https://github.com/thedrow", [n["html_url"] for n in res]
        )
        self.assertIn(
            "https://github.com/hvnsweeting", [n["html_url"] for n in res]
        )

    def test_ex6_6(self):
        res = ex6_6.solve("pallets")
        self.assertIn("flask", res)

    def test_ex6_7(self):
        prefix = (
            "       1       1     0o1     0x1\n"
            "       2      10     0o2     0x2\n"
        )
        suffix = (
            "      18   10010    0o22    0x12\n"
            "      19   10011    0o23    0x13\n"
        )
        res = ex6_7.solve(range(1, 20))

        self.assertEqual(prefix, res[: len(prefix)])
        self.assertEqual(suffix, res[-len(suffix) :])

    @unittest.skip
    def test_ex6_10(self):
        pass


if __name__ == "__main__":
    unittest.main()
