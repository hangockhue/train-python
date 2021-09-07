import unittest


class TestExercise(unittest.TestCase):
    MESSAGE_FMT = "Đầu vào: {0!r} - Kết quả đúng là {1!r}, nhận được {2!r}"

    def _test_all(self, func, cases):
        for input_, expect in cases:
            output = func(input_)
            msg = self.MESSAGE_FMT.format(input_, expect, output)
            self.assertEqual(output, expect, msg)
