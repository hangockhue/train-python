#!/usr/bin/env python3

__doc__ = """
Chuẩn bị cho buổi sau
---------------------

- Cài đặt `requests`, `BeautifulSoup4` lên máy:
http://docs.python-requests.org/en/latest/user/install/#install
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

Chú ý cách đọc docstring của function:
--------------------------------------

- :rtype abc: kiểu dữ liệu trả về của function là `abc`
- :param name: phần mô tả cho argument `name` truyền vào function

Từ bài này, thay vì dùng print, ta sẽ dùng logging để ghi lại "nhật ký" (log)
của chương trình.

Đọc thêm: https://github.com/hvnsweeting/pynosed

Các đoạn code Python để thay thế UNIX command lines.

Tham khảo các viết chương trình có giao diện đồ họa với TK::

https://pp.pymi.vn/article/gui/

Giải đáp các thắc mắc về phần mềm có giao diện đồ họa:
https://docs.python.org/3/faq/gui.html

Từ Python 3.6 trở đi, có thể sử dụng type annotation để ký hiệu kiểu của
input/output function, kiểu của các biến...
Tham khảo https://pp.pymi.vn/article/mypy/
https://docs.python.org/3/tutorial/controlflow.html#function-annotations
"""


def main() -> None:
    print(__doc__)


if __name__ == "__main__":
    main()
