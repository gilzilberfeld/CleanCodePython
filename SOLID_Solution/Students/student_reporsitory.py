from SOLID_Solution.Exceptions.not_implemented import not_implemented
from SOLID_Solution.Students.student import student


class student_repository:
    def exists(self, emailAddress):
        raise not_implemented()

    def add(self, theStudent):
        raise not_implemented()

    def create_student(self, emailAddress, universityID):
        return student(emailAddress, universityID)
