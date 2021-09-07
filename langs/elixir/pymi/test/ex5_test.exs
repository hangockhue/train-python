defmodule Ex5Test do
  use ExUnit.Case
  doctest Pymi

  test "51" do
    assert Ex51.solve() == [
             G: "#4885ed",
             o: "#db3236",
             o: "#f4c20d",
             g: "#4885ed",
             l: "#3cba54",
             e: "#db3236"
           ]
  end

  test "52" do
    assert Ex52.solve() == [
             %{
               name: "Hoang",
               phone: "0988888888",
               languages: ["Python", "C", "SQL", "HTML", "CSS", "JavaScript", "Golang", "Elixir"]
             },
             %{
               name: "Duy",
               languages: ["Python", "C", "SQL", "HTML", "CSS", "JavaScript", "Golang"]
             },
             %{
               name: "Dai",
               girl_friend: "Angela",
               languages: ["Python", "C", "SQL", "HTML", "CSS", "JavaScript", "Golang"]
             },
             %{
               name: "Tu",
               girl_friend: "Do Anh",
               languages: ["Python", "C", "SQL", "HTML", "CSS", "JavaScript", "Golang"]
             }
           ]
  end

  test "53" do
    data = """
    Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments.
    """

    res = Ex53.solve(data)
    assert {"be", 5} in res
    assert {"can", 4} in res
    assert length(res) == 10
  end

  describe "Big file" do
    @describetag :slow
    test "54" do
      assert Ex54.solve() == [
               "111111111111111111111111111111\n",
               "59999984\n",
               "111111111111111111111111111111\n",
               "59999988\n",
               "111111111111111111111111111111\n",
               "59999992\n",
               "111111111111111111111111111111\n",
               "59999996\n",
               "111111111111111111111111111111\n",
               "60000000\n"
             ]
    end
  end

  test "55" do
    data = ["Trang", "Trung", "Tien", "Dai", "Duong", "Dung", "Hung", "Huy", "Hoang"]

    assert Ex55.solve(data, 5)
           |> Enum.take(3)
           |> Enum.map(fn {_, name, _, room} -> {name, room} end) == [
             {"Dai", 5},
             {"Dung", 5},
             {"Duong", 5}
           ]
  end

  test "56" do
    term1 = %{math: 3, python: 5, data: 2}
    term2 = %{math: 7, python: 9, SQL: 8, HTML: 6}
    res = Ex56.solve(term1, term2)

    assert res[:python] == 9
    assert res[:math] == 7
    assert res[:data] == 2
  end

  test "57" do
    res = Ex57.solve(1..19)

    assert Enum.take(res, 2) == [
             "       1       1     0o1     0x1\n",
             "       2      10     0o2     0x2\n"
           ]

    assert Enum.take(res, -2) == [
             "      18   10010    0o22    0x12\n",
             "      19   10011    0o23    0x13\n"
           ]
  end

  test "58" do
    {ascii_, _, tabcp, newlinecp, spacecp} = Ex58.solve()
    assert Enum.take(ascii_, 3) == [{33, '!'}, {34, '"'}, {35, '#'}]
    assert Enum.take(ascii_, -4) == [{49, '1'}, {50, '2'}, {51, '3'}, {52, '4'}]
    assert {tabcp, newlinecp, spacecp} == {9, 10, 32}
  end

  test "59" do
    {start_with_h, more_than_1mil} = Ex59.solve(Ex59.get_data())
    assert Enum.take(start_with_h, -2) == [{"Hải Phòng", 1_904_100}, {"Hậu Giang", 769_700}]
    assert Enum.take(more_than_1mil, 2) == [{"TP. Hồ Chí Minh", 7_681_700}, {"Hà Nội", 6_844_100}]
  end
end
