defmodule Ex44 do
  @doc """
    Tính số nghiệm của bài toán lớp 3

    Với các biến a,b,c,d,e,f,g,h,i là các số nằm trong khoảng 1-9 (các biến có
    thể có giá trị giống nhau), dạng biểu thức:

      a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 = 66

    Bài toán lớp 3 có số đáp án khổng lồ
    (http://www.familug.org/2015/05/codegolf-giai-bai-toan-lop-3-co-so.html)
  """
  def condition1(f, a, d, e) do
    87 + f - a - d - e * 12 > 0
  end

  def condition2(f, a, d, e, c, i, b) do
    rhs = 87 + f - a - d - e * 12
    rhs2 = rhs * i * c - 13 * b * i
    rem(b * i, c) == 0 && rhs2 > 0
  end

  def condition3(f, a, d, e, c, i, b, g, h) do
    rhs = 87 + f - a - d - e * 12
    rhs2 = rhs * i * c - 13 * b * i
    g * h * c == rhs2
  end

  @doc """
  Follow https://play.golang.org/p/euUskIcgtE
  """
  def solve() do
    fade =
      for f <- 1..9, a <- 1..9, d <- 1..9, e <- 1..9, condition1(f, a, d, e), do: {f, a, d, e}

    fadecib =
      for {f, a, d, e} <- fade,
          c <- 1..9,
          i <- 1..9,
          b <- 1..9,
          condition2(f, a, d, e, c, i, b),
          do: {f, a, d, e, c, i, b}

    result =
      for {f, a, d, e, c, i, b} <- fadecib,
          h <- 1..9,
          g <- 1..9,
          condition3(f, a, d, e, c, i, b, g, h),
          do: 1

    result
    |> length
  end
end
