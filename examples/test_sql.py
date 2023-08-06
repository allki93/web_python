# Система управления базами данных (СУБД) CQLite

import sqlite3 as sql

# соединение с базой данных
conn = sql.connect("test.db")

# курсор - панель управления базой данных
cursor = conn.cursor()

# создание таблицы
sql_cmd = """create table if not exists users (
    user_id int primary key,
    f_name text,
    l_name text,
    age real,
    gender text
);"""
cursor.execute(sql_cmd)
conn.commit()

# запись данных
# одна строка
# sql_cmd = "INSERT INTO users VALUES(?,?,?,?,?)"
# cursor.execute(sql_cmd, (0, "John", "Sherman", 24.5, "m"))
# conn.commit()

# много строк
# sql_cmd = "INSERT INTO users VALUES(?,?,?,?,?)"
# my_users = [
#     (1, "Peter", "Penn", 32.3, "m"),
#     (2, "Katrin", "Johnes", 25.0, "f"),
#     (3, "Lena", "Chan", 26.5, "f")
# ]
# cursor.executemany(sql_cmd, my_users)
# conn.commit()

# # чтение данных
# sql_cmd = "SELECT * FROM users;"
# cursor.execute(sql_cmd)
# # первая строка
# # result = cursor.fetchone()
# # все строки
# result = cursor.fetchall()
# print(result)

# # чтение определенных столбов
# sql_cmd = "SELECT user_id, f_name, age FROM users;"
# cursor.execute(sql_cmd)
# result = cursor.fetchall()
# print(result)

# # чтение определенных столбов с условием
# sql_cmd = "SELECT user_id, f_name, age FROM users WHERE age < 30 AND gender='f';"
# cursor.execute(sql_cmd)
# result = cursor.fetchall()
# print(result)

# # удаление данных
# sql_cmd = "DELETE FROM users WHERE l_name='Sherman'"
# cursor.execute(sql_cmd)
# conn.commit()

# # чтение данных
# sql_cmd = "SELECT * FROM users;"
# cursor.execute(sql_cmd)
# result = cursor.fetchall()
# print(result)

# создание 2 таблицы
sql_cmd = """create table if not exists orders (
    order_id int primary key,
    date text,
    user_id int,
    total real
);"""
cursor.execute(sql_cmd)
conn.commit()

# запись данных
# sql_cmd = "INSERT INTO orders VALUES(?,?,?,?)"
# orders = [
#     (0, "01-08-2023", 2, 100.23),
#     (1, "01-08-2023", 2, 10.2),
#     (2, "02-08-2023", 2, 360.45),
#     (3, "03-08-2023", 2, 240.23),
#     (4, "04-08-2023", 2, 60.3),
#     (5, "05-08-2023", 2, 70.53),
#     (6, "06-08-2023", 2, 230.23)
# ]
# cursor.executemany(sql_cmd, orders)
# conn.commit()

# # чтение данных из двух таблиц
# sql_cmd = "SELECT * FROM orders LEFT JOIN users ON orders.user_id=users.user_id;"
# sql_cmd = "SELECT * FROM users LEFT JOIN orders ON orders.user_id=users.user_id;"
# cursor.execute(sql_cmd)
# result = cursor.fetchall()
# print(result)

# sql_cmd = "SELECT * FROM users INNER JOIN orders ON orders.user_id=users.user_id;"
# cursor.execute(sql_cmd)
# result = cursor.fetchall()
# print(result)

sql_cmd = "SELECT * FROM users CROSS JOIN orders;"
cursor.execute(sql_cmd)
result = cursor.fetchall()
print(result)

conn.close()