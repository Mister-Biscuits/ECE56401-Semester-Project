import getpass
from argon2 import PasswordHasher as ph

"""
Prompt user for username and password securely

returns: 
    (Username, Argon2(password||salt))
"""
def get_credentials():
    print("==== Computer Security Project 56401 Log In ====")
    
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")
    print(type(password))
    #Add request for salt from server 

    #hash = ph.hash(ph,password)
    #Validate hash is done correctly and securely
    #ph.verify(password, hash)
    #ph.check_needs_rehash(hash)

    return username, password

def login():
    #nothing yet
    return 0


#if __name__ == "__main__":
    #main()