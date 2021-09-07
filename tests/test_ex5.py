from tests.base import TestExercise

import exercises.ex5_1 as ex5_1
import exercises.ex5_2 as ex5_2
import exercises.ex5_3 as ex5_3
import exercises.ex5_4 as ex5_4
import exercises.ex5_5 as ex5_5
import exercises.ex5_6 as ex5_6
import exercises.ex5_7 as ex5_7
import exercises.ex5_8 as ex5_8
import exercises.ex5_9 as ex5_9


class TestExercise5(TestExercise):
    def test_ex5_1(self):
        res = ex5_1.solve(ex5_1.data)
        self.assertEqual(
            len(res), len("Google"), "Kết quả không đủ các chữ cái"
        )
        self.assertEqual(res[0], ("G", "#4885ed"), "Sai màu")

    def test_ex5_2(self):
        hoang, duy, dai, tu = ex5_2.data
        res = ex5_2.solve(ex5_2.data[::-1])
        self.assertIsInstance(res, list)
        self.assertNotIn("languages", duy)

        ns = {}
        for i in res:
            ns.update({i["name"]: i})

        newhoang, newduy, newdai, newtu = (
            ns["Hoang"],
            ns["Duy"],
            ns["Dai"],
            ns["Tu"],
        )

        self.assertEqual(hoang["languages"], newduy["languages"])
        self.assertEqual(hoang["languages"], newdai["languages"])
        self.assertEqual(hoang["languages"], newtu["languages"])
        self.assertIn("Elixir", newhoang["languages"])
        self.assertEqual(newtu["girl_friend"], "Do Anh")
        self.assertNotIn("girl_friend", newduy)

    def test_ex5_3(self):
        res = ex5_3.solve(ex5_3.data)
        self.assertEqual(10, len(res), "Không đủ 10 phần tử")
        self.assertIn(
            ("be", 5), res, "Không tìm thấy cặp ('be', 5) trong kết quả"
        )
        self.assertIn(
            ("can", 4), res, "Không tìm thấy cặp ('can', 4) trong kết quả"
        )

    def test_ex5_4(self):
        expected = [
            "111111111111111111111111111111\n",
            "4\n",
            "111111111111111111111111111111\n",
            "8\n",
            "111111111111111111111111111111\n",
            "12\n",
            "111111111111111111111111111111\n",
            "16\n",
            "111111111111111111111111111111\n",
            "20\n",
            "111111111111111111111111111111\n",
            "59999984\n",
            "111111111111111111111111111111\n",
            "59999988\n",
            "111111111111111111111111111111\n",
            "59999992\n",
            "111111111111111111111111111111\n",
            "59999996\n",
            "111111111111111111111111111111\n",
            "60000000\n",
        ]
        import tempfile

        _, fn = tempfile.mkstemp()
        self.assertEqual(ex5_4.solve(fn), expected)

    def test_ex5_5(self):
        res = ex5_5.solve(ex5_5.datafile)
        msv, name, year, room = res[0]
        self.assertLess(
            msv,
            ex5_5.MAGIC_NUMBER,
            "Mã sinh viên phải nhỏ hơn số MAGIC_NUMBER",
        )
        self.assertEqual(year, 1990, "Các học viên phải có năm sinh là 1990")
        self.assertEqual(
            [("Dai", 5), ("Dung", 5), ("Duong", 5)],
            [(e[1], e[-1]) for e in res[:3]],
        )

    def test_ex5_6(self):
        term1, term2 = ex5_6.data
        res = ex5_6.solve(term1, term2)
        self.assertIsInstance(res, dict)
        self.assertEqual(res["python"], 9)
        self.assertEqual(res["math"], 7)
        self.assertEqual(res["data"], 2)

    def test_ex5_7(self):
        cases = [
            ("a", "a"),
            ("aa", "aa2"),
            ("abbbccccdddd", "abb3cc4dd4"),
            ("xxyyyxyyx", "xx2yy3xyy2x"),
        ]
        self._test_all(ex5_7.solve, cases)

    def test_ex5_8(self):
        ascii_, _, tabcp, newlinecp, spacecp = ex5_8.solve()
        self.assertEqual(ascii_[:3], [(33, "!"), (34, '"'), (35, "#")])
        self.assertEqual(
            ascii_[-4:], [(49, "1"), (50, "2"), (51, "3"), (52, "4")]
        )
        self.assertEqual(tabcp, ord("\t"))
        self.assertEqual(spacecp, ord(" "))
        self.assertEqual(newlinecp, ord("\n"))

    def test_ex5_9(self):
        start_with_h, more_than_1mil = ex5_9.solve(ex5_9.data)
        self.assertEqual(
            start_with_h[-2:], [("Hải Phòng", 1904100), ("Hậu Giang", 769700)]
        )
        self.assertEqual(
            more_than_1mil[:2],
            [("TP. Hồ Chí Minh", 7681700), ("Hà Nội", 6844100)],
        )
