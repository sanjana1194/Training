import xml.etree.ElementTree as et
import os

FILE_NAME = "Accounts.xml"
FIELDS_FILE = "fields.cfg"
MENU_FILE = "menu.cfg"

fields = []

def load_fields():
	global fields
	with open(FIELDS_FILE, 'r') as fp_fields:
		fields = fp_fields.read().splitlines()
		if not fields:
			print("No field names found.")
			exit()
	print(f"Loaded fields: {fields}")
	
def display_menu():
    with open(MENU_FILE, 'r') as fp_menu:
        if not MENU_FILE:
            print("No Menu found")
            return
        menu = fp_menu.read()
        print(menu)

def get_input_from_user():
	return [input(f"Enter {field}: ") for field in fields]

def read_records():
	if not os.path.exists(FILE_NAME):
		print("No data file found.")
		return

	tree = et.parse(FILE_NAME)
	root = tree.getroot()

	if not list(root):
		print("No accounts found in XML.")
		return

	for i, account in enumerate(root.findall("Account"), 1):
		print(f"Account {i}:")
		for element in account:
			print(f"   {element.tag}: {element.text}")

def create_record():
    if os.path.exists(FILE_NAME):
        tree = et.parse(FILE_NAME)
        root = tree.getroot()
    else:
        root = et.Element("Bank_Accounts")
        tree = et.ElementTree(root)


    values = get_input_from_user()
    account = et.SubElement(root, "Account")
    for field, value in zip(fields, values):
        et.SubElement(account, field).text = value

    et.indent(tree, space="\t", level=0)
    tree.write(FILE_NAME, encoding="utf-8", xml_declaration=True)

    print("Account added successfully!")

def update_record():
      print("updating..")
def delete_record():
      print("deleting...")
def exiting():
    exit(0)

def main():
    load_fields()
    while True:
        display_menu()
        operations = [create_record, read_records, update_record, delete_record, exiting]
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= len(operations):
            operations[choice - 1]()
        else:
            print("Invalid choice. Try again.\n")

main()
	
