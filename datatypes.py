student_id = int(input("Enter Student Id: "))
height = float(input("Enter your height in feet: "))

name = input("Enter student name: ")

#List
grades=[]
print("Enter 3 subject grades: ")
for i in range(3):
    grade = int(input(f"{i+1}st grade:"))
    grades.append(grade)

#tuple
subjects = ("DSA","JAVA PROGRAMMING", "OPERATING SYSTEM")

roll_no = range(1,6)

#dictinory
profile = {
    "Name" : name,
    "Id" : student_id,
    "Height" : height,
    "Grades" : grades
}

#set
unique_marks = set(grades)

avg = sum(grades)/len(grades)
is_passed = avg>40

print("Student ID:", student_id)
print("Name:", name)
print("Height in feet:", height)
print("Grades List:", grades)
print("Subjects Tuple:", subjects)
print("Roll Numbers Range:", list(roll_no))
print("Student Profile Dictionary:",profile)
print("Unique Marks Set:", unique_marks)
print("Average Grade:", avg)
print("Has Passed?:", is_passed)