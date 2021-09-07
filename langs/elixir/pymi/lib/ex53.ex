defmodule Ex53 do
  @doc """
    Đặt result bằng list chứa 10 tuple ứng với 10 từ xuất hiện nhiều nhất,
    mỗi tuple chứa từ và số lần xuất hiện tương ứng.
    (Nếu có nhiều từ cùng xuất hiện với số lần như nhau thì trả về từ nào
    cũng được).
    '''
  """
  def solve(text) do
    text
    |> String.trim()
    |> String.replace(["“", "”"], "")
    |> String.downcase()
    |> String.split()
    |> Enum.reduce(%{}, fn w, acc -> Map.update(acc, w, 1, fn c -> c + 1 end) end)
    |> Map.to_list()
    |> Enum.sort(fn {_, c1}, {_, c2} -> c1 > c2 end)
    |> Enum.take(10)
  end
end
