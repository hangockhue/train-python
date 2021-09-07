defmodule Ex7Test do
  use ExUnit.Case

  test "71" do
    assert Ex71.solve(["1/3", "6/9"]) == 1.0
    assert Ex71.solve(["1/10", "1/10", "1/10"]) == 0.3
    assert Ex71.solve(["-1/10", "-1/10", "-1/10"]) == -0.3
  end

  test "72" do
    winner = Ex72.solve()
    assert winner.hp > 0
  end

  test "73" do
    assert Ex73.solve() == 4
  end

  test "74 RLE" do
    assert Ex74.solve("a") == "a"
    assert Ex74.solve("aa") == "aa2"
    assert Ex74.solve("abbbccccdddd") == "abb3cc4dd4"
    assert Ex74.solve("xxyyyxyyx") == "xx2yy3xyy2x"
    assert Ex74.rle2("abbbccccdddd") == "abb3cc4dd4"
    assert Ex74.rle2("xxyyyxyyx") == "xx2yy3xyy2x"
  end

  test "75" do
    assert Ex75.solve(Enum) >= length(Enum.__info__(:functions)) + 3
  end

  test "76" do
    assert Enum.to_list(33..47) ++
             Enum.to_list(58..64) ++ Enum.to_list(91..96) ++ [123, 124, 125, 126] == [
             33,
             34,
             35,
             36,
             37,
             38,
             39,
             40,
             41,
             42,
             43,
             44,
             45,
             46,
             47,
             58,
             59,
             60,
             61,
             62,
             63,
             64,
             91,
             92,
             93,
             94,
             95,
             96,
             123,
             124,
             125,
             126
           ]

    pw = Ex76.solve(16)
    pw2 = Ex76.solve(16)
    assert String.length(pw) == 16
    assert pw != pw2
  end

  test "77" do
    res = Ex77.solve()
    assert length(res) == 3
    [head | _] = res
    {_, rank} = head
    assert rank > 0
    assert Enum.member?(res, {"Singapore", 4}) == true
  end
end
