import sqlite3
import os

DATABASE_FILE = "AccountsData.db"
MENU_FILE = "menu.cfg"

class Bank:
	def __init__(self):
		self.conn = sqlite3.connect(DATABASE_FILE)
		self.cur = self.conn.cursor()
		self.fields = self.get_fieldnames("Accounts") 

	def display_menu(self):
		if not os.path.exists(MENU_FILE):
			print("Menu file not found.")
			return
		with open(MENU_FILE, 'r') as fp_menu:
			print(fp_menu.read())

	def get_fieldnames(self, table_name):
		self.cur.execute(f"PRAGMA table_info({table_name})")
		fieldnames = [col[1] for col in self.cur.fetchall()]
		return fieldnames

	def create_record(self):
		values = []
		for field in self.fields:
			value = input(f"Enter {field}: ")
			values.append(value)
		placeholders = ", ".join(["?"] * len(self.fields))
		query = f"INSERT INTO Accounts ({', '.join(self.fields)}) VALUES ({placeholders})"
		self.cur.execute(query, values)
		self.conn.commit()
		print("Account created successfully.")

	def read_records(self):
		self.cur.execute('SELECT * FROM Accounts')
		records = self.cur.fetchall()
		if records:
			print("______ACCOUNTS______")
			for i, record in enumerate(records, start=1):
				print(f"\nAccount: {i}")
				for field, value in zip(self.fields, record):
					print(f"{field}: {value}")
		else:
			print("No records found.")

	def get_id(self, action):
		id = input(f"Enter {self.fields[0]} to be {action}d: ")
		return id
	
	def search_record(self, id):
		query = f"SELECT * FROM Accounts WHERE {self.fields[0]} = {id}"
		self.cur.execute(query)
		record = self.cur.fetchone()
		return record
	
	def update_record(self):
		action = "update"
		id = self.get_id(action)
		record = self.search_record(id)
		if not record:
			print(f"Record with {id} not found to {action}.")
			return
		else:
			last_field = self.fields[-1]
			print(f"\nCurrent {last_field}: {record[-1]}")
			new_value = input(f"Enter new {last_field}: ")
			query = f"UPDATE Accounts SET {last_field} = ? WHERE {self.fields[0]} = ?"
			self.cur.execute(query, (new_value, id))
			self.conn.commit()
			print(f"Record with {self.fields[0]} {id} {action}d successfully")
	
	def delete_record(self):
		action = "delete"
		id = self.get_id(action)
		record = self.search_record(id)
		if not record:
			print(f"Record with {id} not found to {action}.")
			return
		else:
			query = f"DELETE FROM Accounts WHERE {self.fields[0]} = {id}"
			self.cur.execute(query)
			self.conn.commit()
			print(f"Record with {self.fields[0]} {id} {action}d successfully")
		

	def exiting(self):
		self.conn.close()
		print("Exiting....")

db = Bank()

while True:
	db.display_menu()

	operations = [db.create_record, db.read_records, db.update_record, db.delete_record, db.exiting]
	choice = int(input("Enter your choice: "))
	if 1 <= choice <= len(operations):
		operations[choice - 1]()
	else:
		print("Invalid choice. Try again.\n")

