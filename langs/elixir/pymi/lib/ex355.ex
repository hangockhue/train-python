defmodule Ex355 do
  @doc """
    Creates a list like this - odd numbers repeat six times.
    ['111111', '333333', ..., '999999', '111111111111',..., NNNNNN]
  """
  def int_to_string6(i) do
    Stream.repeatedly(fn -> Integer.to_string(i) end)
    |> Enum.take(6)
    |> Enum.join()
  end

  def solve(n) do
    1..n
    |> Enum.filter(fn x -> rem(x, 2) == 1 end)
    |> Enum.map(&int_to_string6/1)
  end
end
