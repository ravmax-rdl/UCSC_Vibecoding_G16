name = input("Enter student's name: ")

mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))

average = (mark1 + mark2 + mark3) / 3

if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"

print(f"\nStudent: {name}")
print(f"Average Mark: {average:.2f}")
print(f"Grade: {grade}")
