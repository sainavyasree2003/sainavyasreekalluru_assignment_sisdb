class Students:
    def _init_(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth= date_of_birth
        self.email = email
        self.phone_number = phone_number

    def get_student_id(self):
        return self.student_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_dob(self):
        return self.dob

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

