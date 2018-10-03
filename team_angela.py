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

    def login(self):

        for user in self.users:
            if user['username'] == self.username and user['password'] == self.password:
                return True
            return False
            

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