import pickle
import os

FILE = "FileHandling/DataFiles/students.dat"

# ------------------ CREATE ------------------
def add_record():
    try:
        f = open(FILE, "ab")
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        record = [roll, name, marks]
        pickle.dump(record, f)

        print("Record added successfully!")
        f.close()

    except Exception as e:
        print("Error:", e)


# ------------------ READ ------------------
def display_records():
    try:
        f = open(FILE, "rb")

        print("\nStudent Records:")
        while True:
            record = pickle.load(f)
            print(record)

    except EOFError:
        f.close()
    except FileNotFoundError:
        print("No records found!")


# ------------------ SEARCH ------------------
def search_record():
    try:
        f = open(FILE, "rb")
        roll = int(input("Enter Roll No to search: "))

        found = False
        while True:
            record = pickle.load(f)
            if record[0] == roll:
                print("Record Found:", record)
                found = True
                break

    except EOFError:
        if not found:
            print("Record not found!")
        f.close()


# ------------------ UPDATE ------------------
def update_record():
    try:
        f = open(FILE, "rb")
        temp = open("FileHandling/DataFiles/temp.dat", "wb")

        roll = int(input("Enter Roll No to update: "))
        found = False

        while True:
            record = pickle.load(f)

            if record[0] == roll:
                print("Old Record:", record)
                record[1] = input("Enter new name: ")
                record[2] = float(input("Enter new marks: "))
                found = True

            pickle.dump(record, temp)

    except EOFError:
        f.close()
        temp.close()

        if found:
            os.remove(FILE)
            os.rename("FileHandling/DataFiles/temp.dat", FILE)
            print("Record updated!")
        else:
            os.remove("FileHandling/DataFiles/temp.dat")
            print("Record not found!")


# ------------------ DELETE ------------------
def delete_record():
    try:
        f = open(FILE, "rb")
        temp = open("FileHandling/DataFiles/temp.dat", "wb")

        roll = int(input("Enter Roll No to delete: "))
        found = False

        while True:
            record = pickle.load(f)

            if record[0] != roll:
                pickle.dump(record, temp)
            else:
                found = True

    except EOFError:
        f.close()
        temp.close()

        if found:
            os.remove(FILE)
            os.rename("FileHandling/DataFiles/temp.dat", FILE)
            print("Record deleted!")
        else:
            os.remove("FileHandling/DataFiles/temp.dat")
            print("Record not found!")


# ------------------ MENU ------------------
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Record")
        print("2. Display Records")
        print("3. Search Record")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_record()
        elif choice == 2:
            display_records()
        elif choice == 3:
            search_record()
        elif choice == 4:
            update_record()
        elif choice == 5:
            delete_record()
        elif choice == 6:
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()