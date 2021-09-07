defmodule Ex6Test do
  use ExUnit.Case
  doctest Pymi

  test "61" do
    usages = [
      {"nam", "1"},
      {"pikalong", "29"},
      {"phan quan", "1235"},
      {"maria", "69"},
      {"trump", "100"}
    ]

    prices = %{first_50: 1230, from_51_to_100: 1530, above_100: 1786}

    assert Ex61.solve(usages, prices) == [
             {"Nam", 1230},
             {"Pikalong", 35670},
             {"Phan Quan", 2_165_110},
             {"Maria", 90570},
             {"Trump", 138_000}
           ]
  end

  test "62" do
    assert Ex62.solve([]) == []
    assert Ex62.solve([1]) == []
    assert Ex62.solve([1, 2]) == [{1, 2}]
    assert Ex62.solve([1, 2, 3]) == [{1, 2}]
    assert Ex62.solve([1, 2, 3, 4]) == [{1, 2}, {3, 4}]
  end

  test "63" do
    assert Ex63.solve() == {"2017-05-25", 76_454_277.83}
  end

  test "64" do
    assert Ex64.solve([1, 2, 3, 4.0]) == 10
    assert Ex64.solve([1, 2, "3", 4]) == 10
    assert Ex64.solve([1, 2, "3", 4, "20"]) == 30
    assert Ex64.solve([1, 2, 3, 4.5, 5, 9, " 6  "]) == Enum.sum(1..6) + 9 + 0.5
  end

  test "65" do
    result = Ex65.solve()
    assert Enum.find(result, fn x -> x.login == "hvnsweeting" end) != nil

    assert Enum.find(result, fn x -> x.html_url == "https://github.com/thedrow" end) != nil

    assert Enum.find_value(result, fn x -> x.html_url == "https://github.com/hvnsweeting" end) ==
             true
  end
end
