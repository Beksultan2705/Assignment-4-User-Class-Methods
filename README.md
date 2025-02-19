To complete this project, I have created 4 python files for better readability of the code 
and its structure, and now I will tell you what these codes do individually and how they are related.


1) User.py
   In the file User.py we are creating a User class that represents the user of the system. This class stores
   information about a user, such as their ID, first name, last name, email address, password, and date of birth.

We are also adding two methods:
get_details()
get_age()

2) UserService.py
This file is needed for manipulating input data.

This file Contains methods for adding, searching, deleting, and updating users:
"add_user" - adds a new user.
"find_user" — finds the user by his ID.
"delete_user" — deletes the user by his ID.
"update_user" — updates the user's data by his ID.
"get_number" — returns the number of all users.
