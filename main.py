def get_letter(average):
    if average >= 97: return "A+"
    elif average >= 93: return "A"
    elif average >= 90: return "A-"
    elif average >= 87: return "B+"
    elif average >= 83: return "B"
    elif average >= 80: return "B-"
    elif average >= 77: return "C+"
    elif average >= 73: return "C"
    elif average >= 70: return "C-"
    elif average >= 67: return "D+"
    elif average >= 63: return "D"
    elif average >= 60: return "D-"
    else: return "F"
 
def print_results(name, subjects, grades):
    average = sum(grades) / len(grades)
    print(f"\nBreakdown, {name}:")
    print("─" * 30)
    for i in range(len(subjects)):
        print(f"  {subjects[i]:<20} {grades[i]:>6.1f}")
    print("─" * 30)
    print(f"  {'Average':<20} {average:>6.2f}  ({get_letter(average)})")
    print(f"  {'Highest':<20} {max(grades):>6.1f}")
    print(f"  {'Lowest':<20} {min(grades):>6.1f}")
 
 
print("Grade Calculator")
 
name = input("\nName? ").strip() or "Student"
 
print(f"\nAlright {name} lets see how you did.")
print("Enter subjects and grades below. Hit Enter when done.\n")
 
subjects = []
grades = []
 
while True:
    subject = input("Subject (or Enter to finish): ").strip()
    if subject == "":
        break
 
    grade = float(input(f"  Grade for {subject}: "))
 
    if grade < 0 or grade > 100:
        print("  should be between 0 and 100.")
        continue
 
    subjects.append(subject)
    grades.append(grade)
    print("  got it!")
 
if len(grades) == 0:
    print("\nNo grades entered.")
else:
    print_results(name, subjects, grades)