print("Well Come To Registration Program.")
# Author: Kedir G. Gamada
# This program is created for the purpose of job application in the existing market.
# The program accepts students and registers for class.
import datetime
autentication = {"user_name":"kedir", "pass_word":"kedir",
"user_name":"gamada", "pass_word":"gamada"
                 }
profile = {}
id_list = ['000','111','222']
course_list = []
register=1
remove=2
quit = 3
selection1 = int(input("Enter 2 if you are current student 1 otherwise:"))

if selection1 == 2:
    #id = input("Enter your ID number:")
    #if id in id_list:
    user_name=input("Enter your user name. ")
    pass_word=input("Enter your password. ")
    if user_name == autentication["user_name"] and pass_word == autentication["pass_word"]:

        while True:
            print("What would like to do?")
            select_task = int(input("Enter 1 to register 2 to remove a course 3 to quit.: "))
            if select_task == 1:
                course_to_register = input("Enter course number to register: ")
                if course_to_register in course_list:
                    print(f"you are already registered for {course_to_register} course.")
                    print("Enter course that you are not already registered for.")
                else:
                    course_list.append(course_to_register)
                print(f"you are registered for:\n{course_list}")
            elif select_task == 2:
                course_to_remove = input("Enter course number to remove: ")
                if course_to_remove in course_list:
                    course_list.remove(course_to_remove)
                    print(f"{course_to_remove} course is removed.")
                else:
                    print(f"you are not registered for {course_to_remove} course.")
            elif select_task == 3:
                confirm = input('Do you want to exit?: press "y" for yes press any key for no: ')
                if confirm.upper() != "Y":
                    # select_task = int(input("Enter 1 to register 2 to remove a course 3 to quit.: "))
                    continue
                print("Bye!")
                break

        print("Thank you for visiting us. You can also visit us at www//ourschool.com/")
    else:
        print("Your Id is not found. Please try again.")
elif selection1==1:
    reg_date = datetime.datetime.now()
    reg_year = str(reg_date.year)
    first_name = input("Enter your first name. ")
    middle_name = input("Enter your middle name. ")
    last_name = input("Enter your last name. ")
    birth_date = input("Enter your data of birth. ")
    generated_id = reg_year + first_name[0:2] + last_name[0:2]
    id_list.append(generated_id)
    created_user = last_name[0]+first_name[0]+middle_name
    print(f"user name is created for you. Your username is {created_user}. Please create your password.")
    autentication["user_name"] = created_user
    autentication["pass_word"] = input("Create your password. ")
    print(autentication)

    profile["first_name"]=first_name
    profile["last_name"]=last_name
    print(profile)
    print(id_list)
    print("Well come prospective student")
elif selection1==3:
    print("you have selected to quit.")
else:
    print("you have not made the right selection please try again.")
