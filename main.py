def get_letter_grade(average):
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

def get_gpa(average):
    thresholds = [(97, 4.0), (93, 4.0), (90, 3.7), (87, 3.3), (83, 3.0),
                  (80, 2.7), (77, 2.3), (73, 2.0), (70, 1.7), (67, 1.3),
                  (63, 1.0), (60, 0.7)]
    for threshold, gpa in thresholds:
        if average >= threshold:
            return gpa
    return 0.0

def calculate_stats(grades):
    average = sum(grades) / len(grades)
    return {
        "average": average,
        "highest": max(grades),
        "lowest": min(grades),
        "letter": get_letter_grade(average),
        "gpa": get_gpa(average),
    }

print("Grade Calculator")
print("=" * 30)

name = input("Student name: ").strip() or "Student"

grades = []
subjects = []

print("\nEnter a subject and grade, or 'done' to finish.")
print("Example: Math 88\n")

while True:
    entry = input("Subject & grade (or 'done'): ").strip()

    if entry.lower() == "done":
        break

    try:
        parts = entry.rsplit(maxsplit=1)
        subject = parts[0] if len(parts) == 2 else f"Grade {len(grades) + 1}"
        grade = float(parts[-1])

        if not (0 <= grade <= 100):
            print("  ⚠ Grade must be between 0 and 100.")
            continue

        grades.append(grade)
        subjects.append(subject)
        print(f"  ✓ Added {subject}: {grade}")

    except ValueError:
        print("  ⚠ Couldn't parse that. Try: Math 88")

if not grades:
    print("\nNo grades were entered.")
else:
    stats = calculate_stats(grades)

    print(f"\n{'=' * 30}")
    print(f"  Results for {name}")
    print(f"{'=' * 30}")

    for subject, grade in zip(subjects, grades):
        print(f"  {subject:<20} {grade:>6.1f}")

    print(f"{'─' * 30}")
    print(f"  {'Average':<20} {stats['average']:>6.2f}  ({stats['letter']})")
    print(f"  {'GPA':<20} {stats['gpa']:>6.2f}")
    print(f"  {'Highest':<20} {stats['highest']:>6.1f}")
    print(f"  {'Lowest':<20} {stats['lowest']:>6.1f}")
    print(f"{'=' * 30}")