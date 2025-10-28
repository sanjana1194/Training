import xml.etree.ElementTree as et
import os

FIELDS_FILE = "fields.xml"
DATA_FILE = "Accounts_data.xml"
MENU_FILE = "menu.cfg"

def load_fields():
	global root_tag, record_tag, fields
	if not os.path.exists(FIELDS_FILE):
		print(f"File '{FIELDS_FILE}' not found.")
		exit()
	tree = et.parse(FIELDS_FILE)
	root = tree.getroot()
	root_tag = root.find("RootTag").text
	record_tag = root.find("RecordTag").text
	fields = [field.text for field in root.findall("Field")]

def load_data():
	global tree, root
	if os.path.exists(DATA_FILE):
		tree = et.parse(DATA_FILE)
		root = tree.getroot()
	else:
		root = et.Element(root_tag)
		tree = et.ElementTree(root)
		save_data()

def display_menu():
	if not os.path.exists(MENU_FILE):
		print("Menu file not found.")
		return
	with open(MENU_FILE, 'r') as fp_menu:
		print(fp_menu.read())

def save_data():
	tree.write(DATA_FILE, encoding='utf-8', xml_declaration=True)

# def get_input_from_user():
# 	return [input(f"Enter {field}: ") for field in fields]

# def create_record():
# 	values = get_input_from_user()
# 	record = et.SubElement(root, record_tag)
# 	for field, value in zip(fields, values):
# 		et.SubElement(record, field).text = value
# 	save_data()
# 	print("Record added successfully.\n")

def create_record():
	record = et.SubElement(root, record_tag)
	for field in fields:
		value = input(f"Enter {field}: ")
		et.SubElement(record, field).text = value
	save_data()
	print("Record added successfully.\n")

def read_records():
	if not list(root):
		print("No records found.\n")
		return

	for index, record in enumerate(root, 1):
		print(f"\nRecord {index}:")
		for element in record:
			print(f"    {element.tag}: {element.text}")
	print()
	
def get_userid_to_search(action):
	return(input(f"Enter {fields[0]} to {action}: "))

def search_id(id):
	for index, record in enumerate(root.findall(record_tag)):
		element = record.find(fields[0])
		if (element.text == id):
			return index
	return None
	
def update_record():
	action = "update"
	id = get_userid_to_search(action)
	index = search_id(id)
	if not index:
		print(f"No record with {fields[0]} {id} found to {action}")
		return
	record = root.findall(record_tag)[index]
	print("Current Details")
	for element in record:
		print(f"{element.tag}: {element.text}")
	new_value = input(f"Enter new value for {fields[-1]}: ")
	record.find(fields[-1]).text = new_value
	save_data()
	print(f"Record with {fields[0]} {id} {action}d successfully")

def delete_record():
	action = "delete"
	id = get_userid_to_search(action)
	index = search_id(id)
	if not index:
		print(f"No record with {fields[0]} {id} found to {action}")
		return
	record = root.findall(record_tag)[index]
	root.remove(record)
	save_data()
	print(f"Record with {fields[0]} {id} {action}d successfully")
	
def exiting():
	exit(0)
	
def main():
	load_fields()
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
