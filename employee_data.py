import json

class EmployeeData:
    EmployeeNotFound = -1
    def __init__(self):
        self.jsonFile = 'data.json'
        self.maxHolidays = 21
        self.readData()

    def storeData(self):  
        with open(self.jsonFile, 'w') as f:
            json.dump(self.currentData, f)

    def readData(self):
        with open(self.jsonFile, 'r') as f:
            self.currentData = json.load(f)
        
    def addEmployee(self, employee:dict):
        employeeData = {'ID':len(self.currentData)}
        employeeData.update(employee)
        self.currentData.append(employeeData)
        self.storeData()

    def getEmployee(self, id:int) -> dict:
        for index, employee in enumerate(self.currentData):
            if id == employee['ID']:
                return self.currentData[index]
        return None
    
    def removeEmployee(self, id:int) -> bool:
        for index, employee in enumerate(self.currentData):
            if id == employee['ID']:
                self.currentData.pop(index)
                self.storeData()
                return True
        return False
    
    def updateEmployee(self, id:int, employeeUpdate:dict) -> bool:
        for index, employee in enumerate(self.currentData):
            if id == employee['ID']:
                newEmployee = {'ID':id}
                newEmployee.update(employeeUpdate)
                self.currentData[index] = newEmployee
                self.storeData()
                return True
        return False