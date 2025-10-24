import json

DATA_FILE = 'data.dat'
MENU_FILE = 'menu.cfg'
FIELDS_FILE = 'fields.cfg'

records = []
fields = []


def load_data():
    global fields, records

    with open(FIELDS_FILE, 'r') as fp_fields:
        if not FIELDS_FILE:
            print("No FieldsNames found")
            return
        fields = fp_fields.read().splitlines()
    # print(fields)

    with open(DATA_FILE, "r") as fp_data:
        if not DATA_FILE:
            print("No Data found")
            return
        records = json.load(fp_data)
    # print(records)


def display_menu():
    with open(MENU_FILE, 'r') as fp_menu:
        if not MENU_FILE:
            print("No Menu found")
            return
        menu = fp_menu.read()
        print(menu)


def get_input_to_create():
    return [input(f"Enter {field}: ") for field in fields]


def add_record(record):
    records.append(record)


def save_records_to_file():
    with open(DATA_FILE, "w") as fp_records:
        json.dump(records, fp_records)


def create_record():
    record_data = get_input_to_create()
    add_record(record_data)
    save_records_to_file()
    print("Record Created")


def read_records():
    if not records:
        print("No data found")
        return
    else:
        print("_____All Records______")
        '''for index, record in enumerate(records, 1):
            print(f"{index}. {record}")'''
        for index, record in enumerate(records, 1):
            print(f"\nRecord {index}:")
            for counter, field in enumerate(fields):
                print(f"{field}: {record[counter]}")


def get_user_id(action):
    id = input(f"Enter {fields[0]} to {action}: ")
    return id


def search_id(id):
    for index, record in enumerate(records):
        if record[0] == id:
            return index


def update_record():
    temp_id = get_user_id('update')
    record_index = search_id(temp_id)
    if record_index is None:
        return
    curr_record = records[record_index]
    print(f"Current Record: {curr_record}")
    new_value = input(f"Enter new value for {fields[-1]}: ")
    curr_record[-1] = new_value
    save_records_to_file()
    print(f"Record with ID {temp_id} updated successfully")


def delete_record():
    temp_id = get_user_id('delete')
    record_index = search_id('delete', temp_id)
    final_records = records.pop(record_index)
    save_records_to_file()
    print(f"Record with ID {temp_id} deleted successfully.")


def exiting():
    print("Exiting...")
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


if __name__ == "__main__":
    main()