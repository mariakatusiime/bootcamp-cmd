class User:
    users =[]
    scores =[]
    def __init__(self,role,username,password):
        self.role = role
        self.password = password
        self.username = username
    
    def add_user(self):
        user ={}
        user['username'] = self.username
        user['password'] = self.password
        user['role'] = self.role
        self.users.append(user)
        print('User {} successfully added'.format(self.username))
        print('Logging you in...')
        self.login(self.username, self.password)

    @classmethod
    def login(cls, username, password):
        found_user = False
        user_data = {}
        for user in cls.users:
            if user['username'] == username and user['password'] == password:
                print("{} has been logged in".format(username))
                print("########## ", user)
                user_data = user
                found_user = True
            found_user = False
            
        if found_user:
            return {'role':user_data.get('role'), 'username':user_data.get('username')}

    def view_scores(self):
        if self.role == "lf":
            print("")
            #show all scores
        elif self.role == "lfa":
            print("")
            #get lfa bootcampers and show scores
        else:
            print("")
       
class LearningFacilitatorAssistants(User):
    def __init__(self,role,username,password):
        super.__init__(role,username,password)


    def view_scores(self):
        pass
    def add_scores(self):
        pass
    def edit_score(self):
        pass

class LearningFacilitators(User):
    def __init__(self,role, username, password):
        super.__init__(role, username, password)

    def view_scores(self):
        pass

class Bootcampers(User):
    def __init__(self, role, username, password, score):
        super.__init__(role, username, password)
        self.score = score
        self.score = []

    def view_scores(self):
        return self.score