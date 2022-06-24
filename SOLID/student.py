class student:
    def __init__(self, emailAddress, universityID):
        self.universityID = universityID
        self.emailAddress = emailAddress
        self.allowance = 0

    def set_monthly_book_allowance(self, allowance):
        self.allowance = allowance
