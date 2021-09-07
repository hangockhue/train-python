#!/usr/bin/env python3

__doc__ = """

Đọc thêm:

- https://pymi.vn/blog/badcode/
- https://pymi.vn/blog/return-string/
- https://pymi.vn/blog/call-by/

Chuẩn bị cho buổi sau
---------------------

- Cài đặt virtualenv, dùng nó tạo virtualenv cho Python3 (-p python3)
- Xem trong thư mục ``env`` vừa tạo có gì.
  https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments
- Activate môi trường vừa tạo, dùng pip cài đặt các thư viện phổ biến::

  ```
  pip install requests six flake8 ipython ipdb numpy pandas scipy scikit-learn matplotlib jupyter flask gunicorn beautifulsoup4 requests-html
  pip install black # Python 3.6+ only
  ```
"""  # NOQA


def main():
    print(__doc__)


# __name__ là một biến|name đặc biệt do Python tự tạo ra
# nó có giá trị là string "__main__" khi file được chạy bằng lệnh
# python filename.py
# và có giá trị là tên file (bỏ .py) khi được import.
if __name__ == "__main__":
    print(__name__)
    main()
