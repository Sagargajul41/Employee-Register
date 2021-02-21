from Employ_register.configration import app
from Employ_register.model import Employee
from flask import render_template,request
from Employ_register.database import EmployeeOperations
 #Sagar

empop = EmployeeOperations()

@app.route("/emp", methods= ["GET","POST"])       #  http://127.0.0.1:5000/emp
def save_emp_info():
    if request.method== "GET":
        return render_template("Employ_info.html", employee = empop.fetch_all_employee(),emp=Employee.dummy_employee())
    else:
        Empid = request.form["Empid"]
        Fnm = request.form["fnm"]
        Lnm = request.form["lnm"]
        DOB = request.form["DOB"]
        Adr = request.form["adr"]
        gen = request.form["gender"]
        email = request.form["email"]

        emp= Employee( Empid=Empid,Firstname=Fnm, Lastname=Lnm, DOB=DOB, Address=Adr, Gender=gen, Email=email)
        dbstud = empop.fetch_single_employee(Empid)
        if dbstud
            msg = empop.update_employee(Empid, emp)
        else:
            msg = empop.insert_employee(emp)
        return render_template("Employ_info.html", employee= empop.fetch_all_employee(),emp=Employee.dummy_employee())

if __name__=='__main__':
    app.run(debug=True)
