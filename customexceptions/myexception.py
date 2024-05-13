class DuplicateEnrollmentException(Exception):
    def __init__(self, message="student is already enrolled in the course"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class CourseNotFoundException(Exception):
    def __init__(self, message=" course is not found"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class StudentNotFoundException(Exception):
    def __init__(self, message="student  not found"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class TeacherNotFoundException(Exception):
    def __init__(self, message="teacher not found"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class PaymentValidationException(Exception):
    def __init__(self, message="error in payment validation"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class InvalidStudentDataException(Exception):
    def __init__(self, message="invalid student data"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class InvalidCourseDataException(Exception):
    def __init__(self, message="invalid course data"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class InvalidEnrollmentDataException(Exception):
    def __init__(self, message="invalid enrollment data"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class InvalidTeacherDataException(Exception):
    def __init__(self, message="invalid teacher data"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient funds for operation"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
