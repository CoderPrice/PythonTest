#import regex library
import re

def login():
    #Input field  login
    print("Fill the Login:")    
    name = input()

    #Input field password
    print("Fill the Password:")
    password = input()

    #Open saved file
    databaseLogin = open('databaselogin.txt')
    databaseList = databaseLogin.read()

    #Verify if exist login and password
    databaseregex = re.compile('Name:'+name+' Password:'+password)
    mo = databaseregex.search(databaseList)

    #Repeat login field while is not exist login and/or password
    while(mo == None):
        #incorrect login and/or password
        print("Incorrect login and/or password")
        
        #Input field  login
        print("Fill the Login:")    
        name = input()
        
        #Input field password
        print("Fill the Password:")
        password = input()

        #Verify if exist login and password
        databaseregex = re.compile('Name:'+name+' Password:'+password)
        mo = databaseregex.search(databaseList)

    #Logged
    print("Hello " + name)

    #close saved file
    databaseLogin.close();

    #Back to menu
    menu()


def register():
    #Login field
    print("Fill the Login:")
    name = input()

    #while Login field if empty
    while(name == ""):
        #Login field
        print("Fill the Login:")
        name = input()

    #password field
    print("Fill the Password:")
    password = input()

    #while password field if empty
    while(password == ""):
        #password field
        print("Fill the Password:")
        password = input()

    #Open to save register in file
    databaseLogin = open('databaselogin.txt','a')
    databaseLogin.write('Name:'+name+' Password:'+password+'\n')
    databaseLogin.close();

    #Registered
    print("Welcome "+name)

    #Back to menu
    menu()


def menu():
    #Select to login or register
    print("Select actions:")
    print("1 - Login \n2 - register")
    actionID = input()

    #verify the choice
    if(actionID == "1"):
        login()
    if(actionID == "2"):
        register()

#call menu
menu()
