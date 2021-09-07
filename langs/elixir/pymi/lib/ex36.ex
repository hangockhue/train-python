defmodule Ex36 do
  @doc """
  Input: một số nguyên trong range(1,13,1). # start=1, stop=13, step=1
  Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
  Tháng 2 tính 28 ngày.
  """
  def solve(month) do
    months_days = [
      {"January", 31},
      {"February", 28},
      {"March", 31},
      {"April", 30},
      {"May", 31},
      {"June", 30},
      {"July", 31},
      {"August", 31},
      {"September", 30},
      {"October", 31},
      {"November", 30},
      {"December", 31}
    ]

    Enum.at(months_days, month - 1)
  end
end
