import sqlite3
def  initiate_db():
    connection = sqlite3.connect('initiate_db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL, 
    description TEXT,
    price INT NOT NULL
    );
    ''')
    connection.commit()
    connection.close()
def insert_products():

    for i in range(1, 5):
        id=i
        title = f'Продукт {i}'
        description = f'Описание {i}'
        price = i*100
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
    # for i in prod:
    # id_, title, description, price = prod
    # #print(f"ID: {id_} | Наименование: {title} | Описание: {description} | Цена: {price}")
    return prod



    # id
    # title
    # description
    # price
    # count = cursor.execute('SELECT COUNT(*) FROM Products')

    #prod = cursor.fetchall()
    # return  cursor.fetchall()
    # all_products = cursor.fetchall()
    # for product in all_products:
    #return prod
    #id, title, description, price = [prod]
#     #get_all_products()
#     for i in range(len(prod)):
#


#initiate_db()
#insert_products()
get_all_products()
# if __name__ == "__main__":
