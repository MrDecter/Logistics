import sqlite3
import time

# Создание Базы
db = sqlite3.connect('item.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS AllItem (
    name TEXT,
    pieces INTEGER
    )""")
db.commit()


# Функции

# Добавление товара
def AddItem(item, pieces):
    Up_item = item.upper()
    sql.execute(f"SELECT name FROM AllItem WHERE name = '{Up_item}'")
    if sql.fetchone() is None:
        sql.execute(f'INSERT INTO AllItem VALUES(?,?)', (Up_item, pieces))
        db.commit()
        print("Товар добавлен!")
        ViewTable(f"{Up_item}")
        # Добавить функцию вывода еденичного товара
    else:
        print('Такой товар уже есть!')
        time.sleep(1)
        logs = input('Добавить колличество к этому товару? (Да\Нет)\n').lower()
        # Изменение кол-во товара
        if logs == "да":
            pieces_item = sql.execute(f'SELECT pieces FROM AllItem WHERE name = "{item}"').fetchone()
            sum_pieces = pieces_item[0] + int(f"{pieces}")
            sql.execute(f'DELETE FROM AllItem WHERE name = "{item}"')
            sql.execute(f'INSERT INTO AllItem VALUES(?,?)', (item, sum_pieces))
            db.commit()
            print('Кол-во товара измененно!')
            print(sql.execute(f"SELECT * FROM AllItem").fetchall())
        elif logs == "нет":
            print('Возврат в меню')
            time.sleep(1)
        else:
            print("Error")


# Удаление товара
# Отображение остатков
# Расчет маржи
# Корректное отображение одного товара
def ViewTable(name_item):
    string_up = name_item.upper()
    table = sql.execute(f"SELECT * FROM AllItem WHERE name = '{string_up}'").fetchall()
    q = 0
    i = 0
    while q != len(table):
        while i != 2:
            if i == 0:
                print('Название: ' + table[q][i])
                i += 1
            elif i == 1:
                print('Кол-во: ' + str(table[q][i]))
                i += 1
            else:
                print("Error")
        q += 1
    return string_up


# Корректное отображение всей таблицы
def ViewAllTable():
    table = sql.execute("SELECT * FROM AllItem").fetchall()
    q = 0
    i = 0
    while q != len(table):
        print("---------------")
        while i != 2:
            if i == 0:
                print('Название: ' + table[q][i])
                i += 1
            elif i == 1:
                print('Кол-во: ' + str(table[q][i]))
                i += 1
            else:
                print("Error")
        q += 1
        i -= 2


# Меню
def menu():
    logist = int(input("1. Добавить товар\n2. Посмотреть все товары\n3. Посмотреть остатки товара\n"))
    if logist == 1:
        menu_item = input("Введите название товара: ")
        menu_pic = int(input("Введите кол-во товара: "))
        AddItem(menu_item,menu_pic)
    elif logist == 2:
        ViewAllTable()
    elif logist == 3:
        menu_name = input('Введите название товара: ')
        ViewTable(menu_name)
    else:
        print("Error")


# Запуск
print("Добро пожаловать!")
menu()
