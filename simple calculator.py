

#swap two numbers
a = 10
b = 5
a,b=b,a
print(a,b)

#odd even
num=int(input())

if num%2==0:
    print("even")
else:
    print("odd")


    #largest number

    
    a=10
    b=20
    c=30
    print(max(a,b,c))

    #multiplication

    n=int(input())
    for i in range (2,22):

     print(n*i)




     #student management system
     students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average Marks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ").strip().title()
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))
        students.append({"name": name, "age": age, "marks": marks})
        print(f"{name} added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student['name']} | Age: {student['age']} | Marks: {student['marks']}")

    elif choice == "3":
        search = input("Enter name to search: ").strip().title()
        found = False
        for student in students:
            if student["name"] == search:
                print(f"Found: {student}")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        if students:
            total = sum(student["marks"] for student in students)
            average = total / len(students)
            print(f"Average Marks = {average:.2f}")
        else:
            print("No student data available.")

    elif choice == "5":
        print("Thank you for using the Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")