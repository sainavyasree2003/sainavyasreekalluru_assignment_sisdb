

class Enrollment:
    def _init_(self, enrollment_id, student_id, course_id , enrollment_date):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date

    def enrollment_id (self):
        return self.enrollment_id

    def get_student_id(self):
        return self.student_id

    def get_course_id(self):
        return self.course_id

    def get_enrollment_date(self):
        return self.enrollment_date

