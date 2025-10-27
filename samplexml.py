import xml.etree.ElementTree as et
import os

DATA_FILE = "Accounts.xml"
FIELDS_FILE = "fields.cfg"
MENU_FILE = "menu.cfg"

fields = []
tree = None
root = None

def load_data():
	global fields, tree, root

	with open(FIELDS_FILE, 'r') as fp_fields:
		fields = fp_fields.read().splitlines()
		if not fields:
			print("No field names found.")
			exit()
	print(f"Loaded fields: {fields}")

	if os.path.exists(DATA_FILE):
		tree = et.parse(DATA_FILE)
		root = tree.getroot()
	else:
		root = et.Element("Bank_Accounts")
		tree = et.ElementTree(root)
		save_data()


def save_data():
	global tree
	et.indent(tree, space="\t", level=0)
	tree.write(DATA_FILE, encoding="utf-8", xml_declaration=True)

def display_menu():
	if not os.path.exists(MENU_FILE):
		print("Menu file not found.")
		return
	with open(MENU_FILE, 'r') as fp_menu:
		menu = fp_menu.read()
		print(menu)

def get_input_from_user():
	return [input(f"Enter {field}: ") for field in fields]

def read_records():
	if not list(root):
		print("No accounts found in XML File.")
		return

	for i, account in enumerate(root.findall("Account"), 1):
		print(f"\nAccount {i}:")
		for element in account:
			print(f"{element.tag}: {element.text}")
	

def create_record():
	values = get_input_from_user()
	account = et.SubElement(root, "Account")
	for field, value in zip(fields, values):
		et.SubElement(account, field).text = value

	save_data()
	print("Account added successfully!")
	
def update_record(): 
	print("Updating...") 
	
def delete_record(): 
	print("Deleting...")

def exiting():
	print("Exiting program...")
	save_data()
	exit(0)

def main():
	load_data()
	while True:
		display_menu()
		operations = [create_record, read_records, update_record, delete_record, exiting]
		choice = int(input("Enter your choice: "))
		if 1 <= choice <= len(operations):
			operations[choice - 1]()
		else:
			print("Invalid choice. Try again.\n")


main()
