defmodule PymiTest do
  use ExUnit.Case
  doctest Pymi

  test "greets the world" do
    assert Pymi.hello() == :world
  end

  test "Part from last 1 of binary of 10 is 10" do
    assert Ex31.solve(10) == 10
  end

  test "Part from last 1 of binary of 9 is 1" do
    assert Ex31.solve(9) == 1
  end

  test "Print out result for from 1->9" do
    assert Ex31.main() == [
             {1, {"1", 1}},
             {2, {"10", 10}},
             {3, {"11", 1}},
             {4, {"100", 100}},
             {5, {"101", 1}},
             {6, {"110", 10}},
             {7, {"111", 1}},
             {8, {"1000", 1000}},
             {9, {"1001", 1}},
             {10, {"1010", 10}}
           ]
  end

  test "Ex32 " do
    data = """
    Come to the
    River
    Of my
    Soulful
    Sentiments
    Meandering silently
    Yearning for release.
    Hasten
    Earnestly
    As my love flows by
    Rushing through the flood-gates
    To your heart.
    """

    assert Ex32.solve(data) == "CROSSMYHEART"
    assert Ex32.solve("P\nY\nm\nI") == "PYMI"
  end

  test "Ex33 FizzBuzz" do
    cases =
      [{1, 1}, {2, 2}, {3, "Fizz"}, {5, "Buzz"}, {15, "FizzBuzz"}] |> Enum.map(fn {_, r} -> r end)

    result = Ex33.solve()
    rhs = [1, 2, 3, 5, 15] |> Enum.map(fn i -> Enum.at(result, i - 1) end)
    assert cases == rhs
  end

  test "Ex34 get filename remove ext with input '....slsslslsls...sls'" do
    assert Ex34.solve("....slsslslsls...sls") == "....slsslslsls.."
  end

  test "Ex34 get filename remove ext with input 'maria.data.mp9'" do
    assert Ex34.solve("maria.data.mp9") == "maria.data"
  end

  test "Ex35 elem with index" do
    assert Ex35.solve(["I", "Love", "You", "Chiu", "Chiu"]) == [
             [1, "I"],
             [2, "Love"],
             [3, "You"],
             [4, "Chiu"],
             [5, "Chiu"]
           ]
  end

  test "Ex36 day in month" do
    cases = [
      {1, {"January", 31}},
      {2, {"February", 28}},
      {3, {"March", 31}},
      {4, {"April", 30}},
      {7, {"July", 31}},
      {8, {"August", 31}},
      {9, {"September", 30}}
    ]

    assert cases == [1, 2, 3, 4, 7, 8, 9] |> Enum.map(fn i -> {i, Ex36.solve(i)} end)
  end

  test "Ex37 multiple of 5" do
    assert "95 == 19 * 5" == Ex37.solve() |> List.last()
  end

  test "Ex38 palindrome " do
    assert Ex38.solve("Able was I ere I saw Elba") == true
    assert Ex38.solve("Civi") == false
    assert Ex38.solve("Civic") == true
    assert Ex38.solve("C") == false
    assert Ex38.solve("CC") == false
  end

  test "Ex39 simple math with 3 variables" do
    results = Ex39.solve()
    assert {9, 1, 1} == List.first(results)
    assert {1, 9, 1} == List.last(results)
  end

  test "Ex310 find common elements of two list" do
    assert Ex310.solve([1, 5, 2, 3, 4], [4, 5, 0, 4]) == [4, 5]
    assert Ex310.solve([1, 2, 3, 4], [5, 6, 7, 8]) == []
  end
end
