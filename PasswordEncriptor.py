from cryptography.fernet import Fernet

sup=input("What´s up")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User: ", user)
            print ("Password: ", password) 


def add():
    name=input("Account name: ")
    passwrd=input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + passwrd + "\n")




while True:
    mode=input("If you want to view the accounts, type view, if you want to add a new account, type add, if you want to quit press q. ")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Please type a valid mode.")




