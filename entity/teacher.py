class Teacher:
    def _init_(self, teacher_id, first_name="", last_name="", email=""):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_teacher_id(self):
        return self.teacher_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email
