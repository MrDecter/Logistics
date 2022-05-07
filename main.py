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

"""

Провести оптимизацию:
-Случайные нажатия, 
-Отработка ошибок
-И наконец то убрать лишние else 
"""


# Функции

def add_pieces(code, pieces):
    """Функция добавление колличества товара, если он уже есть"""

    item = sql.execute('SELECT * FROM AllItem WHERE code = ?', (code,)).fetchone()
    sum_item = int(item[2]) + int(pieces)
    sql.execute('UPDATE AllItem SET pieces = ? WHERE code = ?', (sum_item, code))
    print('Кол-во товара изменено')
    view_table(f"{code}")


def add_item(code, item, pieces, price):
    """Функция добавление товара в SQL"""

    Up_item = item.upper()
    sql.execute("SELECT code FROM AllItem WHERE code = ?", (code,))
    if sql.fetchone() is None:
        sql.execute('INSERT INTO AllItem VALUES(?,?,?,?)', (code, Up_item, pieces, price))
        db.commit()
        print("Товар добавлен!")
        view_table(f"{code}")
    else:
        print('Такой код товара уже есть!')
        time.sleep(1)
        logs = int(input('Добавить указанное кол-во в товар: ' + f"{item}" + " ?\n1. Да\n2. Нет\n"))
        if logs == 1:
            add_pieces(f"{code}", f"{pieces}")
        elif logs == 2:
            print('Выход в меню')
            time.sleep(2)
        else:
            print('Error')
    print("Возврат в меню")
    time.sleep(1)
    menu()


def delete_item(code):
    """Функция удаление товара из SQL по его коду"""

    sql.execute(f"DELETE FROM AllItem WHERE code = ?", (code,))
    print("Товар удален!")
    print("Возврат в меню")
    time.sleep(1)
    menu()


def view_table(words, flag=True, item_code=0):
    """Функция отображение товаров из SQL"""

    if flag:
        table = sql.execute("SELECT * FROM AllItem WHERE code = ?", (item_code,)).fetchall()
    else:
        table = sql.execute("SELECT * FROM AllItem ORDER BY code").fetchall()
    q = 0
    i = 0
    p = "-----------"
    while q != len(table):
        print(p)
        while i != 4:
            print(words[i] + str(table[q][i]))
            i += 1
        i -= 4
        q += 1
    print("\nВозврат в меню")
    time.sleep(1)
    menu()


def menu():
    """Функция управления"""

    menu_manage = int(input(
        "1. Добавить товар\n2. Посмотреть все товары\n3. Посмотреть остатки товара\n4. Удалить товар\n5. Выход\n"))
    if menu_manage == 1:
        sql_code = int(input("Введите код товара: "))
        sql_name = input("Введите название товара: ")
        sql_pieces = int(input("Введите кол-во товара: "))
        sql_price = int(input("Введите стоимость товара за шт: "))
        add_item(sql_code, sql_name, sql_pieces, sql_price)

    elif menu_manage == 2:
        words = ["Код: ", "Название: ", "Кол-во: ", "Цена за шт: "]
        view_table(words, flag=False)

    elif menu_manage == 3:
        sql_code = int(input('Введите код товара: '))
        words = ["Код: ", "Название: ", "Кол-во: ", "Цена за шт: "]
        view_table(words, item_code=sql_code)

    elif menu_manage == 4:
        menu_del = input('Введите код удаляемого товара: ')
        delete_item(menu_del)

    elif menu_manage == 5:
        print("Всего доброго!")
        time.sleep(3)

    else:
        print("Error")


# Запуск
print("Добро пожаловать!")
menu()

