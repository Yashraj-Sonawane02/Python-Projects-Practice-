# password manager (encryption - description)
from cryptography.fernet import Fernet 

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key" , "wb") as key_file:
        key_file.write(key)
write_key()'''


def load_key():
    file = open("key.key" , "rb")
    key = file.readline()
    file.close()
    return key


def add():    
    name = input("Enter an account name : ")
    pwd = input("Enter a password : ")
    with open("password.txt" , "a") as file:
        file.write(name + "|"+ fer.encrypt(pwd.encode()).decode() + "\n")


def view():
    with open("password.txt" , "r") as file:
        for line in file.readlines() : 
            temp_a , temp_b = line.rstrip().split("|")
            print("user:",temp_a ,"| password :", fer.decrypt(temp_b.encode()).decode())


master_pwd = input("What is the Master Password ? : ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


while True  : 
    choice = input("Would you like to add new password or view existing once (add / view) or q to quit? ").lower()
    if choice == 'q' : 
        break

    if choice == "add" : 
        add()
    elif choice == "view" : 
        view()
    else :
        continue


#stored passwordss
#Facebook_account|gAAAAABn0dwzW9Bp-K9gHr2smlWSl6_oPzlvVxW4Bhixp0eVNid17ElOUyFkPgp8BVjrxaOIHe7V22iwPaWUgS9R--az33Uuuw==
#Gaurav_Goat|gAAAAABn0dxRjcuz0Dpv5FrAhEdiBZTvw2ZZd5WJCJE2pT2161uaTJyGg5FJyeYVAxn-s8ReTev2Uu3R_FViZz1g2RQ6WeWQGA==


#key generated using fernet
#FE5ueKNzJo_ZYGopgSpxG-pSc0Yh2mAZIH-a6qYInH8=
