from employee_data import EmployeeData

class Operations(EmployeeData):
    def displayInfo(self, id:int) -> dict:
        return self.getEmployee(id)
    
    def getSalaryWithFactor(self, id:int, factor:float):
        for employee in self.currentData:
            if id == employee['ID']:
                return employee['Salary'] * factor
        else:
            return EmployeeData.EmployeeNotFound

    def calculateBonus(self, id:int) -> int:
        return self.getSalaryWithFactor(id,0.1)

    def calculateDiscount(self, id:int) -> int:
        return self.getSalaryWithFactor(id,0.05)
   
    def getRemainingHolidays(self, id) -> int:
        for employee in self.currentData:
            if id == employee['ID']:
                numDays = self.maxHolidays - employee['Days of Absence'] 
                return numDays if numDays>0 else 0
        else:
            return EmployeeData.EmployeeNotFound

    