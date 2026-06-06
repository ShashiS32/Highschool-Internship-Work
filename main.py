print("grade calculator")

name = input("\nname? ").strip()
if name == "":
    name = "student"

print(f"\nhey {name}! enter your subjects and grades below.")
print("hit Enter with no subject when you're done.\n")

subjects = []
grades = []

while True:
    subject = input("subject (or Enter to finish): ").strip()
    if subject == "":
        break

    grade = float(input(f"  grade for {subject}: "))

    if grade < 0 or grade > 100:
        print("  should be between 0 and 100\n")
        continue

    subjects.append(subject)
    grades.append(grade)
    print(f"  got it!\n")

if len(grades) == 0:
    print("no grades entered")
else:
    average = sum(grades) / len(grades)

    if average >= 97: letter = "A+"
    elif average >= 93: letter = "A"
    elif average >= 90: letter = "A-"
    elif average >= 87: letter = "B+"
    elif average >= 83: letter = "B"
    elif average >= 80: letter = "B-"
    elif average >= 77: letter = "C+"
    elif average >= 73: letter = "C"
    elif average >= 70: letter = "C-"
    elif average >= 67: letter = "D+"
    elif average >= 63: letter = "D"
    elif average >= 60: letter = "D-"
    else: letter = "F"

    print(f"\nok here's how you did, {name}:")
    print("─" * 30)
    for i in range(len(subjects)):
        print(f"  {subjects[i]:<20} {grades[i]:>5.1f}")
    print("─" * 30)
    print(f"  average   {average:.2f}  ({letter})")
    print(f"  highest   {max(grades):.1f}")
    print(f"  lowest    {min(grades):.1f}")