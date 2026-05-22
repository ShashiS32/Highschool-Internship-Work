def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
 
def calculate_average(grades):
    total = 0
    for grade in grades:
        total = total + grade
    average = total / len(grades)
    return average


print("Grade Calculator!")
print("-----------------")
 
name = input("Enter  name: ")
 
grades = []
 
print("\nEnter one grade at a time. Type 'done' when finished.")
 
while True:
    entry = input("Enter a grade: ")
 
    if entry == "done":
        break
 
    grade = float(entry)
 
    if grade < 0 or grade > 100:
        print("Please enter a grade between 0 and 100.")
    else:
        grades.append(grade)
 
if len(grades) == 0:
    print("No grades were entered.")
else:
    average = calculate_average(grades)
    letter = get_letter_grade(average)
 
    print("\n--- Results for", name, "---")
    print("Grades entered: ", grades)
    print("Number of grades: ", len(grades))
    print("Average: ", round(average, 2))
    print("Letter grade: ", letter)