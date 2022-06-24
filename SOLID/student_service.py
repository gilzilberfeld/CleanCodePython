from SOLID.not_implemented_exception import not_implemented_exception
from SOLID.student import student
from SOLID.student_reporsitory import student_repository
from SOLID.university_repository import university_repository


class StudentService:
    def AddIfValid(self, emailAddress, universityId):

        # SRP
        print("Log: Start add student with email  %s", emailAddress)

        if emailAddress == "":
            return False

        studentRepository = student_repository()

        if studentRepository.exists(emailAddress):
            return False

        universityRepository = university_repository()
        theUniversity = universityRepository.get_by_id(universityId)

        theStudent = student(emailAddress, universityId)

        # SRP, OCP
        package_type = theUniversity.get_package_type()
        if package_type == package_type.Standard:
            theStudent.set_monthly_book_allowance(10)
        else:
            if package_type == package_type.Premium:
                theStudent.set_monthly_book_allowance(10 * 2)

        studentRepository.add(theStudent)

        # SRP
        print("Log: End add student with email  %s", emailAddress)

        # CQS
        return True

    def GetStudentsByUniversity(self):
        raise not_implemented_exception()

    def GetStudentsByCurrentlyBorrowedEbooks(self):
        raise not_implemented_exception()
