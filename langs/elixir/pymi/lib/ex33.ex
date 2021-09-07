defmodule Ex33 do
  def fizzbuzz(n) do
    cond do
      rem(n, 15) == 0 ->
        "FizzBuzz"

      rem(n, 3) == 0 ->
        "Fizz"

      rem(n, 5) == 0 ->
        "Buzz"

      true ->
        n
    end
  end

  def solve() do
    1..100
    |> Enum.map(&fizzbuzz/1)
  end
end
