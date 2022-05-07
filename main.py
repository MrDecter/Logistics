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

def add_pieces(code, pieces):
    """Функция добавление колличества товара, если он уже есть"""

    item = sql.execute('SELECT * FROM AllItem WHERE code = ?', (code,)).fetchone()
    sum_item = int(item[2]) + int(pieces)
    sql.execute('UPDATE AllItem SET pieces = ? WHERE code = ?', (sum_item, code))
    db.commit()
    print('Кол-во товара изменено')
    view_table(code)


def add_item(code, item, pieces, price):
    """Функция добавление товара в SQL"""

    Up_item = item.upper()
    sql.execute("SELECT code FROM AllItem WHERE code = ?", (code,))
    if sql.fetchone() is None:
        sql.execute('INSERT INTO AllItem VALUES(?,?,?,?)', (code, Up_item, pieces, price))
        db.commit()
        print("Товар добавлен!")
        view_table(code)
    else:
        print('Такой код товара уже есть!')
        time.sleep(1)
        logs = int(input('Добавить указанное кол-во в товар: ' + f"{item}" + " ?\n1. Да\n2. Нет\n"))
        if logs == 1:
            add_pieces(code, pieces)
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
            if i == 3:
                print(words[i] + str(table[q][i]) + " Руб.")
            else:
                print(words[i] + str(table[q][i]))
            i += 1
        i -= 4
        q += 1
    print("\nВозврат в меню")
    time.sleep(1)
    menu()


def calculation_goods(code, pieces):
    """Функция расчет стоимости при закупке товара"""
    item = sql.execute('SELECT * FROM AllItem WHERE code = ?', (code,)).fetchone()
    calculation_item = int(item[3]) * int(pieces)
    print("Рассчет стоимости: " + item[1] + "\nУказанная ранее стоимость за шт: " + str(item[3]) +
          "\nВедено кол-во для расчета: " + str(pieces) + "\nИтог: " + str(calculation_item) + " Руб.")


def variable_code():
    """Функция для изменения кода товара"""
    code = int(input("Введите код изменяемого товара: "))
    new_code = int(input("Введите код для изменения: "))
    sql.execute('UPDATE AllItem SET code = ? WHERE code = ?', (new_code, code))
    db.commit()
    time.sleep(2)
    print("Код товара изменен, возврат в меню...")
    time.sleep(2)
    menu()


def variable_name():
    """Функция для изменения имени товара"""
    code = int(input("Введите код изменяемого товара: "))
    new_name = int(input("Введите новое имя для изменения: "))
    sql.execute('UPDATE AllItem SET name = ? WHERE code = ?', (new_name, code))
    db.commit()
    time.sleep(2)
    print("Имя товара изменено, возврат в меню...")
    time.sleep(2)
    menu()


def variable_pieces():
    """Функция для изменения кол-ва товара"""
    code = int(input("Введите код изменяемого товара: "))
    new_pieces = int(input("Введите новое кол-во товара: "))
    sql.execute('UPDATE AllItem SET pieces = ? WHERE code = ?', (new_pieces, code))
    db.commit()
    time.sleep(2)
    print("Кол-во товара изменено, возврат в меню...")
    time.sleep(2)
    menu()


def variable_price():
    """Функция для изменения стоимости товара"""
    code = int(input("Введите код изменяемого товара: "))
    new_price = int(input("Введите новое цену для изменения: "))
    sql.execute('UPDATE AllItem SET price = ? WHERE code = ?', (new_price, code))
    db.commit()
    time.sleep(2)
    print("Стоимость товара изменена, возврат в меню...")
    time.sleep(2)
    menu()


def average_stock():
    """Формула расчета среднего запаса на складе"""

    print("Описание: Показатель может определяться как в натуральном, так и в стоимостном выражении,"
          " как в целом по складу, так и по группам товаров.")
    x = int(input("Введите кол-во запасов на начало первого периода: "))
    y = int(input("Введите кол-во запасов на конец первого периода: "))
    print("Рассчитываем....")
    time.sleep(1)
    z = (x + y) / 2
    print("Средний запас за первый перион: " + str(z))
    print("Возврат в меню...")
    time.sleep(2)
    menu()


