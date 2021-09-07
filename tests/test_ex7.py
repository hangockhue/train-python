import unittest
from tests.base import TestExercise

import exercises.ex7_1 as ex7_1
import exercises.ex7_2 as ex7_2
import exercises.ex7_3 as ex7_3
import exercises.ex7_4 as ex7_4
import exercises.ex7_5 as ex7_5
import exercises.ex7_6 as ex7_6
import exercises.ex7_7 as ex7_7


class TestExercise7(TestExercise):
    def test_ex7_1(self):
        self.assertEqual(ex7_1.solve("1/3", "6/9"), 1.0)
        self.assertEqual(ex7_1.solve("1/10", "1/10", "1/10"), 0.3)

    def test_ex7_2(self):
        name, HP = ex7_2.solve(
            ex7_2.Fighter("PyMi", 100), ex7_2.Fighter("Foo", 100)
        )
        self.assertIn(name, ("PyMi", "Foo"))
        self.assertGreater(HP, 0)

    def test_ex7_3(self):
        res = ex7_3.solve()
        len_expected = 4
        self.assertEqual(res, len_expected, "Không đủ số phần tử")
        import json
        import os
        import pickle
        import yaml

        cwd = os.getcwd()
        current_dir = os.path.basename(cwd)
        if current_dir == "pyfml":
            fmt_path = "exercises/{}"
        elif current_dir == "test":
            fmt_path = "../exercises/{}"
        else:
            raise Exception("Please run test under pyfml directory")
        cases = ("event.json", "event.yaml", "event.pkl")
        for case in cases:
            print(fmt_path)
            self.assertTrue(
                os.path.exists(fmt_path.format(case)),
                "File {} không tồn tại".format(case),
            )

        with open(fmt_path.format("event.json")) as f:
            data = json.load(f)
        with open(fmt_path.format("event.yaml")) as f:
            out_yaml = yaml.safe_load(f)
            self.assertEqual(
                data, out_yaml, "Ghi dữ liệu vào file event.yaml chưa đúng"
            )
        with open(fmt_path.format("event.pkl"), "rb") as f:
            out_pkl = pickle.load(f)
            self.assertEqual(
                data, out_pkl, "Ghi dữ liệu vào file event.pkl chưa đúng"
            )

    @unittest.skip
    def test_ex7_4(self):
        import hashlib

        r = hashlib.md5(ex7_4.solve().encode()).hexdigest()
        self.assertEqual(
            r,
            "9fd583bca43a756b86dd74706afb24d8",
            "Đây không phải chủ mưu vụ án, "
            "kết quả bạn nhìn thấy đã được mã hóa.",
        )

    def test_ex7_5(self):
        import os

        result = ex7_5.solve()
        self.assertEqual(os.__file__, result[0])

    def test_ex7_6(self):
        import string

        res = ex7_6.solve(12)
        self.assertEqual(len(res), 12)
        self.assertTrue(
            all(
                [
                    any(map(lambda s: s.isdigit(), res)),
                    any(map(lambda s: s.islower(), res)),
                    any(map(lambda s: s.isupper(), res)),
                    any(map(lambda s: s in string.punctuation, res)),
                ]
            )
        )
        self.assertNotEqual(res, ex7_6.solve(12))

    def test_ex7_7(self):
        res = ex7_7.solve(ex7_7.data)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], tuple)
        self.assertIn(("Singapore", 4), res)


if __name__ == "__main__":
    unittest.main()
