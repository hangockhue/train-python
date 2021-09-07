defmodule Ex353 do
  @doc """
  Creates a list which contains N first even integers. ``[2, 4 ...]``
  """
  def solve(n) do
    1..(n * 2) |> Enum.filter(fn x -> rem(x, 2) == 0 end)
  end
end