def all_average_stock():
    """Формула расчета среднего запаса за несколько периодов"""

    x = int(input("Введите кол-во периодов: "))
    stock_list = []
    i = 1
    while len(stock_list) != x:
        stock_list.append(int(input("Введите " + str(i) + " значение периода: ")))
        i += 1
    print("Вычисляем...")
    time.sleep(2)
    z = len(stock_list)
    s = 0
    while z != -1:
        z -= 1
        s += stock_list[z]
    s = s / len(stock_list) - 1
    print("Средний запас из " + str(len(stock_list)) + " периодов: " + str(s))

    print("Возврат в меню...")
    time.sleep(2)
    menu()


def turnover_rate():
    """Формула для расчета скорости товарооборота"""
    print("Описание: Скорость товарооборота показывает, сколько раз в течение одного периода "
          "продается и возобновляется имеющийся товарный запас.")
    time.sleep(3)
    x = int(input("Введите скорость товарооборота за требуемый период: "))
    y = int(input('Cредний товарный запас за период: '))
    s = x / y
    print("Скорость товарооборота равна: " + str(s))
    time.sleep(2)
    print("Возврат в меню...")
    time.sleep(2)
    menu()


def appeal_item():
    """Формула для расчета времени обращения товаров"""
    print("Описание:  показывает продолжительность периода, в течение которого реализуется запас,"
          " время нахождения товаров в сфере обращения или на складе торгового предприятия.")
    time.sleep(3)
    x = int(input("Введите средние товарные запасы за период: "))
    y = int(input("Число дней в периоде: "))
    print('Вычисляем...')
    time.sleep(2)
    s = (x * y) / 0
    print("Время обращение товара: " + str(s))
    time.sleep(2)
    print("Возврат в меню...")
    time.sleep(2)
    menu()


def expenses():
    """Функция по расчету затрат на логистику, приходящиеся на единицу товарооборота"""
    print("Описание: Функция по расчету затрат на логистику, приходящиеся на единицу товарооборота")
    time.sleep(2)
    x = int(input('Введите затраты на логистику за период: '))
    y = int(input('Введите товарооборот за период: '))
    s = (x * y) / 100
    print("Затраты на единицу товарооборота: " + str(s))
    time.sleep(2)
    print("Возврат в меню...")
    time.sleep(2)
    menu()


def menu():
    """Функция управления"""
    print("\nМеню: ")
    menu_manage = int(input(
        "1. Добавить товар\n"
        "2. Посмотреть все товары\n"
        "3. Посмотреть остатки товара\n"
        "4. Удалить товар\n"
        "5. Рассчет стоимости закупки товара\n"
        "6. Изменить значения товара\n"
        "7. Формулы\n"
        "8. Выход\n"))
    try:
        if 0 < menu_manage < 9:
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
                sql_code = int(input('Введите код товара: '))
                pieces_item = int(input("Кол-во закупаемого товара : "))
                print("Рассчет....\n")
                time.sleep(2)
                calculation_goods(sql_code, pieces_item)

            elif menu_manage == 6:
                time.sleep(1)
                variable_parameter = int(input("\nНужно изменить: "
                                               "\n1. Код товара"
                                               "\n2. Название товара"
                                               "\n3. Кол-во товара"
                                               "\n4. Стоимость товара\n"))
                if variable_parameter == 1:
                    variable_code()
                elif variable_parameter == 2:
                    variable_name()
                elif variable_parameter == 3:
                    variable_pieces()
                elif variable_parameter == 4:
                    variable_price()
            elif menu_manage == 7:
                variable_formula = int(input("Какую формулу выбрать?"
                                             "\n1. Средний запас на складе\n"
                                             "2. Средний запас за несколько периодов складе\n"
                                             "3. Скорость товараоборота\n"
                                             "4. Время обращения товаров\n"
                                             "5. Затраты на логистику, приходящиеся на единицу товарооборота\n"))
                if variable_formula == 1:
                    average_stock()
                elif variable_formula == 2:
                    all_average_stock()
                elif variable_formula == 3:
                    turnover_rate()
                elif variable_formula == 4:
                    appeal_item()
                elif variable_formula == 5:
                    expenses()

            elif menu_manage == 8:
                print("Всего доброго!")
                time.sleep(3)

        else:
            print("Введено неверное значение, попробуйте снова")
            time.sleep(2)
            menu()
    except ValueError:
        print("Внимание: Ввод разрешен только числами, попробуйте снова...")
        time.sleep(2)
        menu()


# Запуск
print("Добро пожаловать в \'Lite-Logistic\'!")
time.sleep(2)
menu()
