defmodule Ex35Test do
  use ExUnit.Case
  doctest Pymi

  test "Gen list 10 elements 2" do
    assert Ex351.solve() == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert Ex351.solve() == for(_ <- 1..10, do: 2)
  end

  test "Gen list N random integer" do
    assert Ex352.solve(5) |> length == 5
    assert Ex352.solve(3) |> Enum.member?(0) == false
    assert Ex352.solve(3) |> Enum.member?(10) == false
  end

  test "Gen list first N even integers" do
    assert Ex353.solve(5) |> length == 5
    assert Ex353.solve(3) == [2, 4, 6]
  end

  test "Gen string contains N random ASCII letters" do
    assert Ex354.solve(5) |> length == 5
    assert Ex354.solve(3) |> length == 3
    one = Ex354.solve(3) |> List.first()
    assert 65 <= one
    assert 122 >= one
  end

  test "Gen list of string of 6 chars of odd numbers til N" do
    assert Ex355.solve(1) == ["111111"]
    assert Ex355.solve(2) == ["111111"]
    assert Ex355.solve(3) == ["111111", "333333"]
  end

  test "Test 356 power function" do
    assert Ex356.pow(2, 2) == 4
    assert Ex356.pow(2, 3) == 8
    assert Ex356.pow(3, 2) == 9
    assert Ex356.pow(2, 10) == 1024
  end

  test "Test sum of all digits of 2 to the power of 1000 - ProjectEuler 16" do
    assert Ex356.solve() == 1366
  end

  test "Test sum of multiples of 3 or 5 - PE01" do
    assert Ex357.solve(1000) == 233_168
  end

  test "Test 358" do
    assert Ex358.solve() == "\
0********0
*1******1*
**2****2**
***3**3***
****44****
****55****
***6**6***
**7****7**
*8******8*
9********9"
  end
end
