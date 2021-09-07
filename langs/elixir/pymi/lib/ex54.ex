defmodule Ex54 do
  @doc """
  Tạo ra 1 file chứa 30 triệu dòng, các dòng lẻ chứa 30 số 1,
  các dòng chẵn chứa giá trị 2 * số dòng hiện tại.

  Sau khi tạo xong file, return result là list chứa 10 dòng cuối theo thứ tự
  dòng xuất hiện trước đứng trước.

  Chú ý: 30 triệu dòng.
  """
  def solve() do
    fs = File.stream!("/tmp/30_mil.txt")

    1..30_000_000
    |> Stream.map(fn i ->
      if rem(i, 2) == 1 do
        "111111111111111111111111111111\n"
      else
        Integer.to_string(i * 2) <> "\n"
      end
    end)
    |> Enum.into(fs)

    File.stream!("/tmp/30_mil.txt") |> Stream.take(-10) |> Enum.to_list()
  end
end
