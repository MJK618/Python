#Database Login Checing Program
#By MJK618

db_user_pass = {'user1':'123456',
                'user2':'654321',
                'admin':'pass'}

#Introduction
print("Welcome to Database Login Program")

username = input("\nEnter your Username : ")
password = input("Enter your Password")

if username in db_user_pass:
    print("Checking Credentials")
    print("Authenticating with Database")
    if password == db_user_pass[username]:
        print("Login Succesfull")
        pass_change_choice = input("Would you like to change your password? (y/n)")
        if username == 'admin':
            for key, value in db_user_pass.items():
                print("Username : " + key + "\t" + "Password : " + str(value))
        if pass_change_choice.startswith('y'):
            new_password = input("Enter new Password")
            if len(new_password) < 6:
                print("Your new password is too short.\nPlease Try Again")
            else:
                db_user_pass[username] = new_password
                print("Password Changed Successfully")
                choice = input("Would you like to see full database? (y/n)")
                print("Login As Admin To Continue")
                username = input("\nEnter your Username : ")
                password = input("Enter your Password")
                if username == 'admin':
                    for key, value in db_user_pass.items():
                        print("Username : " + key + "\t" + "Password : " + str(value))
                else:
                    print("YOU ARE NOT ADMIN!!!")
        else:
            print("Thank you for using me")
    else:
        print("Password doesn't match\nLogin as admin to see the database")
else:
    print("User Not Found In Database \n GOODBYE")
            


