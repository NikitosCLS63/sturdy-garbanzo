

import sqlite3

class Product:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

class Order:
    def __init__(self, product, quantity, status):
        self.product = product
        self.quantity = quantity
        self.status = status
        
class Registration:
    def __init__(self):
        self.customers = []

    def register_customer(self, name):
        new_customer = Customer(input[name])
        self.customers.append(new_customer)
        return new_customer

    registration = Registration()
    new_customer = registration.register_customer("customer2")
    print(new_customer.name)  # Output: customer2      
          

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def view_items(self):
        for item in self.items:
            print(item)

# Создаем экземпляр класса Registration и регистрируем нового покупателя
registration = Registration()
new_customer = registration.register_customer("customer2")

# Создаем экземпляр класса ShoppingCart
shopping_cart = ShoppingCart()

# Добавляем товары в корзину покупок
shopping_cart.add_item("item1")
shopping_cart.add_item("item2")

# Просмотр содержимого корзины покупок
shopping_cart.view_items()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class ShoeStoreSystem:
    def __init__(self):
        self.conn = sqlite3.connect('shoe_store.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            brand TEXT,
                            price REAL)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                            id INTEGER PRIMARY KEY,
                            product_id INTEGER,
                            quantity INTEGER,
                            status TEXT,
                            FOREIGN KEY (product_id) REFERENCES products(id))''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            email TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT,
                            password TEXT)''')
        self.conn.commit()

    def add_product(self, product):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO products (name, brand, price) VALUES (?, ?, ?)', (product.name, product.brand, product.price))
        self.conn.commit()

    def update_product_price(self, product_id, new_price):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        self.conn.commit()

    def get_products_by_brand(self, brand):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM products WHERE brand = ?', (brand,))
        return cursor.fetchall()

    # другие методы для управления заказами и клиентами

    def register_user(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        self.conn.commit()

    def login_user(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        return cursor.fetchone() is not None

    # другие методы для авторизации и регистрации

    def __del__(self):
        self.conn.close()

# Пример использования
        system = ShoeStoreSystem()
        nike_Air_Max = Product('Air Max', 'Nike', 150.00)
        system.add_product(nike_Air_Max)
        system.update_product_price(1, 160.00)
        system.delete_product(1)

        system = ShoeStoreSystem()
        nike_Dank = Product('Dank', 'Nike', 140.00)
        system.add_product(nike_Dank)
        system.update_product_price(1, 160.00)
        system.delete_product(1)

        system = ShoeStoreSystem()
        nike_Air_Force = Product('Air Force', 'Nike', 160.00)
        system.add_product(nike_Air_Force)
        system.update_product_price(1, 190.00)
        system.delete_product(1)
