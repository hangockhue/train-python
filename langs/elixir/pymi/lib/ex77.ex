defmodule Ex77 do
  @data """
  <?xml version="1.0"?>
    <data>
      <country name="Liechtenstein">
          <rank>1</rank>
          <year>2008</year>
          <gdppc>141100</gdppc>
          <neighbor name="Austria" direction="E"/>
          <neighbor name="Switzerland" direction="W"/>
      </country>
      <country name="Singapore">
          <rank>4</rank>
          <year>2011</year>
          <gdppc>59900</gdppc>
          <neighbor name="Malaysia" direction="N"/>
      </country>
      <country name="Panama">
          <rank>68</rank>
          <year>2011</year>
          <gdppc>13600</gdppc>
          <neighbor name="Costa Rica" direction="W"/>
          <neighbor name="Colombia" direction="E"/>
      </country>
  </data>
  """

  @doc """
  Trả về list các tuple (tên quốc gia, thứ hạng)
  TODO: improve this by iterating, using xpath is not safe here,
  Check what if rank is missing from a country?
  """
  def solve() do
    tree = Exml.parse(@data)
    countries = Exml.get(tree, "country/@name")
    ranks = Exml.get(tree, "country/rank") |> Enum.map(fn x -> String.to_integer(x) end)
    Enum.zip(countries, ranks)
  end
end
