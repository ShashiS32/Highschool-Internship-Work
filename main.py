print("Grade Calculator")
print("=" * 30)

name = input("Student name: ").strip()
if name == "":
    name = "Student"

print("\nEnter up to 10 subjects and grades.")
print("Leave subject blank to stop early.\n")

subject1 = input("Subject 1 name (or press Enter to finish): ").strip()
grade1 = 0.0
subject2 = ""
grade2 = 0.0
subject3 = ""
grade3 = 0.0
subject4 = ""
grade4 = 0.0
subject5 = ""
grade5 = 0.0
subject6 = ""
grade6 = 0.0
subject7 = ""
grade7 = 0.0
subject8 = ""
grade8 = 0.0
subject9 = ""
grade9 = 0.0
subject10 = ""
grade10 = 0.0
count = 0

if subject1 != "":
    grade1 = float(input(f"  Grade for {subject1}: "))
    count = 1

    subject2 = input("Subject 2 name (or press Enter to finish): ").strip()
    if subject2 != "":
        grade2 = float(input(f"  Grade for {subject2}: "))
        count = 2

        subject3 = input("Subject 3 name (or press Enter to finish): ").strip()
        if subject3 != "":
            grade3 = float(input(f"  Grade for {subject3}: "))
            count = 3

            subject4 = input("Subject 4 name (or press Enter to finish): ").strip()
            if subject4 != "":
                grade4 = float(input(f"  Grade for {subject4}: "))
                count = 4

                subject5 = input("Subject 5 name (or press Enter to finish): ").strip()
                if subject5 != "":
                    grade5 = float(input(f"  Grade for {subject5}: "))
                    count = 5

                    subject6 = input("Subject 6 name (or press Enter to finish): ").strip()
                    if subject6 != "":
                        grade6 = float(input(f"  Grade for {subject6}: "))
                        count = 6

                        subject7 = input("Subject 7 name (or press Enter to finish): ").strip()
                        if subject7 != "":
                            grade7 = float(input(f"  Grade for {subject7}: "))
                            count = 7

                            subject8 = input("Subject 8 name (or press Enter to finish): ").strip()
                            if subject8 != "":
                                grade8 = float(input(f"  Grade for {subject8}: "))
                                count = 8

                                subject9 = input("Subject 9 name (or press Enter to finish): ").strip()
                                if subject9 != "":
                                    grade9 = float(input(f"  Grade for {subject9}: "))
                                    count = 9

                                    subject10 = input("Subject 10 name (or press Enter to finish): ").strip()
                                    if subject10 != "":
                                        grade10 = float(input(f"  Grade for {subject10}: "))
                                        count = 10

if count == 0:
    print("\nNo grades were entered.")
else:
    total = grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7 + grade8 + grade9 + grade10
    average = total / count

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

    print("\n" + "=" * 30)
    print("  Results for " + name)
    print("=" * 30)

    if count >= 1:
        print(f"  {subject1:<20} {grade1:>6.1f}")
    if count >= 2:
        print(f"  {subject2:<20} {grade2:>6.1f}")
    if count >= 3:
        print(f"  {subject3:<20} {grade3:>6.1f}")
    if count >= 4:
        print(f"  {subject4:<20} {grade4:>6.1f}")
    if count >= 5:
        print(f"  {subject5:<20} {grade5:>6.1f}")
    if count >= 6:
        print(f"  {subject6:<20} {grade6:>6.1f}")
    if count >= 7:
        print(f"  {subject7:<20} {grade7:>6.1f}")
    if count >= 8:
        print(f"  {subject8:<20} {grade8:>6.1f}")
    if count >= 9:
        print(f"  {subject9:<20} {grade9:>6.1f}")
    if count >= 10:
        print(f"  {subject10:<20} {grade10:>6.1f}")

    print("-" * 30)
    print(f"  {'Average':<20} {average:>6.2f}  ({letter})")
    print("=" * 30)