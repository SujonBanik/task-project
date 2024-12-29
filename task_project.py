FILENAME = "employees.txt"

# using try and except :
def load_employees():
    try:
        with open(FILENAME, "r") as file:
            return [line.strip().split(",") for line in file]
    except FileNotFoundError:
        return []

# function to save employees details :
def save_employees(employees):
    with open(FILENAME, "w") as file:
        for emp in employees:
            file.write(",".join(emp) + "\n")

# A function to add employee :
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    designation = input("Enter Employee Designation: ")
    employees = load_employees()
    employees.append([emp_id, name, designation])
    save_employees(employees)
    print("Employee added successfully!")

# A function to update employee :
def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    employees = load_employees()
    for emp in employees:
        if emp[0] == emp_id:
            emp[1] = input("Enter new Employee Name: ")
            emp[2] = input("Enter new Employee Designation: ")
            save_employees(employees)
            print("Employee updated successfully!")
            return
    print("Employee not found!")

# function to delete employee :
def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    employees = load_employees()
    new_employees = [emp for emp in employees if emp[0] != emp_id]
    save_employees(new_employees)
    print("Employee deleted successfully!" if len(new_employees) < len(employees) else "Employee not found!")

# function to view employee :
def view_employees():
    employees = load_employees()
    if not employees:
        print("No employees found.")
    else:
        print("Employee List:")
        print("{:<10} {:<20} {:<15}".format("ID", "Name", "Designation"))
        print("-" * 45)
        for emp in employees:
            print("{:<10} {:<20} {:<15}".format(emp[0], emp[1], emp[2]))

# function to search employee :
def search_employee():
    term = input("Enter name or designation to search: ").lower()
    employees = load_employees()
    results = [emp for emp in employees if term in emp[1].lower() or term in emp[2].lower()]
    if not results:
        print("No matching employees found.")
    else:
        print("Search Results:")
        for emp in results:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Designation: {emp[2]}")

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. View All Employees")
        print("5. Search Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            update_employee()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            view_employees()
        elif choice == "5":
            search_employee()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()