

class Payment:
    def _init_(self, payment_id, student_id, amount, payment_date):
        self.payment_id = payment_id
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date

    def payment_id(self):
        return self.payment_id

    def get_student_id(self):
        return self.student_id

    def get_amount(self):
        return self.amount

    def get_payment_date(self):
        return self.payment_date


