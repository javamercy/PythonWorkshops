from student import Student


class StudentManager:
    def __init__(self) -> None:
        self.students: list[Student] = list()

    def add(self, student: Student) -> None:
        self.students.append(student)
        print("Student was added: " + student.firstName + " " + student.lastName)

    def addMultiple(self, students: list[Student]) -> None:
        count: int = 0
        while (count < len(students)):
            self.students.append(students[count])
            count += 1

    def delete(self, student: Student) -> None:
        self.students.remove(student)
        print("Student was deleted: " +
              student.firstName + " " + student.lastName)

    def deleteMultiple(self, students: list[Student]) -> None:
        for student in students:
            self.students.remove(student)
        print("All students were deleted.")

    def printAllStudents(self) -> None:
        for student in self.students:
            print(str(self.students.index(student)) + " - " +
                  student.firstName + " " + student.lastName)
        print("All students were listed.")

    def getStudentNumber(self, student: Student) -> Student:
        return self.students.index(student)
