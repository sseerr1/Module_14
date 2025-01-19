import sqlite3


def initiate_db():
    connection = sqlite3.connect('initiate_db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL, 
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

    connection.commit()
    connection.close()


##############################################################
def add_user(username, email, age):
    connection = sqlite3.connect('initiate_db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)",
                   (username, email, age))
    connection.commit()
    connection.close()


def is_included(username_or_email):
    connection = sqlite3.connect('initiate_db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Users WHERE username = ? OR email = ?",
                   (username_or_email, username_or_email))
    result = cursor.fetchone()
    connection.close()
    return result is not None


#################################################################

def insert_products():
    for i in range(1, 5):
        id = i
        title = f'Продукт {i}'
        description = f'Описание {i}'
        price = i * 100
        connection = sqlite3.connect('initiate_db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)
         ''', (id, title, description, price))
        connection.commit()
        connection.close()


def get_all_products():
    connection = sqlite3.connect('initiate_db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    connection.commit()
    prod = cursor.fetchall()
    connection.commit()
    connection.close()
    return prod


initiate_db()
# insert_products()
# get_all_products()
# if __name__ == "__main__":
