print("Grade Calculator")
print("=" * 30)
 
name = input("Name? ").strip()
if name == "":
    name = "Student"
 
print(f"\nAlright {name} lets see how you did.")
print("Enter your subjects and grades below. Hit Enter when done.\n")
 
subjects = []
grades = []
 
while True:
    subject = input("Subject (or Enter to finish): ").strip()
    if subject == "":
        break
 
    grade = float(input(f"  Grade for {subject}: "))
 
    if grade < 0 or grade > 100:
        print("  That doesn't look right. Your grade should be between 0 and 100.")
        continue
 
    subjects.append(subject)
    grades.append(grade)
    print(f"  got it!")
 
if len(grades) == 0:
    print("\nNo grades entered ")
else:
    average = sum(grades) / len(grades)
 
    if average >= 97:
        letter = "A+"
    elif average >= 93:
        letter = "A"
    elif average >= 90:
        letter = "A-"
    elif average >= 87:
        letter = "B+"
    elif average >= 83:
        letter = "B"
    elif average >= 80:
        letter = "B-"
    elif average >= 77:
        letter = "C+"
    elif average >= 73:
        letter = "C"
    elif average >= 70:
        letter = "C-"
    elif average >= 67:
        letter = "D+"
    elif average >= 63:
        letter = "D"
    elif average >= 60:
        letter = "D-"
    else:
        letter = "F"
 
    print(f"\nBreakdown, {name}:")
    print(f"{'─' * 30}")
 
    for i in range(len(subjects)):
        print(f"  {subjects[i]:<20} {grades[i]:>6.1f}")
 
    print(f"{'─' * 30}")
    print(f"  {'Average':<20} {average:>6.2f}  ({letter})")
    print(f"  {'Highest':<20} {max(grades):>6.1f}")
    print(f"  {'Lowest':<20} {min(grades):>6.1f}")
    print(f"{'─' * 30}")
 
    if average >= 90:
        print(f"\nnot bad !")
    elif average >= 70:
        print(f"\ndecent! ")
    else:
        print(f"\ncould be better ")