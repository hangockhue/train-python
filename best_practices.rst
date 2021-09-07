Các lỗi thường gặp
==================

Git báo `everything up to date`
-------------------------------

Bạn chưa gõ `git add`, `git commit` như trong hướng dẫn.

Comment code
------------

Code không dùng thì xoá đi, không comment. Sử dụng git là giải pháp xem lại các phiên bản cũ của
code (git log) -  vì vậy không có lý do gì để giữ lại code không dùng cả.

Duyệt từng phần tử của tập hợp
------------------------------

Nên [1]::

  names = ["Python", "C", "Java", "Elixir"]
  for name in names:
      print(name)

Không nên [2]::

  for i in range(len(names)):
      print(names[i])

Giải thích: khi mục đích là lấy từng phần tử, đoạn code [2] lại lấy index, rồi sau đó dùng index để truy cập vào phần tử của list. Code [1] không cần quan tâm đến index - thứ không có giá trị gì trong đoạn code. Ngoài ra code [1] cũng dễ đọc hơn. Đặc biệt với Python2, code [2] sẽ sinh ra một list integer với số phần tử bằng số phẩn tử của `names`, chỉ để dùng để làm index truy cập `names`. Tưởng tượng `names` có 1 triệu phần tử, [2] sẽ sinh ra thêm 1 list integer chứa 1 triệu phần tử nữa.

Nối string
----------

Nên [1]::

  lines = ['Line1', 'Line2', 'Line3']
  s = '\n'.join(lines)

Không nên [2]::

  s = ''
  for line in lines:
      s += line + '\n'

Lý do: string là kiểu dữ liệu ``immutable``, khi ``+`` hai string, nó không thay đổi string ban đầu mà sinh ra một string mới.

s sẽ lần lượt có các giá trị:

- ``''``
- ``Line1\n`` -> sẽ bị xóa đi sau đó
- ``Line1\nLine2`` -> sẽ bị xóa đi sau đó
- ``Line1\nLine2\nLine3``

Việc tạo ra các string trung gian này tốn tài nguyên hơn so với cách [1].

Nếu cần thêm ``\n`` ở cuối?::

  In [n]: lines = ['Line1', 'Line2', 'Line3']
     ...: lines.append('')
     ...: s = '\n'.join(lines)
     ...: s
     ...:
  Out[n]: 'Line1\nLine2\nLine3\n'

Tham khảo: https://docs.python.org/3/faq/programming.html#what-is-the-most-efficient-way-to-concatenate-many-strings-together

Tham khảo thêm:
- http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
- https://access.redhat.com/blogs/766093/posts/2802001
- http://pep8.org/
