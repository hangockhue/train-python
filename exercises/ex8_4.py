#!/usr/bin/env python3


__doc__ = """
Yêu cầu:
- Viết decorator in ra thời gian chạy của 1 function
"""

import time


def your_decorator(function):
    """Tính thời gian chạy của `function` (float)"""
    # Sửa lại tên và function cho phù hợp
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    return


# Sửa tên decorator cho phù hợp
@your_decorator
def worker():
    for i in range(10000):
        pass
    time.sleep(1)


def solve():
    """Thực hiện 1 tính toán bất kì trong function `solve`

    Trả về kết quả tùy ý, gán lại vào `result`
    """
    result = worker()
    # Xoá dòng sau sau khi đã thay đổi your_decorator phù hợp
    raise NotImplementedError("Học viên chưa thực hiện tính toán")
    return result


def main():
    print("Function worker chạy mất: {0} giây".format(solve()))


if __name__ == "__main__":
    main()
