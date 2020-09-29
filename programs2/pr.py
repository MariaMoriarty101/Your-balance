import sys, os
import sqlite3
#doc.close()

money = 0

while True:
    first = int(input("Choose option: \n\n 1 - Income\n 2 - Costs\n\n"))

    if first==1:
        second = int(input("\n\n\nChoose option: \n\n 1 - Write a Coment\n 2 - No Coment\n\n"))

        if second == 1:
            comun = int(input("Write below your income:\n\n"))
            coment = input("Write below your coment:\n\n")
            money += comun
            doc = open("list.txt", "w")
            doc.write(str(comun) + "\n" + coment + "\n")
            doc.close()

        elif second == 2:
            comun = int(input("Write below your income:\n\n"))
            money += comun
            doc = open("list.txt", "a")
            doc.write(str(comun) + "\nNo Coment" + "\n")
            doc.close()

        elif second == 3:
            break

    elif first == 2:
        third = int(input("\n\n\nChoose option: \n\n 1 - Food\n 2 - Transport\n 3 - House\n 4 - Enterteiment\n 5 - Health\n 6 - Chothes\n\n\n"))
        if third == 1:
            comun = int(input("Write below your cost:\n\n"))
            coment = input("Write below your coment:\n\n")
            money -= comun
            doc = open("list.txt", "w")
            doc.write(str(comun) + "\n" + "FOOD " + coment + "\n")
            doc.close()

        elif third == 2:
            comun = int(input("Write below your cost:\n\n"))
            coment = input("Write below your coment:\n\n")
            money -= comun
            doc = open("list.txt", "w")
            doc.write(str(comun) + "\n" + "TRANSPORT " + coment + "\n")
            doc.close()

        elif third == 3:
            comun = int(input("Write below your cost:\n\n"))
            coment = input("Write below your coment:\n\n")
            money -= comun
            doc = open("list.txt", "w")
            doc.write(str(comun) + "\n" + "HOUSE " + coment + "\n")
            doc.close()

        elif third == 4:
            comun = int(input("Write below your cost:\n\n"))
            coment = input("Write below your coment:\n\n")
            money -= comun
            doc = open("list.txt", "w")
            doc.write(str(comun) + "\n" + "ENTERTEIMENT " + coment + "\n")
            doc.close()

        elif third == 5:
            comun = int(input("Write below your cost:\n\n"))
            coment = input("Write below your coment:\n\n")
            money -= comun
            doc = open("list.txt", "w")
            doc.write(str(comun) + "\n" + "HEALTH " + coment + "\n")
            doc.close()

        elif third == 6:
            comun = int(input("Write below your cost:\n\n"))
            coment = input("Write below your coment:\n\n")
            money -= comun
            doc = open("list.txt", "w")
            doc.write(str(comun) + "\n" + "CLOTHES " + coment + "\n")
            doc.close()

        else:
            print (money)
            break
    else: break


#value = input("Enter the text\n")
#doc.write(value)
