print("==== CGPA CALCULATOR ====\n")
# Conversion of [GRADES → GRADE POINTS]
letter_map = { "S": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5, "D": 4, "F": 0 }
# Conversion of [MARKS (0–100) → GRADE POINTS (0–10)]
def marks_to_gp(marks):        #[Defining the function "marks"]
    marks = float(marks)
    if 90 <= marks <= 100: return 10
    elif 80 <= marks < 90: return 9
    elif 70 <= marks < 80: return 8
    elif 60 <= marks < 70: return 7
    elif 50 <= marks < 60: return 6
    elif 40 <= marks < 50: return 5
    elif 30 <= marks < 40: return 4
    else: return 0
#[IDENTIFICATION AND CONVERSION OF GIVEN INPUTS]
def convert_to_gp(value):
    value = value.strip().upper()
   # CASE 1: GRADES(i.e S,A+,A,B+,B etc)
    if value in letter_map:
        return letter_map[value]
   # CASE 2: MARKS(i.e 56,78,90,99 etc)
    num = float(value)
    if 0 <= num <= 100:
       return marks_to_gp(num)                        
subjects = int(input("Enter no. of Subjects: "))
total_credits = 0
total_points = 0
table = []
for i in range(1, subjects + 1):
    print(f"\n--- Subject {i} ---")
    name = input("Enter Subject Name: ")
    # [ENTERING CREDITS INPUTS] 
    while True:
            credit = float(input("Enter no. Credits: "))
            if credit > 0:
                break
            else:
                print("Credits must be positive.")
    # [GRADE OR MARKS INPUT]
    while True:
        inp = input("Enter GRADE (S,A+...) or MARKS (0–100): ")
        gp = convert_to_gp(inp)
        if gp is not None:
            break
    total_credits += credit
    total_points += gp * credit
    table.append([name, credit, inp, gp])
cgpa = total_points / total_credits
# [OUTPUT TABLE]
print("\n------------------------------------")
print("             \"RESULT TABLE\"")
print("======================================")
print(f"{'Subject':15s}{'Credits':10s}{'Input':10s}{'GDADE POINTS'}")
print("--------------------------------------")
for sub in table:
    print(f"{sub[0]:15s}{str(sub[1]):10s}{sub[2]:10s}{sub[3]}")
print("======================================")
print(f"Your CGPA is: {cgpa:.2f}")
print("--------------------------------------")