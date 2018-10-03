from team_angela import User

def main():
    login_prompt = input("Enter a letter, Login - l, Register - r, Exit - e: ")
    if login_prompt is 'l':
        username = input("username: ")
        password = input("password: ")
        isLoggedIn = User.login(username, password)
        if isLoggedIn:
            check_or_add_scores = input("Enter V to view scores or I to insert scores: ")
        else:
            print("Login failed. Exiting")
            
            return False
    elif login_prompt is 'r':
        username = input("Register name:")
        password = input("Register password:")
        role = input("Register role:")

        user = User(role,username,password)
        user.add_user()
        isLoggedIn = User.login(username, password)
        if isLoggedIn:
            check_or_add_scores = input("Enter V to view scores or I to insert scores: ")
        else:
            print("Login failed. Exiting")
    else:
        print("bye!")
        return 0
    

    
    # user.login()
    
if __name__ == '__main__':
    main()