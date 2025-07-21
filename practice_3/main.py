import yaml

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

def evaluate_grade(student):
    if student.score >= 90:
        return "A"
    elif student.score >= 80:
        return "B"
    elif student.score >= 70:
        return "C"
    elif student.score >= 60:
        return "D"
    else:
        return "F"
    

def main():
    with open('students.yaml', 'r') as file:
        students_data = yaml.safe_load(file)

    # print(students_data)
    # exit(0)

    students = [Student(student['name'], student['score']) for student in students_data]

    for student in students:
        grade = evaluate_grade(student)
        print(f"Student: {student.name}, Score: {student.score}, Grade: {grade}")

if __name__ == "__main__":
    main()
