defmodule Ex65 do
  @doc """
  Trả về list chứa các dictionary chứa data về các contributor bao gồm
  các key: login, html_url và contributions.
  Nếu html_url nào bị thiếu, tạo html_url mới bằng
  "https://github.com/" + login tương ứng.
  """
  def solve() do
    {:ok, contributors} =
      Path.expand("../../../exercises/salt_contributors.json")
      |> File.read!()
      |> Jason.decode()

    contributors
    |> Enum.map(fn c ->
      html_url =
        case c["html_url"] do
          nil -> "https://github.com/" <> c["login"]
          "" -> "https://github.com/" <> c["login"]
          url -> url
        end

      %{login: c["login"], contributions: c["contributions"], html_url: html_url}
    end)
  end
end
