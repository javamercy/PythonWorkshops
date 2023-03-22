from student import Student
from studentManager import StudentManager

student1 = Student("Emre", "Kurşun")
student2 = Student("Ahmet", "Eren")
student3 = Student("Osman", "Yücesoy")
student4 = Student("Cemal", "Taş")
studentManager = StudentManager()
studentManager.add(student1)
studentManager.addMultiple([student2, student3, student4])
print(studentManager.getStudentNumber(student1))
print(studentManager.getStudentNumber(student2))
print(studentManager.getStudentNumber(student3))
studentManager.printAllStudents()
studentManager.delete(student1)
studentManager.printAllStudents()
