defmodule Ex74 do
  @doc """
  Thực hiện biến đổi

    input: [a, abbbccccdddd, xxyyyxyyx]
    output: [a, abb3cc4dd4, xx2yy3xyy2x]

  Giải thích: Những chữ cái không lặp lại thì output giữ nguyên chữ cái đó.
  Những chữ cái liên tiếp sẽ in ra 2 lần + số lần lặp lại liên tiếp.

  Đây là một biến thể của một thuật toán nén dữ liệu có tên Run-length
  encoding (RLE).
  """
  def solve(string) do
    cl = string |> String.to_charlist()

    if cl == [] do
      ""
    else
      [head | tail] = cl
      rle(tail, head, 1, [])
    end
  end

  def rle([], aux, count, result) do
    compressed =
      if count == 1 do
        [aux | result]
      else
        [Integer.to_charlist(count) | [aux | [aux | result]]]
      end

    compressed |> Enum.reverse() |> List.to_string()
  end

  def rle([head | tail], aux, count, result) do
    if head == aux do
      rle(tail, head, count + 1, result)
    else
      if count == 1 do
        rle(tail, head, 1, [aux | result])
      else
        rle(tail, head, 1, [Integer.to_charlist(count) | [aux | [aux | result]]])
      end
    end
  end

  def rle2(string) do
    string
    |> String.split("", trim: true)
    |> Enum.chunk_by(fn x -> x end)
    |> Enum.map(fn xs ->
      if length(xs) == 1 do
        "#{List.first(xs)}"
      else
        "#{List.first(xs)}#{List.first(xs)}#{length(xs)}"
      end
    end)
    |> Enum.join()
  end
end
