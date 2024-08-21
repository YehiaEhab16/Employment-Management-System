import tkinter as tk
from tkinter import messagebox
from operations import Operations
from authentication import Auth

class BaseApp(Operations):
    AddEmployee = 0
    UpdateEmployee = 1
    RemoveEmployee = 2

    def __init__(self, root):
        super().__init__()
        self.auth = Auth(self.currentData)
        self.root = root
        self.root.title('Employee Management App')
        self.root.geometry('500x300')
        self.root.configure(bg='#1a1b26')

        title = tk.Label(self.root, text='Employee Management App', font=('Helvetica', 16, 'bold'), fg='#ff9e64', bg ='#1a1b26')
        title.pack(pady=15)

        self.employeeName = tk.Label(self.root, text='Not Logged In', font=('Helvetica', 14, 'bold'), fg='#e0af68', bg ='#1a1b26')
        self.employeeName.pack(pady=5)

        buttoFrame = tk.Frame(self.root, bg='#1a1b26')
        buttoFrame.pack(pady=20)

        buttonOptions = {'font': ('Helvetica', 11, 'bold'), 'bg': '#565f89', 'fg': 'white', 
                               'relief': 'raised', 'borderwidth': 3, 'activebackground': '#414868', 'activeforeground': 'white'}
        
        buttons = {'Login': self.login, 'Log Out': self.logout, 'Display Info': self.displayInfo, 'Add Employee': lambda:self.selectEmployeeId(BaseApp.AddEmployee), 
                   'Remove Employee': lambda:self.selectEmployeeId(BaseApp.RemoveEmployee), 'Update Employee': lambda:self.selectEmployeeId(BaseApp.UpdateEmployee), 
                   'Calculate Bonus': self.calculateBonus, 'Calculate Discount': self.calculateDiscount, 'Remaining Holidays': self.getRemainingHolidays}

        # Create and place buttons in the grid
        row, column = 0, 0
        for name, func in buttons.items():
            button = tk.Button(buttoFrame, text=name, command=func, **buttonOptions)
            button.grid(row=row, column=column, padx=10, pady=10)
            column += 1
            if column > 2: 
                column = 0
                row += 1

    def createDialog(self,title,size):
        dialog = tk.Toplevel()
        dialog.title(title)
        dialog.geometry(size)
        dialog.transient(self.root)
        dialog.configure(bg='#1a1b26')
        return dialog
    
    def showErrorDialog(self, message:str):
        messagebox.showinfo("Dialog", message) 

    def showDialog(self, title:str, data, size='200x80'):
        dialog = self.createDialog(title,size)

        if type(data) == str :
            label = tk.Label(dialog, text=data, bg='#1a1b26', fg='white')
            label.pack(pady=15)
        elif type(data) == dict:
            row = 0
            for key, value in data.items():
                keyLabel = tk.Label(dialog, text=f'{key}:', bg='#1a1b26', fg='#ff9e64')
                keyLabel.grid(row=row, column=0, padx=10, pady=(10, 5), sticky='e')
                
                valueLabel = tk.Label(dialog, text=f'{value}', bg='#1a1b26', fg='#e0af68')
                valueLabel.grid(row=row, column=1, padx=10, pady=(10, 5), sticky='w')
                
                row += 1

    def showInputDialog(self, title:str, fields:dict[str], button, size = '300x200'):
        dialog = self.createDialog(title,size)

        entries = []
        for field,initText in fields.items():
            label = tk.Label(dialog, text=f'{field}:', bg='#1a1b26', fg='white') 
            label.pack(pady=(20, 5))
            entry = tk.Entry(dialog, show='*') if field.lower()=='password' else  tk.Entry(dialog)
            entry.insert(0,initText)
            entry.pack(pady=5)
            entries.append(entry)

        submit_button = tk.Button(dialog, text='Submit', bg='#e0af68', fg='#1a1b26', command=lambda: self.submit_input(entries, button, dialog))
        submit_button.pack(pady=(10, 20))
    
    def submit_input(self, entries, button, dialog):
        input_values = [entry.get() for entry in entries]
        if button(*input_values):
            dialog.destroy()

    def login(self) -> bool:
        if self.auth.getAuthUser() is not None:
            self.showErrorDialog('Already Logged In')
            return False
        else:
            return True
        
    def logout(self):
        if self.auth.getAuthUser() is None:
            self.showErrorDialog('Please Login First')
        else:
            self.employeeName.config(text='Not Logged In')
        
    def displayInfo(self):
        if self.auth.getAuthUser() is None:
            self.showErrorDialog('Please Login First')
        else:
            return super().displayInfo(self.auth.getAuthUserId())
    
    def calculateBonus(self):
        if self.auth.getAuthUser() is None:
            self.showErrorDialog('Please Login First')
        else:
            return super().calculateBonus(self.auth.getAuthUserId())

    def calculateDiscount(self):
        if self.auth.getAuthUser() is None:
            self.showErrorDialog('Please Login First')
        else:
            return super().calculateDiscount(self.auth.getAuthUserId())

    def getRemainingHolidays(self):
        if self.auth.getAuthUser() is None:
            self.showErrorDialog('Please Login First')
        else:
            return super().getRemainingHolidays(self.auth.getAuthUserId())       
        
    def selectEmployeeId(self,operation:int) -> bool:
        if self.auth.getAuthUser() is None:
            self.showErrorDialog('Please Login First')
            return False
        else:
            if self.auth.getAuthUser() != 'admin':
                self.showErrorDialog('Only admins can perform this operation')
                return False
            else:
                return True
