defmodule Ex55 do
  @magic_number 20_200_000
  @doc """
    '''Biết những bạn có tên bắt đầu bằng chữ `D` sẽ ngồi phòng thi số N,
    các bạn có tên bắt đầu chữ `H` ngồi phòng thi số N+1, và các bạn còn lại,
    nếu có tên kết thúc là `ng` sẽ ngồi cùng phòng các bạn tên `H`, còn lại
    ngồi cùng phòng `D`.
    Tất cả các học viên đều sinh năm 1990.
    Mã học viên được tính bằng: hash(NAME) % MAGIC_NUMBER
    (chú ý số này mỗi lần chạy sẽ khác nhau).
    Ví dụ: mã học viên của 'Dung' là: hash('Dung') % MAGIC_NUMBER

    Trả về result là list các tuple chứa
    (mã sinh viên, tên học viên, năm sinh, phòng thi), sắp xếp
    theo thứ tự tên học viên.
  """
  def solve(students, n \\ 5) do
    students
    |> Enum.map(fn name ->
      # case does not work, use cond https://stackoverflow.com/questions/34649321/regular-expressions-in-elixir-case
      # case work on value in head
      # cond have function call in head
      room =
        cond do
          ~r/^D.*/ ->
            n

          ~r/^H.*/ ->
            n + 1

          true ->
            if String.ends_with?(name, "ng") do
              n + 1
            else
              n
            end
        end

      {"1", name, 1990, room}
    end)
    |> Enum.sort(fn {_, name1, _, _}, {_, name2, _, _} -> name1 < name2 end)
  end
end
