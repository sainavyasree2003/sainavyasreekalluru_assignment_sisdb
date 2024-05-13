from Utility import propertyutil
from Utility.propertyutil import DBConnectivity
from entity.payment import Payment
from entity.students import Students
from entity.course import Course
from entity.enrollment import Enrollment
from entity.teacher import Teacher
from mycollections.my_collections import Student, Course, Teacher,Enrollment,Payment

from customexceptions.myexception import *

class DBInteraction:
    def __init__(self):
        self.propertyutil = DBConnectivity()

    def create_student(self):
        try:
           conn = self.propertyutil.makeconnection()
           if conn is None:
               print("no connection")
           cursor = conn.cursor()
           self.student_id = int(input("Enter student id: "))
           self.first_name = input("Enter student first name: ")
           self.last_name = input("Enter student last name: ")
           self.date_of_birth = input("Enter student date of birth: ")
           self.email = input("Enter student email id: ")
           self.phone_number = input("Enter student phone number: ")
           cursor.execute(
            "INSERT INTO Students (student_id, first_name, last_name, date_of_birth, email, phone_number) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (self.student_id, self.first_name, self.last_name, self.date_of_birth, self.email, self.phone_number))
           conn.commit()
           conn.close()
        except InvalidStudentDataException as e:
           print(e)
        except Exception as e:
            (print(str(e) + "---error in creating student:---"))
        conn.close()
        return None



    def create_course(self):
            try:
                conn = self.propertyutil.makeconnection()
                if conn is None:
                    print("no connection")
                cursor = conn.cursor()
                self.course_id = int(input("Enter course_id: "))
                self.course_name= input("Enter course_name: ")
                self.course_code = int(input("Enter course_code "))
                self.instructor_name = input("Enter instructor_name: ")

                cursor.execute(
                "INSERT INTO Course (course_id, course_name, course_code, instructor_name) VALUES (%s, %s, %s, %s)",
                (self.course_id, self.course_name, self.course_code, self.instructor_name))
                conn.commit()
                conn.close()
            except InvalidCourseDataException as e:
                    print(e)
            except Exception as e:
                      (print(str(e) + "---error in creating course:---"))
                  #conn.close()
                  #return None

    def create_enrollment(self):
        try:
            conn = propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            if conn is None:
                print("no connection")
            cursor = conn.cursor()
            self.enrollment_id= int(input("enrollment_id: "))
            self.student_id= int(input("Enter student_id: "))
            self.course_id= int(input("Enter course_id "))
            self.enrollment_date = input("Enter enrollment_date: ")
            cursor.execute(
                "INSERT INTO Enrollment (enrollment_id, student_id, course_id, enrollment_date) VALUES (%s, %s, %s, %s)",
                (self.enrollment_id, self.student_id, self.course_id,self.enrollment_date))
            conn.commit()
            conn.close()
        except InvalidEnrollmentDataException as e:
           print(e)
        except Exception as e:
            (print(str(e) + "---error in creating enrollment:---"))

    def create_teacher(self):
        try:
            conn = propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            if conn is None:
                print("no connection")
            cursor = conn.cursor()
            self.teacher_id = int(input("Enter teacher_id: "))
            self.first_name = input("Enter first_name: ")
            self.last_name = input("Enter last_name ")
            self.email = input("Enter email: ")

            cursor.execute(
                "INSERT INTO Teacher (teacher_id, first_name, last_name, email) VALUES (%s, %s, %s, %s, %s)",
                (self.teacher_id, self.first_name, self.last_name, self.email))

            conn.commit()
            conn.close()
        except InvalidTeacherDataException as e:
           print(e)
        except Exception as e:
            (print(str(e) + "---error in creating teacher:---"))
        conn.close()
        return None

    def create_payment(self):
        try:
            conn = self.propertyutil.makeconnection()
            if conn is None:
                print("no connection")
            cursor = conn.cursor()
            self.payment_id  = int(input("Enter payment_id : "))
            self.student_id = int(input("Enter student_id: "))
            self.amount = int(input("Enter amount "))
            self.payment_date = input("Enter payment_date: ")

            cursor.execute("INSERT INTO Payment (payment_id, student_id, amount, payment_date) VALUES (%s, %s, %s, %s)",
                           (self.payment_id, self.student_id, self.amount,self.payment_date))

            conn.commit()
            conn.close()
        except Exception as e:
            (print(str(e) + "---error in creating teacher:---"))


    def get_student_by_id(self):
        try:
            conn =propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            self.student_id = int(input("Enter student_id: "))
            cursor.execute("SELECT * FROM Students WHERE student_id = %s",[(self.student_id )])
            row = cursor.fetchone()
            if row:
                student = Student(row[0], row[1], row[2], row[3], row[4], row[5])
                conn.close()
                return student
            else:
                raise StudentNotFoundException("entered student_id is not found")
        except StudentNotFoundException as e:
                print(e)
        except Exception as e:(
                print(str(e) + "---error in getting students:---"))

    def get_course_by_id(self):
        try:
            conn = propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            self.course_id = int(input("Enter course_id: "))
            cursor.execute("SELECT * FROM Course WHERE course_id = %s",[(self.course_id)])
            row = cursor.fetchone()

            if row:
                course = Course(row[0], row[1], row[2], row[3])
                conn.close()
                return course
            else:
                raise CourseNotFoundException("entered course_id is not found")
        except CourseNotFoundException as e:
                print(e)
        except Exception as e:
            print(str(e) + "---error in getting course:---")
            conn.close()
            return None

    def get_enrollments_for_student(self):
            conn = propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            self.student_id = int(input("Enter student_id: "))
            cursor.execute("SELECT * FROM Enrollment WHERE student_id = %s",[(self.student_id)])
            rows = cursor.fetchall()

            enrollments = []
            for row in rows:
                course = DBInteraction.get_course_by_id(row[2])
                enrollment = Enrollment(row[0], student, course, row[3])
                enrollments.append(enrollment)

            conn.close()
            return enrollments

    def get_enrollments_for_course(self):
            conn =propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            self.course_id = int(input("Enter course_id: "))
            cursor.execute("SELECT * FROM Enrollment WHERE course_id = %s",[(self.course_id)])
            rows = cursor.fetchall()

            enrollments = []
            for row in rows:
                student = DBInteraction.get_student_by_id(row[1])
                enrollment = enrollment(row[0], student, course, row[3])
                enrollments.append(enrollment)

            conn.close()
            return enrollments

    def enroll_in_course(self):
        try:
            conn = propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            self.enrollement_id=int(input("enter enrollment_id:"))
            self.student_id=int(input("enter student_id:"))
            self.course_id=int(input("course_id:"))
            self.enrollment_date=input("enter enrollment_date: ")
            sql = "INSERT into Enrollment (enrollment_id,student_id,course_id,enrollment_date) values (%s,%s,%s,%s) "
            values =[(self.enrollement_id, self.student_id, self.course_id,self. enrollment_date)]
            cursor.execute(sql, (values,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(str(e))
            return False


    def get_payments_for_student(self):
        try:
            conn =propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            self.student_id = int(input("Enter student_id: "))
            cursor.execute("SELECT * FROM Payment WHERE student_id = %s",[(self.student_id)])
            records = cursor.fetchall()
            if records:
                print('_______Records In payment Table___')
            for i in records:
                print(i)
            else:
                conn.close()
        except Exception as e:
            print(str(e))


    def get_payment_amount(self):
        try:
            conn =propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            self.student_id=int(input("enter student_id :"))
            cursor.execute("SELECT amount FROM Payment WHERE student_id = %s",[(self.student_id)])
            records = cursor.fetchall()
            if records:
                print('_______Records In payment Table___')
            for i in records:
                print(i)
            else:
                conn.close()
        except Exception as e:
            print(str(e))


    def get_payment_date(self):
        try:
            conn =propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            self.student_id=int(input("enter student_id :"))

            cursor.execute("SELECT payment_date  FROM Payment WHERE student_id = %s",[(self.student_id)])
            records = cursor.fetchall()
            if records:
                print('_______Records In payment Table___')
            for i in records:
                print(i)
            else:
                conn.close()
        except Exception as e:
             print(str(e))

    def get_teacher_by_id(self):
        try:
            conn = propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            self.teacher_id = int(input("Enter teacher_id: "))
            cursor.execute("SELECT * FROM Teacher WHERE teacher_id = %s",[(self.teacher_id )])
            records = cursor.fetchall()
            if records:
                print('_______Records In teacher Table___')
            for i in records:
                print(i)
            else:
                conn.close()
                raise InvalidTeacherDataException("entered teacher_id is not found")
        except Exception as e:
            print(str(e) + "---error in getting teacher:---")


    def update_student(self):
        try:
            conn = self.propertyutil.makeconnection()
            if conn is None:
                print("no connection")
            cursor = conn.cursor()
            self.student_id = int(input("Enter student id: "))
            self.first_name = input("Enter student first name: ")
            self.last_name = input("Enter student last name: ")
            self.date_of_birth = input("Enter student date of birth: ")
            self.email = input("Enter student email id: ")
            self.phone_number = input("Enter student phone number: ")
            cursor.execute(
                "UPDATE Students SET first_name = %s, last_name = %s, date_of_birth = %s, email = %s, phone_number = %s WHERE student_id = %s",
                (self.first_name, self.last_name, self.date_of_birth, self.email, self.phone_number,self.student_id))

            conn.commit()
            conn.close()
            return True
        except Exception as e:
            (print(str(e) + "---error in updating student:---"))

    def update_enrollment(self):
        try:
            conn = propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            if conn is None:
                print("no connection")
            cursor = conn.cursor()
            self.enrollment_id = int(input("enrollment_id: "))
            self.student_id = int(input("Enter student_id: "))
            self.course_id = int(input("Enter course_id "))
            self.enrollment_date = input("Enter enrollment_date: ")

            cursor.execute(
                "UPDATE Enrollment SET  student_id=%s, course_id=%s , enrollment_date=%s WHERE enrollment_id = %s",
                (self.student_id,self.course_id,self.enrollment_date,self.enrollment_id))
            conn.commit()
            conn.close()
        except Exception as e:
            (print(str(e) + "---error in updating student:---"))

    def update_payment(self):
        try:
            conn = self.propertyutil.makeconnection()
            if conn is None:
                print("no connection")
            cursor = conn.cursor()
            self.payment_id = int(input("Enter payment_id : "))
            self.student_id = int(input("Enter student_id: "))
            self.amount = int(input("Enter amount "))
            self.payment_date = input("Enter payment_date: ")

            cursor.execute(
            "UPDATE Payment SET   student_id=%s, amount=%s, payment_date=%s WHERE payment_id = %s",
            (self.payment_id,self.student_id,self.amount,self.payment_date))

            conn.commit()
            conn.close()
        except Exception as e:
            (print(str(e) + "---error in updating payment:---"))


    def update_course(self):
        try:
            conn = self.propertyutil.makeconnection()
            if conn is None:
                print("no connection")
            cursor = conn.cursor()
            self.course_id = int(input("Enter course_id: "))
            self.course_name = input("Enter course_name: ")
            self.course_code = int(input("Enter course_code "))
            self.instructor_name = input("Enter instructor_name: ")

            cursor.execute(
                "UPDATE Course SET course_name = %s, course_code = %s, instructor_name = %s WHERE course_id = %s",
                (self.course_name, self.course_code,self.instructor_name,self.course_id))
            conn.commit()
            conn.close()
        except Exception as e:
            (print(str(e) + "---error in updating course:---"))

    def update_teacher(self):
            conn = propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            self.teacher_id = int(input("Enter teacher id to update:"))
            self.first_name = input("Enter first name:")
            self.last_name = input("Enter last name:")
            self.email = input("Enter email:")
            sql = "UPDATE Teacher SET first_name = %s, last_name = %s, email = %s WHERE teacher_id = %s "
            values = [(self.first_name, self.last_name, self.email, self.teacher_id)]

            cursor.executemany(sql, values)
            conn.commit()
            conn.close()

    def delete_student(self):
            conn = propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            self.student_id = int(input("Enter student_id to delete"))
            sql = "delete from  Student  WHERE student_id = %s "
            values = [(self.student_id)]

            cursor.execute(sql, values)
            conn.commit()
            conn.close()

    def delete_enrollment(self):
            conn = propertyutil.DBConnectivity().makeconnection()
            cursor = conn.cursor()
            self.enrollement_id = int(input("Enter enrollment_id to delete"))
            sql = "delete from  Enrollment  WHERE enrollment_id = %s"
            values = [(self.enrollment_id)]

            cursor.execute(sql, values)
            conn.commit()
            conn.close()

    def delete_payment(self):
        conn = propertyutil.DBConnectivity().makeconnection()
        cursor = conn.cursor()
        self.payment_id = int(input("Enter payment_id to delete"))
        sql = "delete from  Payment  WHERE payment_id = %s"
        values = [self.payment_id]

        cursor.execute(sql, values)
        conn.commit()
        conn.close()

    def delete_teacher(self):
        conn = propertyutil.DBConnectivity().makeconnection()
        cursor = conn.cursor()
        self.teacher_id = int(input("Enter teacher_id to delete"))
        sql = "delete from  Teacher  WHERE teacher_id = %s "
        values = [self.teacher_id]

        cursor.execute(sql, values)
        conn.commit()
        conn.close()

    def delete_course(self):
        conn = propertyutil.DBConnectivity().makeconnection()
        cursor = conn.cursor()
        self.course_id = int(input("Enter course_id to delete"))
        sql = "delete from  Course  WHERE course_id = %s "
        values = [self.course_id]

        cursor.execute(sql, values)
        conn.commit()
        conn.close()

    def make_payment(self):
        try:
            conn = self.propertyutil.makeconnection()
            if conn is None:
                print("no connection")
            cursor = conn.cursor()
            self.payment_id = int(input("Enter payment_id : "))
            self.student_id = int(input("Enter student_id: "))
            self.amount = int(input("Enter amount "))
            self.payment_date = input("Enter payment_date: ")

            cursor.execute("INSERT INTO Payment (payment_id, student_id, amount, payment_date) VALUES (%s, %s, %s, %s)",
                           (self.payment_id, self.student_id, self.amount,self.payment_date))
            conn.commit()
            conn.close()
        except Exception as e:
            (print(str(e) + "---error in making payment:---"))


    def get_enrolled_courses(self):
            try:
                conn = propertyutil.DBConnectivity().makeconnection()
                cursor = conn.cursor()
                self.student_id = int(input("Enter student_id: "))
                cursor.execute("SELECT * FROM Students WHERE student_id = %s", [(self.student_id)])
                records = cursor.fetchall()
                if records:
                    print('_______Records In course Table___')
                for i in records:
                    print(i)
                else:
                    conn.close()
            except Exception as e:
                print(str(e) + "---error in getting courses:---")

    def assign_teacher(self):
        try:
            conn = self.propertyutil.makeconnection()
            if conn is None:
                print("no connection")
            cursor = conn.cursor()
            self.course_id = int(input("Enter course_id: "))
            self.instructor_name = input("Enter instructor_name: ")

            cursor.execute(
                "update  Course set instructor_name = %s WHERE course_id = %s ",(self.instructor_name,self.course_id))
            conn.commit()
            conn.close()
        except Exception as e:
            (print(str(e) + "---error in assigning teacher :---"))

    def get_courses_assigned_teacher(self):
        try:
            conn = self.propertyutil.makeconnection()
            if conn is None:
                print("no connection")
            cursor = conn.cursor()
            self.instructor_name = input("Enter instructor_name: ")

            cursor.execute(
                "select course_id,course_name from Course where instructor_name = %s", [(self.instructor_name)])
            conn.commit()
            conn.close()
        except Exception as e:
            (print(str(e) + "---error in assigning teacher :---"))

    def get_assigned_teacher_for_course(self):
        try:
            conn = self.propertyutil.makeconnection()
            if conn is None:
                print("no connection")
            cursor = conn.cursor()
            self.course_id = int(input("Enter course_id: "))

            cursor.execute(
                "select instructor_name from Course where course_id= %s",[(self.course_id)])
            conn.commit()
            conn.close()
        except Exception as e:
            (print(str(e) + "---error in finding teacher :---"))





