defmodule Ex61 do
  @doc """
  Tính tiền điện (integer)
  với giá tiền cho bởi đề bài, số điện tiêu thụ `usage`
  """

  def solve(usages, prices) do
    cost(1, prices)

    usages
    |> Enum.map(fn {name, usage_str} ->
      {title(name), cost(String.to_integer(usage_str), prices)}
    end)
  end

  defp title(name) do
    name
    |> String.split(" ")
    |> Enum.map(fn x -> String.capitalize(x) end)
    |> Enum.join(" ")
  end

  defp cost(usage, prices) do
    cond do
      usage <= 50 ->
        usage * prices.first_50

      usage <= 100 ->
        prices.first_50 * 50 + (usage - 50) * prices.from_51_to_100

      usage > 100 ->
        prices.first_50 * 50 + prices.from_51_to_100 * 50 + (usage - 100) * prices.above_100
    end
  end
end
