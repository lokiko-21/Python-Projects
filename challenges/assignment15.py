import sqlite3

firstName = input("Enter you first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People Values ('" + firstName + "', '" + lastName + "', " + str(age) + ")"
    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
              (45, 'Luigi', 'Vercotti'))
