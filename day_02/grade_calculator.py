name = input("Enter student's name: ")

mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))

average = (mark1 + mark2 + mark3) / 3

result = "Pass" if average >= 40 else "Fail"

print(f"\nStudent: {name}")
print(f"Average Mark: {average:.2f}")
print(f"Result: {result}")
