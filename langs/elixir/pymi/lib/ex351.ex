defmodule Ex351 do
  @doc """
  Create a list which contains N elements 2
  """
  def solve() do
    Stream.cycle([2])
    |> Enum.take(10)
  end
end
