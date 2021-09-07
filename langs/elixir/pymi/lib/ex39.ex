defmodule Ex39 do
  @doc """
  a, b, c là các số nguyên dương nhỏ hơn 10, biết a + b/c = 10

  In ra list chứa các bộ số thỏa mãn điều kiện trên (a, b, c có thể trùng nhau).

  Ví dụ:

  - output: [[9, 1, 1], ...]
  """
  def condition(a, b, c) do
    a * c + b == 10 * c
  end

  def solve() do
    for a <- 9..1, b <- 1..9, c <- 1..9, condition(a, b, c), do: {a, b, c}
  end
end
