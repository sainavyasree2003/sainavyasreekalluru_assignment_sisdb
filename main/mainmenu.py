import dao.implement as imp

class Main:
    def __init__(self):
        self.obj_a=imp.DBInteraction()

    def run(self):
        while True:
            print("student information system Menu:")
            print("1. enroll student in course")
            print("2. update student info")
            print("3. make payment")
            print("4.display student info")
            print("5.get student enrolled courses")
            print("6.payment history of student")
            print("7.assign teacher to course")
            print("8.update course info")
            print("9.list of students enrolled for the course")
            print("10.get assigned teacher for the course")
            print("11.get student associated with enrollment")
            print("12.display course info")
            print("13.update teacher info")
            print("14.display teacher info")
            print("15.get assigned courses to teacher")
            print("16.get payment associated with student")
            print("17.get payment amount")
            print("18.get payment date")
            print("19.display course info")
            print("20.create_student")
            print("21.create_course")
            print("22.create_enrollment")
            print("23.create_teacher")
            print("24.create_payment")
            print("25.update_enrollment")
            print("26.update_payment")
            print("27.delete_student")
            print("28.delete_course")
            print("29.delete_enrollment")
            print("30.delete_teacher")
            print("31.delete_payment")

            choice = int(input("Enter your choice (1-31): "))
            if choice == 1:
                self.obj_a.enroll_in_course()
            elif choice == 2:
                self.obj_a.update_student()
            elif choice == 3:
                self.obj_a. make_payment()
            elif choice == 4:
                self.obj_a. get_student_by_id()
            elif choice == 5:
                self.obj_a.get_enrolled_courses()
            elif choice == 6:
                self.obj_a.get_payments_for_student()
            elif choice == 7:
                self.obj_a.assign_teacher()
            elif choice == 8:
                self.obj_a.update_course()
            elif choice == 9:
                 self.obj_a.get_enrollments_for_course()
            elif choice == 10:
                self.obj_a.get_assigned_teacher_for_course()
            elif choice == 11:
                self.obj_a.get_enrollments_for_student()
            elif choice == 12:
                self.obj_a.get_course_by_id()
            elif choice == 13:
                self.obj_a.update_teacher()
            elif choice == 14:
                 self.obj_a.get_teacher_by_id()
            elif choice == 15:
                self.obj_a.get_courses_assigned_teacher()
            elif choice == 16:
                self.obj_a.get_payments_for_student()
            elif choice == 17:
                self.obj_a.get_payment_amount()
            elif choice == 18:
                self.obj_a.get_payment_date()
            elif choice == 19:
                self.obj_a.get_course_by_id()
            elif choice == 20:
                self.obj_a.create_student()
            elif choice == 21:
                self.obj_a.create_course()
            elif choice == 22:
                self.obj_a.create_enrollment()
            elif choice == 23:
                self.obj_a. create_teacher()
            elif choice == 24:
                self.obj_a. create_payment()
            elif choice == 25:
                self.obj_a.update_enrollment()
            elif choice == 26:
                self.obj_a.update_payment()
            elif choice == 27:
                self.obj_a.delete_student()
            elif choice == 28:
                self.obj_a.delete_course()
            elif choice == 29:
                self.obj_a.delete_enrollment()
            elif choice == 30:
                self.obj_a.delete_teacher()
            elif choice == 31:
                self.obj_a.delete_payment()
            else:
                print("Invalid choice. Please try again.")
            continue_choice = input("To continue press 'y', to stop press 'n':")
            if continue_choice.lower() == 'n':
                break

obj1=Main()
obj1.run()
