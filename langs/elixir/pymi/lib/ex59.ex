defmodule Ex59 do
  @data [
    %{name: "An Giang", population: 2_153_700, area: 3536.7, senator: 10},
    %{name: "Bà Rịa - Vũng Tàu", population: 1_039_200, area: 1989.5, senator: 6},
    %{name: "Bạc Liêu", population: 873_400, area: 2468.7, senator: 6},
    %{name: "Bắc Kạn", population: 301_000, area: 4859.4, senator: 6},
    %{name: "Bắc Giang", population: 1_588_500, area: 3848.9, senator: 8},
    %{name: "Bắc Ninh", population: 1_079_900, area: 822.7, senator: 6},
    %{name: "Bến Tre", population: 1_258_500, area: 2357.7, senator: 7},
    %{name: "Bình Dương", population: 1_748_000, area: 2694.4, senator: 8},
    %{name: "Bình Định", population: 1_501_800, area: 6050.6, senator: 8},
    %{name: "Bình Phước", population: 912_700, area: 6871.5, senator: 6},
    %{name: "Bình Thuận", population: 1_193_500, area: 7812.8, senator: 7},
    %{name: "Cà Mau", population: 1_217_100, area: 5294.9, senator: 7},
    %{name: "Cao Bằng", population: 515_200, area: 6707.9, senator: 6},
    %{name: "Cần Thơ", population: 1_214_100, area: 1409, senator: 7},
    %{name: "Đà Nẵng", population: 973_800, area: 1285.4, senator: 6},
    %{name: "Đắk Lắk", population: 1_796_700, area: 13125.4, senator: 9},
    %{name: "Đắk Nông", population: 543_200, area: 6515.6, senator: 6},
    %{name: "Đồng Nai", population: 2_720_800, area: 5907.2, senator: 11},
    %{name: "Đồng Tháp", population: 1_676_300, area: 3377, senator: 8},
    %{name: "Điện Biên", population: 519_300, area: 9562.9, senator: 6},
    %{name: "Gia Lai", population: 1_342_700, area: 15536.9, senator: 7},
    %{name: "Hà Giang", population: 758_000, area: 7914.9, senator: 6},
    %{name: "Hà Nam", population: 790_000, area: 860.5, senator: 6},
    %{name: "Hà Nội", population: 6_844_100, area: 3323.6, senator: 30},
    %{name: "Hà Tĩnh", population: 1_230_500, area: 5997.8, senator: 7},
    %{name: "Hải Dương", population: 1_735_100, area: 1656, senator: 9},
    %{name: "Hải Phòng", population: 1_904_100, area: 1523.9, senator: 9},
    %{name: "Hòa Bình", population: 806_100, area: 4608.7, senator: 6},
    %{name: "Hậu Giang", population: 769_700, area: 1602.5, senator: 6},
    %{name: "Hưng Yên", population: 1_145_600, area: 926, senator: 7},
    %{name: "TP. Hồ Chí Minh", population: 7_681_700, area: 2095.6, senator: 30},
    %{name: "Khánh Hòa", population: 1_183_000, area: 5217.7, senator: 7},
    %{name: "Kiên Giang", population: 1_726_200, area: 6348.5, senator: 9},
    %{name: "Kon Tum", population: 462_400, area: 9689.6, senator: 6},
    %{name: "Lai Châu", population: 397_500, area: 9068.8, senator: 6},
    %{name: "Lào Cai", population: 646_800, area: 6383.9, senator: 6},
    %{name: "Lạng Sơn", population: 744_100, area: 8320.8, senator: 6},
    %{name: "Lâm Đồng", population: 1_234_600, area: 9773.5, senator: 7},
    %{name: "Long An", population: 1_458_200, area: 4492.4, senator: 8},
    %{name: "Nam Định", population: 1_836_900, area: 1652.6, senator: 9},
    %{name: "Nghệ An", population: 2_952_000, area: 16490.9, senator: 13},
    %{name: "Ninh Bình", population: 915_900, area: 1376.7, senator: 6},
    %{name: "Ninh Thuận", population: 576_700, area: 3358.3, senator: 6},
    %{name: "Phú Thọ", population: 1_335_900, area: 3533.4, senator: 7},
    %{name: "Phú Yên", population: 877_200, area: 5060.6, senator: 6},
    %{name: "Quảng Bình", population: 857_900, area: 8065.3, senator: 6},
    %{name: "Quảng Nam", population: 1_450_100, area: 10438.4, senator: 8},
    %{name: "Quảng Ngãi", population: 1_227_900, area: 5153, senator: 7},
    %{name: "Quảng Ninh", population: 1_177_200, area: 6102.3, senator: 7},
    %{name: "Quảng Trị", population: 608_100, area: 4739.8, senator: 6},
    %{name: "Sóc Trăng", population: 1_301_900, area: 3311.6, senator: 7},
    %{name: "Sơn La", population: 1_134_300, area: 14174.4, senator: 7},
    %{name: "Tây Ninh", population: 1_089_900, area: 4039.7, senator: 6},
    %{name: "Thái Bình", population: 1_868_800, area: 1570, senator: 9},
    %{name: "Thái Nguyên", population: 1_150_200, area: 3534.7, senator: 7},
    %{name: "Thanh Hóa", population: 3_426_600, area: 11132.2, senator: 16},
    %{name: "Thừa Thiên - Huế", population: 1_114_500, area: 5033.2, senator: 7},
    %{name: "Tiền Giang", population: 1_692_500, area: 2508.3, senator: 8},
    %{name: "Trà Vinh", population: 1_015_300, area: 2341.2, senator: 6},
    %{name: "Tuyên Quang", population: 738_900, area: 5867.3, senator: 5},
    %{name: "Vĩnh Long", population: 1_033_600, area: 1504.9, senator: 6},
    %{name: "Vĩnh Phúc", population: 1_020_600, area: 1236.5, senator: 6},
    %{name: "Yên Bái", population: 764_400, area: 6886.3, senator: 7}
  ]
  def get_data, do: @data

  @doc """
  - Tạo 1 list chứa tên, dân số của các thành phố có tên bắt đầu bằng chữ H,
  sắp xếp theo thứ tự tên A-Z.

  - Tạo 1 list chứa tên, dân số của các thành phố có dân số trên 1 triệu,
  sắp xếp theo thứ tự giảm dần.
  """
  def solve(data) do
    start_with_h =
      data
      |> Enum.map(fn p -> {p.name, p.population} end)
      |> Enum.filter(fn {name, _} -> String.starts_with?(name, "H") end)
      |> Enum.sort(fn name1, name2 -> name1 < name2 end)

    more_than_1mil =
      data
      |> Enum.map(fn p -> {p.name, p.population} end)
      |> Enum.filter(fn {_, pol} -> pol > 1_000_000 end)
      |> Enum.sort(fn {_, p1}, {_, p2} -> p1 > p2 end)

    {start_with_h, more_than_1mil}
  end
end
