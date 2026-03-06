def get_mark(subject):
    while True:
        mark = float(input(f"Enter mark for {subject}: "))
        if 0 <= mark <= 100:
            return mark
        print("Invalid mark. Please enter a value between 0 and 100.")

while True:
    name = input("\nEnter student's name (or 'exit' to quit): ")
    if name.lower() == "exit":
        print("Goodbye!")
        break

    mark1 = get_mark("Subject 1")
    mark2 = get_mark("Subject 2")
    mark3 = get_mark("Subject 3")

    average = (mark1 + mark2 + mark3) / 3

    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    print(f"\nName: {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
