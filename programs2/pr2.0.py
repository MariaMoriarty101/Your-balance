import sys, os
import sqlite3

conn = sqlite3.connect('incomes.db')
c = conn.cursor()
money = 0

while True:
    first = int(input("Choose option: \n\n 1 - Income\n 2 - Costs\n\n"))

    if first==1:
            incomes = [((input("name\n")), (input("pay\n")), (input("comment\n")))]
            c.executemany("INSERT INTO Incomes VALUES (?,?,?)", incomes)
            conn.commit()
        #    c.execute("INSERT INTO Money SELECT SUM(Pay) FROM Incomes")
        #    conn.commit()


    elif first == 2:
        third = int(input("\n\n\nChoose option: \n\n 1 - Food\n 2 - Transport\n 3 - House \n 4 - Health\n 5 - Chothes\n\n\n"))
        if third == 1:
            incomes = [((input("Name\n")), (input("Price\n")), (input("Comment\n")))]
            c.executemany("INSERT INTO Food VALUES (?,?,?)", incomes)
            conn.commit()
        #    c.execute("INSERT INTO Money SELECT SUM(Price) from Food")
        #    conn.commit()



        elif third == 2:
            incomes = [((input("Name\n")), (input("Price\n")), (input("Comment\n")))]
            c.executemany("INSERT INTO Transport VALUES (?,?,?)", incomes)
            conn.commit()
            c.execute("SELECT SUM(Price) from Transport")
            helpv = c.fetchone()
            money -= helpv[0]

        elif third ==3:
            incomes = [((input("Name\n")), (input("Price\n")), (input("Comment\n")))]
            c.executemany("INSERT INTO House VALUES (?,?,?)", incomes)
            conn.commit()
            c.execute("SELECT SUM(Price) from House")
            helpv = c.fetchone()
            money -= helpv[0]

        elif third == 4:
            incomes = [((input("Name\n")), (input("Price\n")), (input("Comment\n")))]
            c.executemany("INSERT INTO Health VALUES (?,?,?)", incomes)
            conn.commit()
            c.execute("SELECT SUM(Price) from Health")
            helpv = c.fetchone()
            money -= helpv[0]

        elif third == 5:
            incomes = [((input("Name\n")), (input("Price\n")), (input("Comment\n")))]
            c.executemany("INSERT INTO Clothes VALUES (?,?,?)", incomes)
            conn.commit()
            c.execute("SELECT SUM(Price) from Clothes")
            helpv = c.fetchone()
            money -= helpv[0]
        else:
        #    c.execute("UPDATE Money SET Balance = Income WHERE Income IN (Select SUM(Pay) AS Income FROM Incomes)" )
        #    c.execute("UPDATE Money SET Balance = Costs  WHERE -SUM(Price) AS Costs FROM Food")





            c.execute(" SELECT SUM(Balance) FROM Money")
            helpv = c.fetchone()
            money -= helpv[0]
            print ("\n\n\n\n Your balance is " + str(money))
            break
    else:
        c.execute(" SELECT SUM(Money) FROM Money")
        helpv = c.fetchone()
        money -= helpv[0]
        print ("\n\n\n\n Your balance is " + str(money))
        break
