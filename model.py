from Employ_register.configration import db

class Employee(db.Model):
    __tablename__="emp_info"
    Empid = db.Column(db.Integer(), primary_key = True)
    FirstName = db.Column(db.String(15))
    LastName = db.Column(db.String(15))
    DOB = db.Column(db.Float())
    Address = db.Column(db.String(15))
    Gender = db.Column(db.String(15))
    Email = db.Column(db.String(15))
    active = db.Column("prod_active", db.String(100), default="Y")

    @staticmethod
    def dummy_employee():
        return Employee(Empid='', FirstName='', LastName='', DOB='', Address='', Gender='', Email='')