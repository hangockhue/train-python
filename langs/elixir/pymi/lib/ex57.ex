defmodule Ex57 do
  @doc """
  Trả về string biễu diễn tương ứng ở hệ thập phân (decimal),
  hệ nhị phân (binary), bát phân (octal), thập lục phân (heximal)

  Gợi ý: sử dụng bin(), oct(), hex(), string method `rjust`
  Mỗi dòng 1 số, với độ rộng là 8, các giá trị thẳng nhau căn lề phải.
  Output :

  1       1     0o1     0x1
  2      10     0o2     0x2
  ...
  """
  def p8(s) when is_integer(s) do
    s |> Integer.to_string() |> String.pad_leading(8)
  end

  def p8(s) do
    String.pad_leading(s, 8)
  end

  def format_binary(n) do
    n |> Integer.to_string(2) |> p8
  end

  def format_octal(n) do
    p8("0o" <> Integer.to_string(n, 8))
  end

  def format_hex(n) do
    p8("0x" <> Integer.to_string(n, 16))
  end

  def solve(number_range) do
    number_range
    |> Enum.map(fn n ->
      "#{p8(n)}#{format_binary(n)}#{format_octal(n)}#{format_hex(n)}\n"
    end)
  end
end
