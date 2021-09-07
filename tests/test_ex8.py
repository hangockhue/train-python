import unittest
from tests.base import TestExercise

import configparser
import os
import sys
import tempfile

# hack path for importing exercises.log
sys.path.insert(
    1, os.path.abspath(os.path.join(sys.path[0], "exercises"))
)  # NOQA

import exercises.ex8_1 as ex8_1  # NOQA
import exercises.ex8_2 as ex8_2  # NOQA
import exercises.ex8_3 as ex8_3  # NOQA
import exercises.ex8_4 as ex8_4  # NOQA
import exercises.ex8_5 as ex8_5  # NOQA
import exercises.ex8_8 as ex8_8  # NOQA
import exercises.ex8_9 as ex8_9  # NOQA


class TestExercise8(TestExercise):
    @unittest.skip
    def test_ex8_0(self):
        pass

    def test_ex8_1(self):
        N = 3
        times, total_time = ex8_1.solve(N)
        self.assertEqual(
            len(times), N, "Chưa thực hiện đủ số lần in ra màn hình"
        )
        self.assertLessEqual(N, total_time)

    def test_ex8_2(self):
        conf = configparser.ConfigParser()
        conf.read(os.path.join(os.path.dirname(__file__), "../setup.cfg"))
        n = conf.getint("flake8", "max-line-length")

        res = ex8_2.solve("-h", __file__)
        self.assertEqual(n, len(res), "Số lượng phần tử không đúng")
        with open(__file__) as f:
            line = f.readline()
        self.assertEqual(line.strip(), res[0].strip())

        _, fn = tempfile.mkstemp()
        with open(fn, "w") as f:
            for i in range(100):
                f.write(str(i) + "\n")
        last_n_lines = []
        with open(fn) as f:
            for line in f:
                last_n_lines.append(line)
                if len(last_n_lines) > n:
                    last_n_lines.pop(0)
        res = ex8_2.solve("-t", fn)
        self.assertEqual(last_n_lines, res)

    def test_ex8_3(self):
        res = ex8_3.solve(ex8_3.data)
        self.assertEqual(
            len(res), len(ex8_3.data), "Số lượng phần tử không đúng"
        )
        self.assertEqual(res[0], ex8_3.data[0].upper())

    def test_ex8_4(self):
        timer_res = ex8_4.solve()
        self.assertGreater(timer_res, 1.0)

    def test_ex8_5(self):
        test_res = ex8_5.solve()
        self.assertTrue(test_res, "unittest in this exercise has been failed.")

    def test_ex8_8(self):
        cases = [
            ("02/03/16", "0.3.1"),
            ("09/06/16", "8.2.0"),
            ("06/23/17", "18.3.3"),
        ]

        self._test_all(ex8_8.solve, cases)

    def _total_line_suffix(self, path):
        """
        :param path: path folder
        :rtype dict:
        """
        file_suffix = {}
        for root, _, files in os.walk(path):
            for file in files:
                path_file = os.path.join(root, file)
                _suffix = path_file[path_file.rfind(".") :]
                if not _suffix:
                    continue
                if _suffix not in file_suffix:
                    file_suffix.update({_suffix: 0})

                try:
                    with open(file) as f:
                        file_suffix[_suffix] += sum(1 for _ in f)
                except IOError:
                    continue

        return file_suffix

    def test_ex8_9(self):
        expected = self._total_line_suffix(ex8_9.PATH)
        res = ex8_9.solve(ex8_9.PATH)
        self.assertEqual(
            expected, res, self.MESSAGE_FMT.format(ex8_9.PATH, expected, res)
        )

    @unittest.skip
    def test_ex8_10(self):
        pass


if __name__ == "__main__":
    unittest.main()
