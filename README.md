**# Vityarthi-Project**

*CGPA Calculator*

A simple and interactive CGPA Calculator written in Python.
This program allows students to enter their subject names, credits, and either letter grades (S, A+, A, …) or raw marks (0–100).
The script then converts inputs into grade points, computes the weighted total, and finally prints a formatted result table along with the CGPA.


*Features*

Supports Both Grade & Marks Input
Accepts letter grades (S, A+, A, B+, B, C, D, F)
Accepts marks (0–100) and converts them into grade points automatically

Accurate Grade Conversion
Input Type	Conversion
Letter Grades	Based on predefined mapping (e.g., S → 10, A+ → 9, etc.)
Marks (0–100)	Categorized into grade point ranges

Clean Output Table

Displays:
Subject Name
Credits
User Input (Grade/Marks)
Calculated Grade Points

*CGPA Calculation*

Uses the standard weighted formula:

CGPA = ∑(Grade Points × Credits)/∑Credits
	​

*How It Works*

User enters the number of subjects

For each subject:
Enter subject name
Enter credits (must be positive)
Enter grade or marks

Program converts inputs → grade points
Computes total points and total credits
Displays the final CGPA


*Code Structure*

1. Grade & Marks Conversions
Computes total points and total credits

Displays the final CGPA
letter_map = { "S": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5, "D": 4, "F": 0 }

2. Marks to Grade Points Function

def marks_to_gp(marks):
    if 90 <= marks <= 100: return 10
    elif 80 <= marks < 90: return 9

3. Unified Input Converter

 def convert_to_gp(value):
    # Detect grade or number input

4. CGPA Calculation

   cgpa = total_points / total_credits

   
*How to Run*

Ensure you have Python 3.x installed
Save the script as cgpa_calculator.py
Run in terminal

python cgpa_calculator.py


*Example Output*

==== CGPA CALCULATOR ====

--- Subject 1 ---
Enter Subject Name: Math
Enter no. Credits: 4
Enter GRADE (S,A+...) or MARKS (0–100): A+

--- Subject 2 ---
Enter Subject Name: Physics
Enter no. Credits: 3
Enter GRADE (S,A+...) or MARKS (0–100): 92

------------------------------------
             "RESULT TABLE"
======================================
Subject        Credits   Input     GDADE POINTS
--------------------------------------
Math           4         A+        9
Physics        3         92        10
======================================
Your CGPA is: 9.43
--------------------------------------


*Requirements*

Python 3.x
No external libraries require

