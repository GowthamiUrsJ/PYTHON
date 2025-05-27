age = int(input("Enter your age: "))
grade = float(input("Enter your CGPA: "))
has_lor = input("Do you have a Letter of recommendation? (yes/no): ").lower()

if age >= 18 and grade >= 8:
    print("You are eligible for the college scholarship.")
else:
    print("Try again next year for the college scholarship.")

if grade > 90 or has_lor == "yes":
    print("You can enter the honors program or get priority admission.")
else:
    print("Regular admission applies.")

if not has_lor == "yes":
    print("Get LOR for priority admission.")
