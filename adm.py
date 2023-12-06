class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Admin(User):
    def create_user(self, username, password, role):
        # Создание нового пользователя
        new_user = User(username, password, role)
        # Добавление нового пользователя в базу данных или другое хранилище
        
    def update_user(self, username, new_password, new_role):
        # Изменение данных пользователя
        # Найти пользователя в базе данных по имени пользователя
        # Обновить пароль и роль пользователя
        
    def delete_user(self, username):
        # Удаление пользователя
        # Найти пользователя в базе данных по имени пользователя
        # Удалить пользователя из базы данных
        
    def assign_role(self, username, new_role):
        # Присвоение новой роли пользователю
        # Найти пользователя в базе данных по имени пользователя
        # Обновить роль пользователя

class Operator(User):
    def create_user(self, username, password, role):
        # Создание нового пользователя
        new_user = User(username, password, role)
        # Добавление нового пользователя в базу данных или другое хранилище
        
    def update_user(self, username, new_password, new_role):
        # Изменение данных пользователя
        # Найти пользователя в базе данных по имени пользователя
        # Обновить пароль и роль пользователя
        
    def delete_user(self, username):
        # Удаление пользователя
        # Найти пользователя в базе данных по имени пользователя
        # Удалить пользователя из базы данных
        
    def assign_role(self, username, new_role):
        # Присвоение новой роли пользователю
        # Найти пользователя в базе данных по имени пользователя
        # Обновить роль пользователя