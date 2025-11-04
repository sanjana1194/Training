import sqlite3

DATABASE_FILE = "Accounts.db"

class Bank:
	def __init__(self):
		self.conn = sqlite3.connect(DATABASE_FILE)
		self.cur = self.conn.cursor()
		self.create_table()

	def create_table(self):
		self.cur.execute('''CREATE TABLE IF NOT EXISTS Accounts(
			AccountNo INTEGER PRIMARY KEY,
			Name TEXT NOT NULL,
			Balance REAL NOT NULL
		)''')
		self.conn.commit()

	def create_account(self):
		try:
			acc_no = int(input("Enter Account Number: "))
			name = input("Enter Name: ")
			balance = float(input("Enter Balance: "))
			self.cur.execute(
				'INSERT INTO Accounts(AccountNo, Name, Balance) VALUES (?, ?, ?)',
				(acc_no, name, balance)
			)
			self.conn.commit()
			print("Account created successfully.")
		except sqlite3.IntegrityError:
			print("Account number already exists!")

	def read_accounts(self):
		self.cur.execute('SELECT * FROM Accounts')
		records = self.cur.fetchall()
		if records:
			print("\n--- Accounts List ---")
			for record in records:
				print(f"AccountNo: {record[0]}, Name: {record[1]}, Balance: {record[2]}")
		else:
			print("No accounts found.")

	def exit_program(self):
		self.conn.close()
		print("Exiting...")
		exit()


if __name__ == "__main__":
	db = Bank()

	while True:
		print("\n===== ACCOUNT MENU =====")
		print("1. Create Account")
		print("2. View All Accounts")
		print("3. Exit")

		operations = [db.create_account, db.read_accounts, db.exit_program]

		try:
			choice = int(input("Enter your choice: "))
			if 1 <= choice <= len(operations):
				operations[choice - 1]()
			else:
				print("Invalid choice. Try again.")
		except ValueError:
			print("Please enter a valid number.")

