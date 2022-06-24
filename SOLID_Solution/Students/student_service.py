from SOLID_Solution.Exceptions.invalid_email import invalid_email
from SOLID_Solution.book_allowance_setter import book_allowance_setter
from SOLID_Solution.logger import log


class studen_service:
    def add_if_valid(self, emailAddress, universityId, student_repository, university_repository):
        log("Start add student with email", emailAddress)
        self.validate_email(emailAddress)

        if student_repository.exists(emailAddress):
            return

        theUniversity = university_repository.get_by_id(universityId)
        theStudent = student_repository.create_student(emailAddress, universityId)

        thePackage_type = theUniversity.get_package_type()
        theBoodAllowanceSetter = book_allowance_setter(theStudent)
        theBoodAllowanceSetter.set_allowance(thePackage_type)
        student_repository.add(theStudent)

        log("End add student with email", emailAddress)

    def validate_email(self, emailAddress):
        if emailAddress == "":
            raise invalid_email("Empty")
