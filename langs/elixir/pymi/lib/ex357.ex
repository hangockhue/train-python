defmodule Ex357 do
  @doc """
    Calculates sum of a list contains all integers less than N,
    which are multiple of 3 or 5.
  """
  def solve(n) do
    1..(n - 1)
    |> Enum.filter(fn x -> rem(x, 3) == 0 or rem(x, 5) == 0 end)
    |> Enum.sum()
  end
end
