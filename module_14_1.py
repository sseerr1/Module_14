import sqlite3

# Создаем и подключаемся к базе данных not_telegram.db
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создаем таблицу Users, если она ещё не создана
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

# Заполняем таблицу 10 записями с помощью цикла
for i in range(1, 11):
    username = f'User{i}'
    email = f'example{i}@gmail.com'
    age = i * 10  # Пример возраста (10, 20, ..., 100)
    balance = 1000  # Начальный баланс
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
    ''', (username, email, age, balance))

# Обновляем баланс каждой 2-й записи на 500 через цикл
for user_id in range(1, 11, 2):  # Проходим по id 1, 3, 5, 7, 9
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, user_id))

# Получаем все id пользователей для удаления
cursor.execute('SELECT id FROM Users')
user_ids = cursor.fetchall()
# Удаляем каждую 3-ю запись, начиная с 1-й
for i in range(len(user_ids)):
    if (i + 1) % 3 == 1:  # Удаляем каждую третью запись, начиная с 1-й
        cursor.execute('DELETE FROM Users WHERE id = ?', (user_ids[i][0],))

# Выбираем все записи с возрастом не равным 60
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
rows = cursor.fetchall()

# Выводим результаты в консоль
for row in rows:
    username, email, age, balance = row
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# Закрываем соединение с базой данных
connection.commit()
connection.close()