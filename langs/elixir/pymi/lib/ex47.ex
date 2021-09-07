defmodule Ex47 do
  @doc """
    Trả về tuple-2 chứa year và tên gọi can chi tương ứng. Các từ trong tên
    đề phải viết hoa các chữ cái đầu.

    Biết có 10 thiên can::

      ['giáp', 'ất', 'bính', 'đinh', 'mậu', 'kỷ', 'canh', 'tân', 'nhâm', 'quý']

    Và 12 địa chi::

      ['tý', 'sửu', 'dần', 'mão', 'thìn', 'tị', 'ngọ', 'mui', 'thân', 'dậu',
       'tuất', 'hợi']

    Năm 2017 là năm "Đinh Dậu".
  """
  def solve(year) do
    cans = ["giáp", "ất", "bính", "đinh", "mậu", "kỷ", "canh", "tân", "nhâm", "quý"]
    chis = ["tý", "sửu", "dần", "mão", "thìn", "tị", "ngọ", "mui", "thân", "dậu", "tuất", "hợi"]
    # 2017%10 == 7 == Dinh -> +6 as 3rd in cans
    # 2017%12 == 1 == dau -> + 8 as 9th in chis
    can = Enum.at(cans, rem(year + 6, 10)) |> String.capitalize()
    chi = Enum.at(chis, rem(year + 8, 12)) |> String.capitalize()
    "#{can} #{chi}"
  end
end
