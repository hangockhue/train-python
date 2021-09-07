defmodule Ex64 do
  @doc """
  Viết function ``sumall`` tính tổng của tất cả các argument (int, float,
    hoặc string) được gọi. Thay input_data bằng code phù hợp.
  def solve(input) do
  """
  def solve(input) do
    sumall(input)
  end

  @doc """
  There is no variadic function in Elixir

  1) a function's arity is part of its name and
  2) there are no variadic functions.
  """
  def sumall([]) do
    0
  end

  def sumall([h | t]) when is_binary(h) do
    # need to check float or int
    h = String.trim(h)

    number =
      if String.contains?(h, ".") do
        String.to_float(h)
      else
        String.to_integer(h)
      end

    number + sumall(t)
  end

  def sumall([h | t]) do
    h + sumall(t)
  end
end
