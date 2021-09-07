defmodule Ex35 do
  def solve(iter) do
    iter
    |> Enum.with_index(1)
    |> Enum.map(fn {elem, idx} -> [idx, elem] end)
  end
end
