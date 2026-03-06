# Reflection Report – Day 02

## Prompts Used

Below are the prompts submitted to GitHub Copilot during this session:

### Part 2

#### Task 01

**"Write a Python script that asks for a student's name, asks for 3 subject marks, calculates the average, and displays 'Pass' if the average is greater than or equal to 40, else 'Fail'."**  
Created `grade_calculator.py`. The script collects the student's name and marks for three subjects, computes the arithmetic average, and prints the student's name, average mark, and a Pass/Fail result based on whether the average meets the 40-mark threshold.

#### Task 02

**"Assign Grade A for average ≥ 75, Grade B for 60–74, Grade C for 40–59, Fail below 40."**  
Extended `grade_calculator.py` to replace the binary Pass/Fail result with a four-tier letter grade system using an `if/elif/else` block. The output label was updated from `Result` to `Grade`.

#### Task 03

**"Modify the program so it runs repeatedly until the user types 'exit'."**  
Wrapped the full grade calculator logic inside a `while True` loop. The program prompts for the student's name each iteration and breaks with a goodbye message when the user types `exit`.

### Part 3

#### Task 01

**"Write a Python script that asks the user for a total monthly budget, asks for 3 expenses, subtracts expenses from the total budget, and displays the remaining balance."**  
Created `budget_tracker.py`. The script collects a monthly budget and three expense amounts, subtracts the total expenses from the budget, and prints a formatted summary with remaining balance and a status message.

#### Task 02
The warning message was manually modified as it as already added by the previous prompt.

#### Task 03
The while loop was added similar to Part 1 Task 03 manually.


### Additional prompts

**"The marks for the grade calculator should only be valid if between 0 and 100."**  
   Added a `get_mark(subject)` helper function to `grade_calculator.py` that loops until the user enters a value in the range 0–100, displaying an error message for any out-of-range input.

**"Add validation to the budget tracker as well, for the input values to be greater than 0."**  
   Added a `get_amount(prompt)` helper function to `budget_tracker.py` that re-prompts until a value greater than 0 is entered. The budget input was also validated with the same rule, restarting the loop with an error message if the value is not positive.

---

## GitHub Repository

[https://github.com/ravmax-rdl/UCSC_Vibecoding_G16](https://github.com/ravmax-rdl/UCSC_Vibecoding_G16)
