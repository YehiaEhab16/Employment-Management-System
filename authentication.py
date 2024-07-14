class Auth():
    LoggedIn = 0
    UserNotFound = 1
    MaxAttemptsReached = 2
    WrongPassword = 3

    def __init__(self, userData:list[dict]):
        self.authUser = None
        self.authId = None
        self.loginAttempts = 0
        self.maxAttempts = 3
        self.userData = userData

    def updateUserData(self, userData:list[dict]):
        self.userData = userData

    def getAuthUser(self) -> str:
        return self.authUser
    
    def getAuthUserId(self) -> int:
        return self.authId
    
    def logout(self):
        self.authUser = None
    
    def login(self, id:int, password:str) -> int:
        for user in self.userData:
            if id == user['ID']:
                if password == user['Password']:
                    self.authUser = user['Name']
                    self.authId = user['ID']
                    self.loginAttempts = 0
                    return Auth.LoggedIn
                else:
                    self.loginAttempts+=1
                    if self.loginAttempts < self.maxAttempts:
                        return Auth.WrongPassword
                    else:
                        return Auth.MaxAttemptsReached
        else:
            self.loginAttempts+=1
            if self.loginAttempts < self.maxAttempts:
                return Auth.UserNotFound
            else:
                return Auth.MaxAttemptsReached