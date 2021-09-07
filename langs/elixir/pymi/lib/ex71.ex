defmodule Ex71 do
  @doc """
  Return tổng (kiểu float) của các phân số trong args

  https://docs.python.org/3/library/fractions.html
  Thư viện fractions cung cấp class Fraction để tạo ra kiểu phân số trên
  Python.

  Tham khảo:
  http://www.familug.org/2017/03/python-fractions-tinh-toan-phan-so-tren.html
  """
  def solve([]) do
    Fraction.new("0/1")
    |> Fraction.to_float()
  end

  def solve([head | tail]) do
    Fraction.add(Fraction.new(head), solve_helper(tail))
    |> Fraction.to_float()
  end

  defp solve_helper([]) do
    Fraction.new("0/1")
  end

  defp solve_helper([head | tail]) do
    Fraction.add(Fraction.new(head), solve_helper(tail))
  end
end

defmodule Fraction do
  @moduledoc """
  #TODO handler * / -
  """
  defstruct [:numerator, :denominator]

  def new(string) do
    [num, den] = String.split(string, "/")
    [num, den] = [String.to_integer(num), String.to_integer(den)]
    %Fraction{numerator: num, denominator: den}
  end

  def add(n1, n2) do
    %Fraction{
      numerator: n1.numerator * n2.denominator + n2.numerator * n1.denominator,
      denominator: n1.denominator * n2.denominator
    }
  end

  def to_float(fraction) do
    fraction.numerator / fraction.denominator
  end
end
