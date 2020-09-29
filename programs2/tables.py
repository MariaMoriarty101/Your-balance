import sqlite3
conn = sqlite3.connect('incomes.db')

c = conn.cursor()
c.execute("""CREATE TABLE Money(
                Balance float
            )""")

c.execute("""CREATE TABLE Incomes(
            Name text,
            Pay float,
            Comment text
        )""")

c.execute("""CREATE TABLE Food(
            Name text,
            Price float,
            Comment NULL
        )""")

c.execute("""CREATE TABLE Transport(
            Name text,
            Price float,
            Comment NULL
        )""")

c.execute("""CREATE TABLE House(
            Name text,
            Price float,
            Comment NULL
        )""")

c.execute("""CREATE TABLE Health(
            Name text,
            Price float,
            Comment NULL
        )""")

c.execute("""CREATE TABLE Clothes(
            Name text,
            Price float,
            Comment NULL
        )""")



conn.commit()
conn.close()
