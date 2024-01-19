from cryptography.fernet import Fernet
import os

USER_DATA = 'D:/Desktop/Projects/Pyt_proj/projects_2023/crypto_key/user_data.txt'
MAST_KEY = 'D:/Desktop/Projects/Pyt_proj/projects_2023/crypto_key/master_pass.txt'
OLD_KEY = 'D:/Desktop/Projects/Pyt_proj/projects_2023/crypto_key/old_key.txt'
keys = {"old":"", "new": ""}
keys["new"] = Fernet.generate_key()
print_key = keys['new'].decode("ASCII")
f = Fernet(keys['new'])


def decrypted():
    with open(OLD_KEY, 'r') as key_file: 
        data_key = key_file.read()
        keys['old'] = data_key.encode() 
        fer = Fernet(keys['old'])

    with open(USER_DATA, 'r+') as data_file:
        
        i = 0
        for line in data_file.readlines():
            while i < 1:
                data_file.truncate(0)
                data_file.seek(0)
                i += 1
                break
            new_data = fer.decrypt(line).decode()
            data_file.write(new_data + '\n')       
   
            
        
def encrypted(): 
    with open(USER_DATA, 'r') as data_file:
        write_new_data = data_file.read()
        token2 = f.encrypt(write_new_data.encode())

    with open(USER_DATA, 'wb') as write_file:
        write_file.write(token2 + b'\n')


def add_data():
    message = input("enter data: ")
    token = f.encrypt(message.encode())
    with open(USER_DATA, 'ab') as data_file: 
        data_file.write(token + b"\n")

def read_data():
    
    with open(USER_DATA, 'r') as user_file:
        for line in user_file:
            print(f.decrypt(line).decode().strip())




def assign_pass():
   keys["old"] = print_key
   with open(OLD_KEY, 'w') as key_file:
       key_file.write(keys["old"])

def is_file_empty(file_path):
        return os.path.getsize(file_path) == 0




if is_file_empty(USER_DATA):
        print("The file is empty.")
else:
    decrypted()
    encrypted()
        
    
while True:
    
    with open(MAST_KEY, 'w') as key_file:
        key_file.write(print_key)

    master_pass = input('enter your master pass / or enter "Q" to quit: \n')
    if master_pass == print_key:
        print("\nChoose an option:")
        print("1. Add data")
        print("2. View data")
        print("3. Clear DATA")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_data()
        elif choice == "2":
            if is_file_empty(USER_DATA):
                print("The file is empty.")
                continue
            read_data()
        elif choice == "3":
            with open(USER_DATA, 'w') as file:
                pass
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
    elif master_pass.lower() == "q":
        print("Finishing the program")
        break
    else:
        print("invalid key. Please Try again")
    
    assign_pass()



