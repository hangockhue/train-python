defmodule Ex49 do
  @doc """
    Tìm phần tử lớn nhất của list số nguyên `numbers`
    Không sử dụng function `max`, `sorted`
  """
  def solve([]) do
    raise Enum.EmptyError
  end

  def solve(numbers) do
    max(numbers)
  end

  defp max([h | t]) do
    do_max(t, h)
  end

  defp do_max([], max) do
    max
  end

  defp do_max([h | t], max) do
    if h > max do
      do_max(t, h)
    else
      do_max(t, max)
    end
  end
end
