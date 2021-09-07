defmodule Ex37 do
  @doc """
  Xét các số nguyên dương < 100, in ra các số chia hết cho 5 theo dạng::

    5 == 1 * 5
    10 == 2 * 5
    15 == 3 * 5
    ...
  """
  def solve() do
    1..99
    |> Enum.filter(fn x -> rem(x, 5) == 0 end)
    |> Enum.map(fn x -> "#{x} == #{div(x, 5)} * 5" end)
  end
end
