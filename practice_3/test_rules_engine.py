import unittest
from main import Student, evaluate_grade

class TestEvaluateGrade(unittest.TestCase):
    def test_grade_A(self):
        student = Student("Jane", 92)
        self.assertEqual(evaluate_grade(student), "A")

    def test_grade_B(self):
        student = Student("John", 85)
        self.assertEqual(evaluate_grade(student), "B")

    def test_grade_C(self):
        student = Student("Doe", 76)
        self.assertEqual(evaluate_grade(student), "C")

    def test_grade_D(self):
        student = Student("Alice", 65)
        self.assertEqual(evaluate_grade(student), "D")

    def test_grade_F(self):
        student = Student("Bob", 50)
        self.assertEqual(evaluate_grade(student), "F")

if __name__ == "__main__":
    unittest.main()