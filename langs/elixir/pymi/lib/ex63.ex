defmodule Ex63 do
  @doc """
  Tìm ngày giá BTC lên cao nhất. Trả về Tuple chứa ngày ở định dạng
  YYYY-mm-dd (VD: 2017-06-19) và giá VND của 1 BTC

  # http://api.bitcoincharts.com/v1/csv/
  """
  def solve() do
    {timestamp, max_price} =
      Path.expand("../../../exercises/localbtcVND.csv")
      |> File.stream!()
      |> Stream.map(fn x ->
        [timestamp, price, _] = String.trim(x) |> String.split(",")
        {String.to_integer(timestamp), String.to_float(price)}
      end)
      |> Enum.reduce({-1, -1}, fn {ts1, price1}, {ts2, price2} ->
        if price1 > price2 do
          {ts1, price1}
        else
          {ts2, price2}
        end
      end)

    {:ok, date} = DateTime.from_unix(timestamp)
    {Date.to_string(date), max_price}
  end
end
