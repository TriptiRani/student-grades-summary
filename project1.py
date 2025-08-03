def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'Fail'

students = []
num_students = int(input("Enter number of students: "))

for i in range(num_students):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = []
    for j in range(3):
        mark = float(input(f"Enter marks for Subject {j+1}: "))
        marks.append(mark)
    total = sum(marks)
    avg = total / 3
    grade = calculate_grade(avg)
    students.append({'name': name, 'marks': marks, 'total': total, 'avg': avg, 'grade': grade})

print("\n--- Student Summary ---")
for student in students:
    print(f"{student['name']}: Total = {student['total']}, Average = {student['avg']:.2f}, Grade = {student['grade']}")

class_avg = sum([s['avg'] for s in students]) / num_students
print(f"\nClass Average: {class_avg:.2f}")

topper = max(students, key=lambda x: x['total'])
print(f"Topper: {topper['name']} with {topper['total']} marks")


    


       


    