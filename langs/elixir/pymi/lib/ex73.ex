defmodule Ex73 do
  require Logger

  @doc """
  - Lưu file ``https://raw.githubusercontent.com/hvnsweeting/states/master/salt/event/init.sls`` về máy với tên event.yaml

  - Dùng pip cài thư viện PyYAML, import yaml và dùng `yaml.safe_load` để biến nội
  dung trong file thành kiểu dữ liệu trên Python.

  - In ra số phần tử của kiểu dữ liệu vừa tạo. Dùng thư viện json để
   `json.dump` nội dung, ghi ra một file tên là event.json trong thư mục hiện tại.

  - Dùng thư viện pickle để pickle.dump nội dung trên ra file event.pkl trong
    thư mục hiện tại. Chú ý khi mở file, phải mở ở chế độ ghi ở dạng binary. Đọc
    thêm tại đây:
    https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files`

  - In ra kích thước của mỗi file đã tạo.

  Gợi ý: sử dụng os.stat(filename).st_size
  """
  def solve() do
    full_path = Path.expand("../../../exercises/event.yaml")
    Logger.info("File size is #{File.stat!(full_path).size}")

    {:ok, content} = YamlElixir.read_from_file(full_path)
    content |> Map.to_list() |> length
  end
end
