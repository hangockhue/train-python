defmodule Ex356 do
  @doc """
    What is the sum of the digits of the number `2**1000`?
    https://projecteuler.net/problem=16
  """
  def pow(_, 0) do
    1
  end

  def pow(x, n) do
    x * pow(x, n - 1)
  end

  def convert_and_sum("", acc) do
    acc
  end

  def convert_and_sum(s, acc) do
    # TODO is there a better way?
    h = String.at(s, 0)
    t = String.slice(s, 1..-1)
    convert_and_sum(t, acc + String.to_integer(h))
  end

  def solve() do
    pow(2, 1000)
    |> to_string
    |> convert_and_sum(0)
  end
end
