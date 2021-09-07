defmodule Ex48 do
  @doc """
    Trả về list N bộ integer (a, b, c) là độ dài 3 cạnh của tam giác vuông
    cạnh huyền `c` có chu vi 24 cm (perimeter), biết độ dài các cạnh <= 10cm.

    Yêu cầu dùng list comprehension.
  """
  def check_sum(a, b, c) do
    a + b + c == 24 && c * c == a * a + b * b
  end

  def solve() do
    for a <- 1..10, b <- 1..10, c <- 1..10, check_sum(a, b, c), do: {a, b, c}
  end
end
