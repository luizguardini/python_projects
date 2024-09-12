# Just for fun. Not safe for real implementation

import os
from cryptography.fernet import Fernet 
file_dir = os.path.dirname(os.path.realpath(__file__))

'''
def write_key():
    key = Fernet.generate_key()
    with open(file_dir + '/key.key', 'wb') as key_file:
        key_file.write(key)
write_key()       
'''

def load_key():
    file = open(file_dir + '/key.key', 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open(file_dir + '/passowords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print(f'User: {user} | password: {fer.decrypt(passw.encode()).decode()}')

def add():
    name = input('Account name: ')
    pwd = input('Password: ')
    with open(file_dir + '/passowords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input('Would you like to add a new password or view existing ones? (view, add). Press "q" to quit: ').lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode')