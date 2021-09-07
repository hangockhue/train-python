defmodule Ex41 do
  @doc """
    192.168.1.1

    Output::

      11000000.10101000.00000001.00000001
  """
  def to_8bits_string(octet) do
    Binary.binary(octet)
    |> String.pad_leading(8, "0")
  end

  def solve(ip) do
    octets = String.split(ip, ".") |> Enum.map(&String.to_integer/1)

    octets
    |> Enum.map(&to_8bits_string/1)
    |> Enum.join(".")
  end
end
