defmodule Ex51 do
  @data %{
    "xanh lá" => "#3cba54",
    "vàng" => "#f4c20d",
    "đỏ" => "#db3236",
    "xanh da trời" => "#4885ed"
  }

  @doc """
  Ghi ra file index.html code HTML để tạo ra logo của Google với màu sắc
  chính xác.
  Biết cách để tạo chữ G màu xanh da trời dùng code HTML sau::

    <span style="color:#4885ed">G</span>

  Return list chứa các tuple, mỗi tuple  chứa chữ cái trong 'Google' và màu
  của nó.
  Gợi ý: dùng `zip`

      In [1]: list(zip(['xanh', 'do'], ['XXX', 'YYY']))
      Out[1]: [('xanh', 'XXX'), ('do', 'YYY')]
  """
  def write_transparent({char, color}) do
    # TODO better way to write multiple lines
    # this should use :write, not :append but we need to write somehow different
    File.open("/tmp/google.html", [:append], fn file ->
      IO.write(file, "<span style='color:#{color}'>#{char}</span>\n")
    end)

    {char, color}
  end

  def solve() do
    [G: "xanh da trời", o: "đỏ", o: "vàng", g: "xanh da trời", l: "xanh lá", e: "đỏ"]
    |> Enum.map(fn {char, color} -> write_transparent({char, @data[color]}) end)
  end
end
