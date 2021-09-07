defmodule Ex32 do
  def solve(text) do
    text
    |> String.split("\n", trim: true)
    |> Enum.map(fn sent -> String.at(sent, 0) end)
    |> Enum.join()
    |> String.upcase()
  end
end
