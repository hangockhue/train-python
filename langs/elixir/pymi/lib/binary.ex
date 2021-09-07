defmodule Binary do
  @doc """
  Converts integer to string binary representation
  """
  def binary(n) do
    _binary(n, "")
  end

  def _binary(1, acc) do
    "1" <> acc
  end

  def _binary(0, acc) do
    "0" <> acc
  end

  def _binary(n, acc) do
    aux = rem(n, 2) |> Integer.to_string()
    _binary(div(n, 2), aux <> acc)
  end
end
