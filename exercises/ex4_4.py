#!/usr/bin/env python3

import time


def solve():
    """Tính số nghiệm của bài toán lớp 3

    Với các biến a,b,c,d,e,f,g,h,i là các số nằm trong khoảng 1-9 (các biến có
    thể có giá trị giống nhau), dạng biểu thức:

      a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 = 66

    Bài toán lớp 3 có số đáp án khổng lồ
    (http://www.familug.org/2015/05/codegolf-giai-bai-toan-lop-3-co-so.html)

    Sau khi tính xong ra kết quả, học viên thử ước lượng bài toán đã
    xử lý bao nhiêu trường hợp, sau đó chia trung bình với thời gian chạy code
    xem mỗi giây tính được bao nhiêu phép tính.
    Tham khảo tốc độ CPU (bộ phận phần cứng thực hiện tính toán) trên
    https://cpu.pymi.vn/
    """

    start = time.time()
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")

    print("Took: {}".format(time.time() - start))
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
