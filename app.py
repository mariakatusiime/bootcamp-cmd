from team_angela import User

def main():
    username = input("Register name:")
    password = input("Register password:")
    role = input("Register role:")

    user = User(role,username,password)
    user.add_user()

if __name__ == '__main__':
    main()