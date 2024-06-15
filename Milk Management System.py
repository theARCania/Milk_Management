import sqlite3


# Establish connections
cnx = sqlite3.connect(database='Milk_Management')
cursor = cnx.cursor()

# Initiate setup of DBs
def initiateDBs():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Cows (
        cow_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cow_name VARCHAR(20),
        birth_date DATE,
        breed VARCHAR(20),
        health_status VARCHAR(100),
        weight_in_KG INT,
        mother_id INTEGER,
        father_id INTEGER);""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS MilkProducedDaily (
        milk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cow_id INTEGER,
        date DATE,
        morning_production FLOAT,
        morning_sold FLOAT,
        evening_production FLOAT,
        evening_sold FLOAT);""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS IncomeDaily (
        income_id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE,
        amount FLOAT,
        description VARCHAR(255));""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name VARCHAR(20),
        contact_number CHAR(10),
        address VARCHAR(255));""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS WeeklyPayments (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        payment_date DATE,
        amount FLOAT,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id));""")

# to access the Cows table
def CowsTable():
    print("""
1. Display cows
2. Add a cow
3. Alter cows table""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        cursor.execute("SELECT * FROM Cows")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    elif choice == 2:
        cow_name = input("Enter cow name: ")
        birth_date = input("Enter birth date (YYYY-MM-DD): ")
        breed = input("Enter breed: ")
        health_status = input("Enter health status: ")
        weight_in_KG = int(input("Enter weight in KG: "))
        mother_id = int(input("Enter mother's ID: "))
        father_id = int(input("Enter father's ID: "))  
        cursor.execute("INSERT INTO Cows (cow_name, birth_date, breed, health_status, weight_in_KG, mother_id, father_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (cow_name, birth_date, breed, health_status, weight_in_KG, mother_id, father_id))
        cnx.commit()
        print("Cow added successfully!")

    elif choice == 3:
        cow_id = int(input("Enter the cow's ID to alter: "))
        new_health_status = input("Enter new health status: ")
        new_weight_in_KG = int(input("Enter new weight in KG: "))       
        cursor.execute("UPDATE Cows SET health_status = ?, weight_in_KG = ? WHERE cow_id = ?",
                    (new_health_status, new_weight_in_KG, cow_id))
        cnx.commit()
        print("Cow data altered successfully!")
    else:
        print('Invalid choice')

# to access the Milk table
def MilkTable():
    print("""
1. Add records
2. View milk data""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        cow_id = int(input("Enter the cow's ID: "))
        date = input("Enter date (YYYY-MM-DD): ")
        morning_production = float(input("Enter morning production (liters): "))
        morning_sold = float(input("Enter morning sold (liters): "))
        evening_production = float(input("Enter evening production (liters): "))
        evening_sold = float(input("Enter evening sold (liters): "))
        
        cursor.execute("INSERT INTO MilkProducedDaily (cow_id, date, morning_production, morning_sold, evening_production, evening_sold) VALUES (?, ?, ?, ?, ?, ?)",
                       (cow_id, date, morning_production, morning_sold, evening_production, evening_sold))
        cnx.commit()
        print("Milk record added successfully!")
    elif choice == 2:
        cursor.execute("SELECT * FROM MilkProducedDaily ORDER BY date DESC LIMIT 5")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    else:
        print("Invalid choice")

# to access the Income table
def IncomeTable():
    print("""
1. Add a record
2. View income""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        date = input("Enter date (YYYY-MM-DD): ")
        amount = float(input("Enter income amount: "))
        description = input("Enter description: ")
        
        cursor.execute("INSERT INTO IncomeDaily (date, amount, description) VALUES (?, ?, ?)",
                       (date, amount, description))
        cnx.commit()
        print("Income record added successfully!")
    elif choice == 2:
        cursor.execute("SELECT * FROM IncomeDaily ORDER BY date DESC LIMIT 5")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    else:
        print("Invalid choice")

# to access the Customer table
def CustomerTable():
    print("""
1. Add a customer
2. View customers
3. Remove a customer""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        customer_name = input("Enter customer name: ")
        contact_number = input("Enter contact number: ")
        address = input("Enter address: ")
        
        cursor.execute("INSERT INTO Customers (customer_name, contact_number, address) VALUES (?, ?, ?)",
                       (customer_name, contact_number, address))
        cnx.commit()
        print("Customer added successfully!")
    elif choice == 2:
        cursor.execute("SELECT * FROM Customers")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    elif choice == 3:
        customer_id = int(input("Enter the customer's ID to remove: "))
        cursor.execute("DELETE FROM Customers WHERE customer_id = ?", (customer_id,))
        cnx.commit()
        print("Customer removed successfully!")
    else:
        print("Invalid choice")

# to access the Payments table
def PaymentsTable():
    print("""
1. Add records
2. View records""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        customer_id = int(input("Enter customer ID: "))
        payment_date = input("Enter payment date (YYYY-MM-DD): ")
        amount = float(input("Enter payment amount: "))
        
        cursor.execute("INSERT INTO WeeklyPayments (customer_id, payment_date, amount) VALUES (?, ?, ?)",
                       (customer_id, payment_date, amount))
        cnx.commit()
        print("Payment record added successfully!")
    elif choice == 2:
        cursor.execute("SELECT * FROM WeeklyPayments")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    else:
        print("Invalid choice")

# Main

print('Welcome to the Milk Manager!')
initiateDBs()

while True:
    print("""
1) Access Cows table
2) Access Milk table
3) Access Income table
4) Access Customer table
5) Access Payments table
6) Quit
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        CowsTable()
    elif choice == 2:
        MilkTable()
    elif choice == 3:
        IncomeTable()
    elif choice == 4:
        CustomerTable()
    elif choice == 5:
        PaymentsTable()
    elif choice == 6:
        print("Thank you!")
        cnx.commit()
        cursor.close()
        cnx.close()
        break
    else:
        print("Enter a valid choice.")