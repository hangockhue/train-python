defmodule Ex352 do
  @doc """
  Creates a list which contains N random integers, each >=0, <=9
  """
  def solve(n) do
    Stream.repeatedly(fn -> Enum.random(1..9) end)
    |> Enum.take(n)
  end
end
