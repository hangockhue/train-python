defmodule Ex56 do
  @doc """
  term1 = {'math': 3, 'python': 5, 'data': 2}
  term2 = {'math': 7, 'python': 9, 'SQL': 8, 'HTML': 6}
  '''Trả về result là dict chứa bảng điểm của các môn học sau hai học kỳ.
  Biết điểm số được chọn là điểm số ở lần học sau cùng.
  """
  def solve(t1, t2) do
    Map.merge(t1, t2, fn _, v1, v2 -> v2 end)
  end
end
