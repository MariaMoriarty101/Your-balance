import sqlite3

conn = sqlite3.connect('incomes.db')

c = conn.cursor()

c.execute("DROP TABLE Incomes")
c.execute("DROP TABLE Food")
c.execute("DROP TABLE Transport")
c.execute("DROP TABLE House")
c.execute("DROP TABLE Health")
c.execute("DROP TABLE Clothes")
#conn.commit()

#incomes = [((input("name\n")), (input("pay\n")), (input("comment\n")))]

#c.executemany("INSERT INTO Incomes22 VALUES (?,?,?)", incomes)


#c.execute("SELECT * from Incomes")
c.execute("DROP TABLE Money")


conn.commit()
conn.close()
