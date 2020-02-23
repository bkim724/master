#login System Project

#imports
import pickle
from datetime import datetime
import clear_log

#global variables imported from pickle files
global user_dict
user_dict = pickle.load(open('user_dict.p','rb'))
global log
log = pickle.load(open('log.p','rb'))

def login():
    print('-----LOGIN PAGE-----'.center(50,'-'),'\n')
    global username
    username = input('Username: ').strip()
    pw = input('Password: ').strip()
    attempts = 5
    while auth(username, pw) == False:
        print('Invalid username/password\n')
        print(f'You have {attempts} attempts remaining.\n')
        username = input('Username: ').strip()
        attempts -= 1
        pw = input('Password: ').strip()
        if attempts == 0:
            print('You have run out of attempts.\nSystem shutting down')
            break 
    if auth(username,pw) == True:
        print('Login Successful\n')
        log.append(f'User {username} logged in')
        if username == 'admin':
            adminMenu()
        else:
            actionMenu()
def adminMenu():
    if username == 'admin':
        print('Administrator Action Menu'.center(50,'-'),'\n')
        action = input('Press N to create new user\nPress D to delete user\nPress S to view system status\nPress O to logout       ').upper()
        if action == 'N':
            addUser()
        elif action == 'D':
            deleteUser()
        elif action == 'S':
            status()
        elif action == 'O':
            logout()
        else:
            while action not in ['N','D','S','O']:
                if prompt == 'N':
                    addUser()
                    break
                elif prompt == 'D':
                    deleteUser()
                    break
                elif prompt == 'S':
                    status()
                    break
                elif prompt == 'O':
                    logout()
                    break
    print('\n')

def actionMenu():
    print('Action Menu'.center(50,'-'),'\n')
    action = input('Press U to update password\nPress D to delete your account\nPress O to logout       ').upper()
    if action == 'D':
        deleteAcc()
    elif action == 'U':
        updatepw()
    elif action == 'O':
        logout()
    else:
        while action not in ['U','O','D']:
            if prompt == 'D':
                deleteAcc()
                break
            elif prompt == 'U':
                updatepw()
                break
            elif prompt == 'O':
                logout()
                break
    print('\n')

def logout():
    print('You have logged out.\n')
    print('Would you like to go to the Welcome Page?')
    back = input('Press Y for yes\nPress N for no         ').upper()
    if back == 'Y':
        welcome()
    elif back == 'N':
        print('\nSystem shutting down\n')
    else:
        while back not in ['Y','N']:
            print('Unknown key entered...\n')
            back = input('Press Y for yes\nPress N for no         ').upper()
            if back == 'Y':
                print('Returning to the welcome page\n')
                welcome()
                break
            elif back == 'N':
                print('System shutting down\n')
                break

def addUser():
    print('Creating a New User'.center(50,'-'),'\n')
    username = input('Enter a username: ').strip()
    password = input('Enter a password: ').strip()
    if username in user_dict:
        while username in user_dict:
            print('Username already taken\n')
            username = input('Enter a username: ').strip()
            password = input('Enter a password: ').strip()
    user_dict[username] = password
    print(f'User {username} added to the system\n')
    log.append(f'Account for {username} created')
    returnToMenu()

def register():
    print('Register a New Account'.center(50,'-'),'\n')
    username = input('Enter a username: ').strip()
    password = input('Enter a password: ').strip()
    if username in user_dict:
        while username in user_dict:
            print('Username already taken\n')
            username = input('Enter a username: ').strip()
            password = input('Enter a password: ').strip()
    user_dict[username] = password
    print(f'User {username} added to the system\n')
    log.append(f'Account for {username} registered')
    print('Would you liked to login now?\n')
    gotologin = input('Press Y to login\nPress N to exit:      ').upper()
    if gotologin == 'Y':
        login()
    elif gotologin == 'N':
        print('\nSystem shutting down\n')
    if gotologin not in ['Y','N']:
        while gotologin not in ['Y','N']:
            print('Unknown key entered...\n')
            gotologin = input('Press Y to login\nPress N to exit:         ').upper()
            if gotologin == 'Y':
                login()
                break
            elif gotologin == 'N':
                print('System shutting down\n')
                break
       
def auth(user, pw):
    if user in user_dict and pw == user_dict[user]:
        return True
    else:
        return False
    
def deleteAcc():
    print('Deleting your Account'.center(50,'-'),'\n')
    user_dict.pop(username)
    print(f'User {username} removed from system\n')
    log.append(f'Account for {username} deleted')
    print('Would you like to go to the Welcome Page?')
    back = input('Press Y for yes\nPress N for no:         ').upper()
    if back == 'Y':
        welcome()
    elif back == 'N':
        print('\nSystem shutting down\n')
    else:
        while back not in ['Y','N']:
            print('Unknown key entered...\n')
            back = input('Press Y for yes\nPress N for no:         ').upper()
            if back == 'Y':
                print('Returning to the welcome page\n')
                welcome()
                break
            elif back == 'N':
                print('System shutting down\n')
                break

def deleteUser():
    print('Delete a user'.center(50,'-'),'\n')  
    user = input('Enter users username:      ')
    if user not in user_dict:
        while user not in user_dict:
            print('User not found.')
            user = input('Enter users username:      ')
    user_dict.pop(user)
    print(f'Account for {user} deleted.')
    log.append(f'Account for {user} deleted')
    returnToMenu()

def updatepw():
    print('Update Password'.center(50,'-'),'\n')
    user_dict[username] = input('Enter a new password:  ').strip()
    print(f'Password for {username} updated\n')
    log.append(f'Password for {username} updated')
    returnToMenu()
    
def returnToMenu():
    print('Would you like to return to the menu?\n')
    back = input('Press Y for yes\nPress N for no         ').upper()
    if back == 'Y':
        if username == 'admin':
            adminMenu()
        else:
            actionMenu()
    elif back == 'N':
        print('\nSystem shutting down\n')
    else:
        while back not in ['Y','N']:
            print('Unknown key entered...\n')
            back = input('Press Y for yes\nPress N for no         ').upper()
            if back == 'Y':
                print('Returning to the menu\n')
                if username == 'admin':
                    adminMenu()
                else:
                    actionMenu()
                break
            elif back == 'N':
                print('System shutting down\n')
                break

def status():
    print('System Status'.center(50,'-'),'\n')
    print('User Count: ', len(user_dict),'Log Count: ',len(log),'\n')
    print('User List'.center(50,'-'),'\n')
    for i in user_dict:
        print(f'{i}\n')
    print('System Log'.center(50,'-'),'\n')
    for i in log:
        print(f'{i} at {datetime.now()}\n')
    returnToMenu()

def welcome():
    print('='*50)
    print('Welcome to BK Systems!'.center(50,'='))
    print('='*50)
    welc = input('Press L to Login\nPress R to Register      ').upper()
    if welc == 'L':
        login()
    elif welc == 'R':
        register()
    else:
        while welc not in ['R','L']:
            print('Unknown key entered...\n')
            welc = input('Press L to Login\nPress R to Register      ').upper()
            if welc == 'L':
                login()
                break
            elif welc == 'R':
                register()
                break

def execute():
    welcome()
    pickle.dump(user_dict,open('user_dict.p','wb'))
    pickle.dump(log,open('log.p','wb'))

execute()