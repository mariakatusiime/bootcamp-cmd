from team_angela import User

def main():
    username = input("Register name:")
    password = input("Register password:")
    role = input("Register role:")

    user = User(role,username,password)
    user.add_user()
    # user.login()
    login_prompt = input("would you like to log in? y/n ")
    if login_prompt is 'y':
        username = input("username: ")
        password = input("password: ")
        isLoggedIn = user.login(username, password)
        if isLoggedIn:
            message = input("Add Scores ")
        else:
            
            return False
    else:
        print("bye!")
        return 0

if __name__ == '__main__':
    main()