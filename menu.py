import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('shop.db')

# Создаем курсор для выполнения операций с базой данных
cursor = conn.cursor()

# Создаем таблицу "employees" для хранения информации о сотрудниках
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY, name TEXT, position TEXT, salary REAL)''')

# Создаем таблицу "products" для хранения информации о товарах
cursor.execute('''CREATE TABLE IF NOT EXISTS products
                  (id INTEGER PRIMARY KEY, name TEXT, price REAL, quantity INTEGER)''')

# Функция для добавления нового сотрудника
def add_employee(name, position, salary):
    cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", (name, position, salary))
    conn.commit()
    print("Сотрудник успешно добавлен!")

# Функция для удаления сотрудника по ID
def delete_employee(employee_id):
    cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
    conn.commit()
    print("Сотрудник успешно удален!")

# Функция для добавления нового товара
def add_product(name, price, quantity):
    cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
    conn.commit()
    print("Товар успешно добавлен!")

# Функция для удаления товара по ID
def delete_product(product_id):
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    print("Товар успешно удален!")

# Функция для вывода списка сотрудников
def show_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    for employee in employees:
        print(f"ID: {employee[0]}, Имя: {employee[1]}, Должность: {employee[2]}, Зарплата: {employee[3]}")

# Функция для вывода списка товаров
def show_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}")

# Пример использования функций
add_employee("Иван Иванов", "Менеджер", 50000)
add_employee("Петр Петров", "Продавец", 30000)
add_product("Телефон", 10000, 10)
add_product("Ноутбук", 50000, 5)
show_employees()
show_products()
delete_employee(1)
delete_product(1)
show_employees()
show_products()

# Закрываем соединение с базой данных
conn.close()
