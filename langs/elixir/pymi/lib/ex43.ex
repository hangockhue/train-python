defmodule Ex43 do
  @doc """
    Trả về list chứa điểm tương ứng của các từ trong `words`

    Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...
    thì từ ``attitude`` có giá trị bằng 100.
    (http://www.familug.org/2015/05/golang-tinh-tu-cung-9gag.html)
  """
  def solve(word) do
    word
    |> String.downcase()
    |> String.to_charlist()
    |> Enum.map(fn c -> c - ?a + 1 end)
    |> Enum.sum()
  end
end
