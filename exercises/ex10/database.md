# Database

## Database là gì?
Theo từ điển [Cambridge](https://dictionary.cambridge.org/dictionary/english/database)

> Database: a large amount of information stored in a computer system in such a
> way that it can be easily looked at or changed.

Database bộ dữ liệu lưu trên máy tính, có thể dễ dàng tìm kiếm/thay đổi.

Vậy 1 text file có phải 1 database không? với định nghĩa trên thì rõ ràng là
có.
Wikipedia cũng có bài về ["flat-file
database"](https://en.wikipedia.org/wiki/Flat-file_database)

Đây là 1 định nghĩa chính xác, nhưng để truy cập dữ liệu này, thường thông qua
một hệ thống phần mềm "database management system" (DBMS), nên khi nói tới
database, người dùng muốn ám chỉ cả 2: data và DBMS.

Database là khái niệm khá chung chung, nhưng khi nói về database, hầu hết
mọi người đều muốn nói tới "SQL database".

## Có những loại database nào
Các DB có thể chia làm 2 nhóm chính: Relational (có quan hệ) và Non Relational
(không có quan hệ).

### Relational DBMS (RDBMS)
có thể kể tới

- Oracle
- MySQL
- Microsoft SQL Server
- PostgreSQL
- SQLite

nhìn chung (không bắt buộc), đều có sử dụng ngôn ngữ SQL để truy cập/thay đổi
dữ liệu, nên có chỗ gọi là SQL database.

### Non relational DBMS
Trở nên phổ biến vào khoảng năm 2010, với hy vọng ban đầu là THAY THẾ hệ thống
SQL database đã tồn tại lâu đời (1960/1970).
Một vài DB phổ biến nhất, kèm các tính năng thường dùng của chúng:
- Memcached: caching
- Redis: key-value DB, caching
- MongoDB: Document DB
- AWS DynamoDB: Document DB
- Elastisearch: searching
- Neo4j: Graph database

nhìn chung, nhóm này thường không dùng SQL để truy cập/thay đổi dữ liệu mà
mỗi DB có 1 cách riêng, nên có chỗ gọi là NoSQL. Tính năng của các DB
này cũng rất khác nhau.

## Dùng database nào
Trong các hệ thống truyền thống hoặc đơn giản, thường chỉ dùng 1 RDBMS như
Postgres, MySQL, SQL Server... Ngày nay khi các hệ thống Non Relational trở nên phổ biến,
chúng được dùng chung với các RDBMS để cung cấp các tính năng nổi trội hơn.
Như dùng Redis/Memcached để cache kêt quả để truy cập nhanh hơn, dùng
Elastisearch để tìm kiếm nhanh/hiệu quả hơn.
Sau 10 năm từ ngày mới nổi, NoSQL đã không chứng minh được mình có thể thay
thế RDBMS (và các hệ thống RDBMS cũng phát triển thêm nhiều tính năng mới, để
không bị thụt lùi).

## SQL - Structured Query Language
SQL (/ ˌ ɛ s ˌ k juː ˈ ɛ l / S-Q-L, / ˈ s iː k w əl / ) - Việtsub: Si Quờ

Structured Query Language là một ngôn ngữ được thiết kế để truy cập các RDBMS,
Có thể xem như 1 ngôn ngữ lập trình (chính xác hơn thì là DSL - domain specific
language), được chuẩn hóa ISO.

SQL khá khác biệt so với các ngôn ngữ lập trình thường gặp như Python/C/Java...
nó viết theo dạng "declarative" để đưa ra yêu cầu thứ cần truy cập, chứ không
viết cách làm như thế nào. Ví dụ:

```SQL
SELECT name, age, email FROM pymiers WHERE age >= 18;
```

để yêu cầu lấy ra name, age, email từ table `pymiers` với điều kiện age >= 18.
Mỗi câu lệnh SQL còn được gọi là "query".

#### Câu lệnh SQL chạy thế nào?
Phía trong các hệ thống RDBMS là các SQL engine, một phần mềm thông minh có
thể xem như 1 hệ thống AI (trí tuệ nhân tạo) thực hiện xử lý các câu lệnh SQL
để thu được kết quả yêu cầu. Người dùng nói chung không biết rõ chi tiết
nó hoạt động thế nào.

#### Table
Khái niệm chủ đạo của RDBMS là các table, mỗi table gồm các column (cột) định
nghĩa lúc tạo table, và các record (dòng). Có thể xem 1 table tương ứng với
một sheet (bảng) trong Excel/GoogleSheet, có hàng, có cột.
Các bảng này có thể liên kết với nhau (foreign key, trong Excel là VLOOKUP???).

#### Index
Sự khác biệt quan trọng giữa RDBMS và 1 file text, là khả năng
chọn ra các dòng thỏa mãn yêu cầu 1 cách nhanh hơn nhiều lần.

Ví dụ 1 file text theo format CSV chứa 1 triệu dòng:
```csv
1, Thích học Python, Hà Nội, Pymi.vn
2, Yêu Python, Sài Gòn, Pymi.vn
...
1000000, cuồng Python, TP HCM, Pymi.vn
```

Để tìm ra 1 học viên có tên "cuồng Python", trường hợp xấu nhất sẽ phải tìm qua
tất cả các dòng của file, tức 1 triệu dòng mới thấy. Thời gian này là khá lâu,
chưa kể tới nếu có thêm các điều kiện khác (như phải ở Hà Nội).

RDBMS giải quyết việc tìm kiếm kém hiệu quả này bằng cách tạo ra index cho mỗi
bảng. Index chứa 1 phần thông tin của dòng, sử dụng
kiểu dữ liệu được tối ưu cho việc tìm kiếm (Ví dụ:
[B-tree](https://en.wikipedia.org/wiki/B-tree)). Khi thêm 1 dòng vào table,
index sẽ được cập nhật để chứa 1 phần thông tin (thường là 1 hay nhiều cột),
sau đó tổ chức sao cho dễ tìm kiếm nhất.
Việc tạo index hoàn toàn do người dùng quyết định: index cái gì, index
bảng nào, cột nào...
Khi câu lệnh SQL thực hiện tìm kiếm,
SQL engine sẽ tìm trong index nếu đó là cột đã được index, và việc tìm kiếm này
nhanh hơn do: dữ liệu đã được sắp xếp tối ưu cho việc tìm kiếm + SQL engine
thông minh.
Index là một vấn đề khá nâng cao, đọc thêm ở đây https://sqlite.org/queryplanner.html

Khi query bị chậm, việc thường làm là thay đổi/ thêm index để chạy nhanh hơn.

## Dùng Python với Database
Như thấy ở trên, các RDBMS tương tự nhau và đều tuân theo 1 chuẩn chung, thì
các NoSQL mỗi cái một kiểu. Trong bài này sẽ lấy một vài ví dụ điển hình.

## RDBMS: SQL
Việc truy cập các RDBMS đều theo một thủ tục chung như sau:
- Tạo 1 kết nối đến RDBMS (thường cần user/password/địa chỉ để truy cập).
- Tạo 1 "cursor" dùng để chạy các câu lệnh SQL.
- Chạy các câu lệnh SQL để truy cập dữ liệu hay thay đổi dữ liệu (thêm/sửa/xóa).

## CRUD
4 loai câu lệnh SQL cơ bản để làm việc với database:
### C: Create
`CREATE TABLE table_name (column1 type1, column2 type2, column3 type3);`

### R: Read
`SELECT column1, column2, column3 FROM table_name WHERE column1 = 'some value'`

### U: Update
`UPDATE TABLE table_name SET column1=value1, column2=value2 WHERE column1 = 'some value';`

### D: Delete
`DELETE FROM table_name WHERE column1=value1`

## Security: SQL Injection
Theo [OWASP](https://owasp.org/www-project-top-ten/)
Injection là lỗi bảo mật phổ biến nhất trên thế giới.

SQL Injection là một kỹ thuật tấn công dựa vào việc đưa vào 1 giá trị hợp lệ, khiến thay đổi câu lệnh SQL lập trình viên mong muốn thành câu lệnh SQL mà hacker mong muốn, và thường là để chạy thêm 1 vài câu lệnh khác.

![Exploits of a Mom](https://imgs.xkcd.com/comics/exploits_of_a_mom.png )

SQL Injection thường thực hiện được do lập trình viên tạo câu lệnh sử dụng string format / chỉnh sửa string:

```
# KHÔNG BAO GIỜ làm như sau
query = "SELECT name, age FROM table WHERE name='{}'".format(name)
```

Hãy làm như sau (với lib sqlite3, lib khác sẽ dùng cú pháp khác)

```
query = "SELECT name, age FROM table WHERE name=? and age=?"
c.execute(query, (name,age))
```

Chú ý này có ghi trong tất cả các tài liệu của thư viện để dùng database, điều đáng buồn là lập trình viên thường không hay đọc tài liệu chính thống :(

https://docs.python.org/3.8/library/sqlite3.html
https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries

các thư viện sẽ làm nhiệm vụ phòng chống SQL Injection giúp bạn.

## Ví dụ với các SQL database

### SQLite
SQLite là SQL DB được dùng nhiều nhất thế giới, nó có trên mọi thiết bị smartphone,
trong các trình duyệt, trên máy bay Airbus và cả trong standard library Python.

```python
import sqlite3                                                     # tạo connection (kết nối) - ở đây là mở file example.db
conn = sqlite3.connect('example.db')
# tạo cursor
c = conn.cursor()

# chạy lệnh SQL để tạo table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# thêm 2 dòng vào table
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
c.execute("INSERT INTO stocks VALUES ('2006-01-06','SELL','PYMI',69,3.14)")
# Save (commit) thay đổi
conn.commit()

for row in c.execute("SELECT * FROM stocks WHERE symbol='RHAT'").fetchall():
    print(row)
# Luôn đóng connection sau khi đã xong việc
conn.close()

```

Output

```
[('2006-01-05', 'BUY', 'RHAT', 100.0, 35.14)]
```

### Postgres
Postgres là RDBMS mã nguồn mở/miễn phí hiện đại nhất.
Postgres phổ biến sau thời MySQL, nhưng ngày nay thường được chọn làm DB mặc
định khi lập trình web.

https://www.psycopg.org/
```
pip install psycopg2
```

https://www.psycopg.org/docs/usage.html
```
import psycopg2

conn = psycopg2.connect("dbname=test user=hvn")
cur = conn.cursor()
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
cur.execute("SELECT * FROM test;")
print(cur.fetchone())
100, "abc'def")
conn.commit()
cur.close()
conn.close()
```
Output
```
(1, 100, "abc'def")
```

### ORM: TODO

## NoSQL
### Redis
### Elastisearch
### MongoDB
