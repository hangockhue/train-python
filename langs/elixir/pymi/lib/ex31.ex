defmodule Ex31 do
  @doc """
  Returns integer that is part from last 1 to the right
  in binary representation of n
  """
  def solve(n) do
    _solve(n, "")
    |> String.to_integer()
  end

  def _solve(1, acc) do
    "1" <> acc
  end

  def _solve(0, acc) do
    "0" <> acc
  end

  def _solve(n, acc) do
    aux = rem(n, 2) |> Integer.to_string()

    if aux == "1" do
      aux <> acc
    else
      _solve(div(n, 2), aux <> acc)
    end
  end

  def main() do
    IO.puts("Ex 3_1")
    binaries = 1..10 |> Enum.map(&Binary.binary/1)
    results = 1..10 |> Enum.map(&solve/1)
    Enum.zip(1..10, Enum.zip(binaries, results)) |> IO.inspect()
  end
end
