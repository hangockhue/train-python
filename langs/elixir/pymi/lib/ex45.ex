defmodule Ex45 do
  @doc """
    '''Tính tổng và tích của dãy số `numbers`

    Return một tuple (sum, product)
    Không sử dụng hàm `sum`
    '''
  """
  def solve(numbers) do
    {Enum.reduce(numbers, 0, fn x, acc -> x + acc end),
     Enum.reduce(numbers, 1, fn x, acc -> x * acc end)}
  end
end
