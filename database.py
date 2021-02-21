from Employ_register.model import Employee,db

  #--> to create the tables..
db.create_all()
class EmployeeOperations:
    def insert_employee(self, employee):
        if type(employee)== Employee:
            db.session.add(employee)
            db.session.commit()
            return "Employee Added Successfully...!"
        return "Invalid Product Type"


    def fetch_all_employee(self):
        return Employee.query.filter(Employee.active=='Y').all()


        #-->Kapil myakal

