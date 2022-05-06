import sqlite3
import time

# Создание Базы
db = sqlite3.connect('item.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS AllItem (
    code INTEGER,
    name TEXT,
    pieces INTEGER,
    price INTEGER
    )""")
db.commit()


# Функции

# Расчет маржи
# Добавление кол-во товара
def AddPieces(code,pieces):
    item = sql.execute(f'SELECT * FROM AllItem WHERE code = "{code}"').fetchone()
    sum = int(item[2]) + int(pieces)
    sql.execute(f'UPDATE AllItem SET pieces = "{sum}" WHERE code = "{code}"')
    print('Кол-во товара изменено')
    ViewTable(f"{code}")






# Добавление товара
def AddItem(code, item, pieces, price):
    Up_item = item.upper()
    sql.execute(f"SELECT code FROM AllItem WHERE code = '{code}'")
    if sql.fetchone() is None:
        sql.execute(f'INSERT INTO AllItem VALUES(?,?,?,?)', (code, Up_item, pieces,price))
        db.commit()
        print("Товар добавлен!")
        ViewTable(f"{code}")
    else:
        print('Такой код товара уже есть!')
        time.sleep(1)
        logs = int(input('Добавить указанное кол-во в товар: ' + f"{item}" + " ?\n1. Да\n2. Нет\n"))
        if logs == 1:
            AddPieces(f"{code}",f"{pieces}")
        elif logs == 2:
            print('Выход в меню')
            time.sleep(2)
        else:
            print('Error')
    print("Возврат в меню")
    time.sleep(1)
    menu()


# Удаление товара
def DeleteItem(code):
    sql.execute(f"DELETE FROM AllItem WHERE code = '{code}'")
    print("Товар удален!")
    print("Возврат в меню")
    time.sleep(1)
    menu()



# Корректное отображение остатков товара
def ViewTable(item_code):
    table = sql.execute(f"SELECT * FROM AllItem WHERE code = '{item_code}'").fetchall()
    q = 0
    i = 0
    while q != len(table):
        while i != 4:
            if i == 0:
                print('Код: ' + str(table[q][i]))
                i += 1
            elif i == 1:
                print('Название: ' + str(table[q][i]))
                i += 1
            elif i == 2:
                print('Кол-во: ' + str(table[q][i]))
                i += 1
            elif i == 3:
                print('Стоимость за шт: ' + str(table[q][i]) + 'р.')
                i += 1
            else:
                print("Error")
        q += 1
    print("\nВозврат в меню")
    time.sleep(1)
    menu()


# Корректное отображение всей таблицы
def ViewAllTable():
    table = sql.execute("SELECT * FROM AllItem ORDER BY code").fetchall()
    q = 0
    i = 0
    while q != len(table):
        print("---------------")
        while i != 4:
            if i == 0:
                print('Код: ' + str(table[q][i]))
                i += 1
            elif i == 1:
                print('Название: ' + str(table[q][i]))
                i += 1
            elif i == 2:
                print('Кол-во: ' + str(table[q][i]))
                i += 1
            elif i == 3:
                print('Цена: ' + str(table[q][i]) + 'р.')
                i += 1
            else:
                print("Error")
        q += 1
        i -= 4
    print("\nВозврат в меню")
    time.sleep(1)
    menu()


# Меню
def menu():
    logist = int(input("1. Добавить товар\n2. Посмотреть все товары\n3. Посмотреть остатки товара\n4. Удалить товар\n5. Выход\n"))
    if logist == 1:
        menu_code = int(input("Введите код товара: "))
        menu_item = input("Введите название товара: ")
        menu_pic = int(input("Введите кол-во товара: "))
        menu_price = int(input("Введите стоимость товара за шт: "))
        AddItem(menu_code, menu_item, menu_pic, menu_price)
    elif logist == 2:
        ViewAllTable()
    elif logist == 3:
        menu_name = int(input('Введите код товара: '))
        ViewTable(menu_name)
    elif logist == 4:
        menu_del = input('Введите код удаляемого товара: ')
        DeleteItem(menu_del)
    elif logist == 5:
        print("Всего доброго!")
        time.sleep(3)
    else:
        print("Error")


# Запуск
print("Добро пожаловать!")
menu()
