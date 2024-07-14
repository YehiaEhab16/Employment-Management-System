import tkinter as tk
from gui import BaseApp
from authentication import Auth

class EmployeeManagementApp(BaseApp):
    def login(self):
        if super().login():
            self.showInputDialog('Login',{'ID':'','Password':''}, self.authenticate)

    def logout(self):
        super().logout()
        self.auth.logout()

    def displayInfo(self):
        employeeInfo = super().displayInfo()
        if employeeInfo is not None:
            self.showDialog('Employee Data', employeeInfo, '200x250')

    def addEmployee(self):
        super().addEmployee()
    
    def removeEmployee(self):
        super().removeEmployee()
    
    def updateEmployee(self):
        super().updateEmployee()

    def calculateBonus(self):
        bonus = super().calculateBonus()
        if bonus is not None:
            self.showDialog('Employee Bonus', {'Employee':self.auth.getAuthUser(),'Bonus':bonus})

    def calculateDiscount(self):
        discount = super().calculateDiscount()
        if discount is not None:
            self.showDialog('Employee Discount', {'Employee':self.auth.getAuthUser(),'Discount':discount})

    def getRemainingHolidays(self):
        holidays = super().getRemainingHolidays()
        if holidays is not None:
            self.showDialog('Employee Holidays', {'Employee':self.auth.getAuthUser(),'Remaining Holidays':holidays},'220x80')    
        
    def authenticate(self, id, password) -> bool:
        if id != '' and password != '' and id.isdigit():
            loginStatus = self.auth.login(int(id), password)
            if loginStatus == Auth.LoggedIn:
                self.employeeName.config(text='Welcome, ' + self.auth.getAuthUser())
                return True
            elif loginStatus == Auth.UserNotFound:
                self.showErrorDialog('Employee not found')
                return False
            elif loginStatus == Auth.WrongPassword:
                self.showErrorDialog('Wrong Password')
                return False
            elif loginStatus == Auth.MaxAttemptsReached:
                self.showErrorDialog('Max Attempts Reached')
                self.root.destroy()
                return False
        else:
            self.showErrorDialog('Please ensure id and password are valid')
            return False
        
    def selectEmployeeId(self, operation:int):
        if super().selectEmployeeId(operation):
            if operation == BaseApp.AddEmployee:
                self.showInputDialog('Employee Data', {"Name":'', "Department":'', "Salary":'', "Password":'', "Days of Absence":''}, self.addEmployeeData, '300x450')                

            elif operation == BaseApp.UpdateEmployee:
                self.showInputDialog('Which Employee ?', {'ID':''}, self.getID, '250x150')

            elif operation==BaseApp.RemoveEmployee:
                self.showInputDialog('Which Employee ?', {'ID':''}, self.removeID, '250x150')

    def addEmployeeData(self, name:str, department:str, salary:str, password:str, days:str) -> bool:
        if name != '' and department!='' and salary!='' and salary.isdigit() and password !='' and days !='' and days.isdigit():
            employee = {"Name": name, "Department": department, "Salary": int(salary), "Password": password, "Days of Absence": int(days)}
            super().addEmployee(employee)
            self.showErrorDialog('Employee added successfully')
            return True
        else:
            self.showErrorDialog('Please ensure all fields are valid')
            return False
        
    def updateEmployeeData(self, id:str, name:str, department:str, salary:str, password:str, days:str) -> bool:
        if id != '' and id.isdigit() and name != '' and department!='' and salary!='' and salary.isdigit() and password !='' and days !='' and days.isdigit():
            employee = {"Name": name, "Department": department, "Salary": int(salary), "Password": password, "Days of Absence": int(days)}
            if super().updateEmployee(int(id), employee):
                self.showErrorDialog('Employee updated successfully')
                return True
            else:
                self.showErrorDialog('No employee found with selected ID')
                return False
        else:
            self.showErrorDialog('Please ensure all fields are valid')
            return False
            
    def removeID(self, id:str) -> bool:
        if id != '' and id.isdigit():
            if super().removeEmployee(int(id)):
                self.showErrorDialog('Employee removed successfully')
                return True
            else:
                self.showErrorDialog('No employee found with selected ID')
                return False
        else:
            self.showErrorDialog('Please enter a valid id')
            return False
    
    def getID(self, id:str) -> bool:
        if id != '' and id.isdigit():
            employee = super().getEmployee(int(id))
            if employee is not None:
                self.showInputDialog('Update Data', employee, self.updateEmployeeData, '300x500')
                return True
            else:
                self.showErrorDialog('No employee found with selected ID')
                return False
        else:
            self.showErrorDialog('Please enter a valid id')
            return False

if __name__ == '__main__':
    root = tk.Tk()
    app = EmployeeManagementApp(root)
    root.mainloop()
    