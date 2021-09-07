defmodule Ex62 do
  @doc """
  Chia input_data thành các tuple chứa N phần tử (chunk a list).
  Nếu tuple cuối không đủ phần tử thì bỏ đi.
  """
  def solve(input) do
    input
    |> Enum.chunk_every(2, 2, :discard)
    |> Enum.map(fn [a, b] -> {a, b} end)
  end
end
