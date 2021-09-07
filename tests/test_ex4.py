from tests.base import TestExercise

import exercises.ex4_1 as ex4_1
import exercises.ex4_2 as ex4_2
import exercises.ex4_3 as ex4_3
import exercises.ex4_4 as ex4_4
import exercises.ex4_5 as ex4_5
import exercises.ex4_6 as ex4_6
import exercises.ex4_7 as ex4_7
import exercises.ex4_8 as ex4_8
import exercises.ex4_9 as ex4_9


class TestExercise4(TestExercise):
    def test_ex4_1(self):
        cases = [
            ("0.0.0.0", "00000000.00000000.00000000.00000000"),
            ("192.168.1.1", "11000000.10101000.00000001.00000001"),
            ("208.67.222.222", "11010000.01000011.11011110.11011110"),
        ]

        self._test_all(ex4_1.solve, cases)

    def test_ex4_2(self):
        cases = [(0o644, 0o133), (0o755, 0o022)]
        self._test_all(ex4_2.solve, cases)

    def test_ex4_3(self):
        cases = [
            (
                ["knowledge", "hardwork", "discipline", "attitude"],
                [96, 98, 100, 100],
            )
        ]
        self._test_all(ex4_3.solve, cases)

    def test_ex4_4(self):
        self.assertEqual(ex4_4.solve(), 453542)

    def test_ex4_5(self):
        cases = [([1, 2, 3], (6, 6)), ([0, 1, 2], (3, 0))]

        self._test_all(ex4_5.solve, cases)

    def test_ex4_6(self):
        ss3 = "10 Bé học lớp 3 lên lớp 4"
        ss = ", 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu"
        ss2 = "6năm0 cuộc đời, 20 năm đầu, sung sướng0bao lâu"

        import re

        pattern = re.compile(r"\d+")

        def _solve(ss):
            return [int(i) for i in pattern.findall(ss)]

        cases = [(i, _solve(i)) for i in [ss, ss2, ss3]]

        self._test_all(ex4_6.solve, cases)

    def test_ex4_7(self):
        this, that, isgood = ex4_7.solve(1990, 1994)
        self.assertEqual("Canh Ngọ", this)
        self.assertEqual("Giáp Tuất", that)
        self.assertEqual(ex4_7.GOOD, isgood)

        this, that, isgood = ex4_7.solve(1987, 1990)
        self.assertEqual("Đinh Mão", this)
        self.assertEqual("Canh Ngọ", that)
        self.assertEqual(ex4_7.NEUTRAL, isgood)

    def test_ex4_8(self):
        result = ex4_8.solve()
        self.assertIn((6, 8, 10), result)
        self.assertEqual(len(result), 2)

    def test_ex4_9(self):
        cases = [([1, 3, 2], 3), ([42], 42)]
        self._test_all(ex4_9.solve, cases)
