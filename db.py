import sqlite3 as sql

# создание базы данных
def create_db(path):
    connect = sql.connect(path)
    cursor = connect.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pwd TEXT,
            salt TEXT,
            num_char INTEGER,
            result TEXT
        );
        """
    )
    connect.commit()
    connect.close

# функция записи данных в базу данных
def write_db(path, data):
    connect = sql.connect(path)
    cursor = connect.cursor()
    cursor.executemany("INSERT INTO logs (pwd, salt, num_char, result) VALUES (?,?,?,?);", data)
    connect.commit()
    connect.close()

# чтение данных из базы данных
def read_db(path):
    connect = sql.connect(path)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM logs;")
    return cursor.fetchall()

# тестирование
# path = "test.db"
# create_db(path)
# write_db(path, [("qwerty", "mail", 7, "asfdgfdw"), ("qwer1423", "vk", 10, "qwqyweft")])
# print(read_db(path))