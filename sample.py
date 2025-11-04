import sqlite3

DATABASE_FILE = "AccountsData.db"

class Bank:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_FILE)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('create table if not exists accountdetails(accountno INTEGER PRIMARY KEY, name TEXT NOT NULL, balance FLOAT NOT NULL)')
        self.conn.commit()

    def create_record(self):
        acc_no = int(input("Enter Account Number: "))
        name = input("Enter Name: ")
        balance = float(input("Enter Balance: "))
        self.cur.execute('insert into accountdetails(accountno, name, balance) values (?, ?, ?)', (acc_no, name, balance))
        self.conn.commit()

    def read_records(self):
        self.cur.execute('select * from accountdetails')
        records = self.cur.fetchall()
        counter = 1
        if records:
            print("______ACCOUNTS______")
            for record in records:
                print(f"Account: {counter}")
                print(f"AccountNumber: {record[0]}\nName: {record[1]}\nBalance: {record[2]}")
                counter += 1 

    def exiting(self):
          self.conn.commit()
          self.conn.close()
          print("Exiting....")
db = Bank()

while True:
	print("\n===== ACCOUNT MENU =====")
	print("1. Create Account")
	print("2. View All Accounts")
	print("3. Exit")

	operations = [db.create_record, db.read_records, db.exiting]

	try:
		choice = int(input("Enter your choice: "))
		if 1 <= choice <= len(operations):
			operations[choice - 1]()
		else:
			print("Invalid choice. Try again.")
	except ValueError:
		print("Please enter a valid number.")


