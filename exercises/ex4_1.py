#!/usr/bin/env python3
"""
Khi làm bài 4, học viên nhớ làm lại đầy đủ từ bước số 1 trong hướng dẫn nộp
bài để tránh bị nộp lẫn bài 3 và bài 4 với nhau.

==========

Bài tập ở PyMi không nhằm để kiểm tra IQ của học sinh, cũng không thi lấy điểm,
mục tiêu của chúng tôi là học viên với trình độ đầu vào tùy ý, nhưng đến
lúc ra đều có thể làm được việc. Vì vậy, nếu không tự làm được bài tập,
học viên được KHUYẾN KHÍCH xem bài các bạn khác để làm mẫu rồi gõ làm theo.
Tránh tình trạng không làm bài tập với lý do "không làm được".
Xem tại: https://gitlab.com/pyfml/pyfml/merge_requests

Đọc thêm:
- https://pymi.vn/tutorial/boolean/
- https://pymi.vn/tutorial/naming/
- https://pymi.vn/blog/sap-xep-tieng-viet/
- https://pymi.vn/tutorial/string1/
- https://pymi.vn/tutorial/unicode/

===========

while loop

Dùng để lặp khi 1 điều kiện còn đúng:

```python
In [2]: i = 0

In [3]: while i < 5:
   ...:     print(i)
   ...:     i = i + 1
   ...:
0
1
2
3
4
```

Tham khảo:
- https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming
- https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
"""  # noqa


def solve(ip):
    """IP là địa chỉ của một máy tính trong mạng (như địa chỉ nhà).
    IPv4 được biểu diễn bằng 4 số từ 0-255, phân cách nhau bởi dấu `.`
    Mỗi số trong khoảng 0-255 được biểu diễn bằng 8 bits (1 byte),
    có tài liệu gọi 4 phần trong IPv4 này là 4 octet.
    VD: IP của Google DNS là 8.8.8.8, IP mọi máy tính dùng để chỉ chính nó
    có địa chỉ 127.0.0.1 hay thường gọi là localhost.

    Trả về string biểu diễn binary (hệ cơ số 2) của `ip`.

    Input::

      192.168.1.1

    Output::

      11000000.10101000.00000001.00000001

    Python có funtion đổi số integer thành biểu diễn ở hệ nhị phân (binary):

      In [1]: bin(168)
      Out[1]: '0b10101000'

    Khi s = '1', s.zfill(5) sẽ thêm đủ "zero" để tạo thành '00001'
    """
    result = None
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")

    return result


def main():
    """
    Biết function `input('Bạn tên gì?')` sẽ in ra màn hình dòng chữ "Bạn tên
    gì?"
    và chờ bạn nhập câu trả lời. Sau khi bạn gõ câu trả lời rồi enter,
    nội dung bạn vừa gõ sẽ được function trả về::

      In [4]: name = input('Bạn tên gì? ')
      Bạn tên gì? Hưng

      In [5]: print(name)
      Hưng

    Note::

      Trên Python2, function tương ứng tên là `raw_input`
    """

    ip = input("Nhập vào IP:")
    print(solve(ip))


if __name__ == "__main__":
    main()
