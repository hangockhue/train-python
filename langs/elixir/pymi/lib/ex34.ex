defmodule Ex34 do
  @doc """
  Viết chương trình loại bỏ phần mở rộng của một tên file bất kỳ.
  """
  def remove_ext(filename) do
    # TODO: need better way
    idx =
      filename
      |> String.reverse()
      |> String.to_charlist()
      |> Enum.find_index(fn x -> x == ?. end)

    String.slice(filename, 0, String.length(filename) - 1 - idx)
  end

  def solve(filename) do
    remove_ext(filename)
  end
end
