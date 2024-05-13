class Course:
    def _init_(self, course_id, course_name="", course_code="", instructor_name=""):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name

    def course_id (self):
        return self.course_id

    def get_course_name(self):
        return self.course_name

    def get_course_code(self):
        return self.course_code

    def get_instructor_name(self):
        return self.instructor_name



