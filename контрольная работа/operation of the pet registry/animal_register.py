class Counter:
    def __init__(self):
        self._count = 0
        self._is_open = True

    def add(self):
        if not self._is_open:
            raise RuntimeError("Counter is not open.")
        self._count += 1

    def get_count(self):
        if not self._is_open:
            raise RuntimeError("Counter is not open.")
        return self._count

    def __enter__(self):
        if not self._is_open:
            raise RuntimeError("Counter is already closed.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if not self._is_open:
            raise RuntimeError("Counter is already closed.")
        self._is_open = False
        # Handle exception if necessary
        if exc_type:
            print(f"Exception type: {exc_type}, value: {exc_value}")

# Пример использования

try:
    with Counter() as counter:
        counter.add()
        counter.add()
        print(f"Current count: {counter.get_count()}")
        # Убедимся, что ресурс открыт
        # counter.add()  # Это вызовет RuntimeError, если убрать комментарий
except RuntimeError as e:
    print(f"RuntimeError: {e}")

# Попробуем использовать объект вне блока with
try:
    counter = Counter()
    counter.add()  # Это должно работать
    print(f"Count before closing: {counter.get_count()}")
    # Закроем ресурс вручную
    counter.__exit__(None, None, None)
    # Попробуем добавить после закрытия
    counter.add()  # Это вызовет RuntimeError
except RuntimeError as e:
    print(f"RuntimeError: {e}")




class Animal:
    def __init__(self, name, species, date_of_birth, age, breed):
        self._name = name
        self._species = species
        self._date_of_birth = date_of_birth
        self._age = age
        self._breed = breed

    def get_info(self):
        return {
            "name": self._name,
            "species": self._species,
            "date_of_birth": self._date_of_birth,
            "age": self._age,
            "breed": self._breed
        }

class DomesticAnimal(Animal):
    def __init__(self, name, species, date_of_birth, age, breed):
        super().__init__(name, species, date_of_birth, age, breed)
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def get_commands(self):
        return self._commands

class PackAnimal(Animal):
    def __init__(self, name, species, date_of_birth, age, breed):
        super().__init__(name, species, date_of_birth, age, breed)
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def get_commands(self):
        return self._commands

class Dog(DomesticAnimal):
    def __init__(self, name, date_of_birth, age, breed):
        super().__init__(name, "Dog", date_of_birth, age, breed)

class Cat(DomesticAnimal):
    def __init__(self, name, date_of_birth, age, breed):
        super().__init__(name, "Cat", date_of_birth, age, breed)

class Hamster(DomesticAnimal):
    def __init__(self, name, date_of_birth, age, breed):
        super().__init__(name, "Hamster", date_of_birth, age, breed)

class Horse(PackAnimal):
    def __init__(self, name, date_of_birth, age, breed):
        super().__init__(name, "Horse", date_of_birth, age, breed)

class Camel(PackAnimal):
    def __init__(self, name, date_of_birth, age, breed):
        super().__init__(name, "Camel", date_of_birth, age, breed)

class Donkey(PackAnimal):
    def __init__(self, name, date_of_birth, age, breed):
        super().__init__(name, "Donkey", date_of_birth, age, breed)

import mysql.connector
from mysql.connector import Error

# Функция создания соединения с БД
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='mans_friends',
            user='root',
            password='1111'
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Функция добавления записи в таблицу AllAnimals
def add_animal(connection, animal):
    info = animal.get_info()
    commands = ', '.join(animal.get_commands())
    
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO AllAnimals (name, species, date_of_birth, age, breed, commands)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (info['name'], info['species'], info['date_of_birth'], info['age'], info['breed'], commands))
        connection.commit()
        print(f"Запись животного {info['name']} была успешно добавлена.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()

# Функция добавления команды для животного
def add_command_to_animal(connection, name, new_command):
    try:
        cursor = connection.cursor()
        query = "SELECT id, commands FROM AllAnimals WHERE name = %s"
        cursor.execute(query, (name,))
        animal = cursor.fetchone()

        if animal:
            animal_id, existing_commands = animal
            updated_commands = existing_commands + ', ' + new_command if existing_commands else new_command
            
            query = "UPDATE AllAnimals SET commands = %s WHERE id = %s"
            cursor.execute(query, (updated_commands, animal_id))
            connection.commit()
            print(f"Команда '{new_command}' была добавлена для животного {name}.")
        else:
            print(f"Животное с именем {name} не найдено.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()

# Функция просмотра команд для животного
def view_animal_commands(connection, name):
    try:
        cursor = connection.cursor()
        query = "SELECT commands FROM AllAnimals WHERE name = %s"
        cursor.execute(query, (name,))
        animal = cursor.fetchone()

        if animal:
            commands = animal[0]
            print(f"Команды для животного {name}: {commands}" if commands else f"Животное {name} не имеет команд.")
        else:
            print(f"Животное с именем {name} не найдено.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()

# Функция получения и отображения всех записей из таблицы AllAnimals
def fetch_and_display_animals(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM AllAnimals"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        if rows:
            print("Записи из таблицы AllAnimals:")
            for row in rows:
                print(row)
        else:
            print("В таблице AllAnimals нет записей.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()

# Функция закрытия соединения с БД
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Connection closed")

# Основная функция
def main():
    connection = create_connection()
    if connection:
        counter = Counter()  # Создание экземпляра счетчика
        try:
            while True:
                print("\nМеню:")
                print("1. Добавить запись в таблицу AllAnimals")
                print("2. Вывести все записи из таблицы AllAnimals")
                print("3. Добавить команду для животного")
                print("4. Просмотреть команды для животного")
                print("5. Выйти")
                
                choice = input("Выберите пункт меню: ")
                
                if choice == '1':
                    print("Введите информацию о животном:")
                    name = input("Имя: ")
                    species = input("Вид: ")
                    date_of_birth = input("Дата рождения (YYYY-MM-DD): ")
                    age = input("Возраст: ")
                    breed = input("Порода: ")
                    animal_type = input("Тип (домашнее/вьючное): ").strip().lower()
                    
                    if animal_type == "домашнее":
                        species_dict = {"dog": Dog, "cat": Cat, "hamster": Hamster}
                    elif animal_type == "вьючное":
                        species_dict = {"horse": Horse, "camel": Camel, "donkey": Donkey}
                    else:
                        print("Неверный тип животного.")
                        continue
                    
                    animal_class = species_dict.get(species.lower())
                    if animal_class:
                        animal = animal_class(name, date_of_birth, age, breed)
                        add_animal(connection, animal)
                        with counter as c:
                            c.add()
                            print(f"Количество заведенных животных: {c.get_count()}")
                    else:
                        print("Неверный вид животного.")
                    
                elif choice == '2':
                    fetch_and_display_animals(connection)
                    
                elif choice == '3':
                    name = input("Введите имя животного: ")
                    new_command = input("Введите новую команду: ")
                    add_command_to_animal(connection, name, new_command)
                    
                elif choice == '4':
                    name = input("Введите имя животного: ")
                    view_animal_commands(connection, name)
                    
                elif choice == '5':
                    print("Выход из программы.")
                    break
                    
                else:
                    print("Неверный выбор. Попробуйте снова.")
        
        except RuntimeError as e:
            print(f"RuntimeError: {e}")

        finally:
            close_connection(connection)

if __name__ == "__main__":
    main()