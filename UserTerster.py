import datetime
from User import User
from UserService import UserService
from UserUtil import UserUtil

def get_user_input():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    birthday = input("Enter your birthday (YYYY-MM-DD): ")
    birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
    return name, surname, birthday

def main():
    name, surname, birthday = get_user_input()
    
    user_id = UserUtil.generate_user_id() 
    password = UserUtil.generate_password() 
    email = UserUtil.generate_email(name, surname, "example.com") 

    user = User(user_id, name, surname, email, password, birthday)
    UserService.add_user(user)

    print("Users in the System:")
    for user in UserService.users.values():
        print(user.get_details())
        print("Age:", user.get_age())
        print("-")

if __name__ == "__main__":
    main()

