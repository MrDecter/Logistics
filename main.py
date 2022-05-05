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
def AddItem(item,pieces):
    sql.execute(f"SELECT name FROM AllItem WHERE name = '{item}'")
    if sql.fetchone() is None:
        sql.execute(f'INSERT INTO AllItem VALUES(?,?)', (item, pieces))
        db.commit()
        print("Товар добавлен!")
        print(sql.execute(f"SELECT * FROM AllItem").fetchall())
    else:
        print('Такой рецепт уже есть!')
        time.sleep(2)
        logs = input('Добавить колличество к этому товару? (Да\Нет)\n').lower()
        if logs == "да":
            sql.execute(f'INSERT INTO AllItem VALUES(?,?)', (item, {}))
            print(sql.execute(f'SELECT * FROM AllItem WHERE name = "{item}"'))
        else:
            print('Error')



# Удаление товара
# Отображение остатков
# Расчет маржи
# Вывод всех товаров

# Запуск
# Меню
its = input('Наименование товара: ').upper()
cos = int(input('Кол-во товара: '))
AddItem(its,cos)