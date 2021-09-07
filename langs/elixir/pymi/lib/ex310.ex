defmodule Ex310 do
  def solve(list1, list2) do
    list1 |> Enum.filter(fn x -> Enum.member?(list2, x) end) |> Enum.uniq() |> Enum.sort()
  end
end
