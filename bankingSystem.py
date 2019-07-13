import getpass
import datetime

def printBalance(username):
    print(str(userBalance[username]))

def transferMoney(username):
    to = input("Transfer to:")
    if to in users:
        money = int(input("Money:"))
        if userBalance[username] < money:
        	print("Sorry:You havn't enought money in your bank account\n")
        else:
            userBalance[username] -= money
            userBalance[to] += money
    else:
        print("Entered incorrect username")

def transferMoneyAdmin():
    user1 = input("From:")
    user2 = input("To:")
    if user1 in users and user2 in users:
        money = int(input("How much:"))
        if userBalance[user1] < money:
            print("Sorry:There aren't enought money in that bank account\n")
        else:
            userBalance[user1] -= money
            userBalance[user2] += money
    else:
        print("Entered incorrect username")
    
def cashOut(username):
    money = int(input("How much cash out:"))
    if money > userBalance[username]:
        print("Sorry:You havn't enought money in your bank account\n")
    else:
        userBalance[username] -= money

def cashOutAdmin():
    user = input("user:")
    if user in users:
        money = int(input("How much"))
        if userBalance[user] > money:
            print("Sorry:There aren't enought money in that bank account\n")
        else:
            userBalance[user] -= money
    else:
        print("entered incorrect username")

def logOut():
    mainProgram()

def createUser():
    username = input("enter username:")
    if username in users:
        print("username already exists")
    else:
        password = getpass.getpass(prompt='Password:')
        balance = int(input("enter balance:"))
        users[username] = password
        userBalance[username] = balance

def deleteUser():
    username = input("enter username:")
    if username in users:
        users.pop(username)
        userBalance.pop(username)
    else:
        print("Entered incorrect username")

def getInfo():
    username = input("enter username:")
    if username in users:
        print(username + " balance is " + str(userBalance[username]))
    else:
        print("Entered incorrect username")

def selectUserOptions(username):
    option = int(input("\n\n\ninsert option number\n"
    	               "1____Watch balance\n"
    	               "2____Transfer Money\n"
    	               "3____Cash Out\n"
    	               "4____Log Out\n"))
    while option != 4:
        if option == 1:
            print(printBalance(username));
        elif option == 2:
            transferMoney(username); 
        elif option == 3:
            cashOut(username)
        else:
            print("Entered incorrect option")
        option = int(input("\n\n\ninsert option number\n"
    	               "1____Watch balance\n"
    	               "2____Transfer Money\n"
    	               "3____Cash Out\n"
    	               "4____Log Out\n"))
    if option == 4:
        logOut()


def selectAdminOptions():
    option = int(input("\n\n\ninsert option number\n"
    	               "1____Create User\n"
    	               "2____Delete User\n"
    	               "3____Take info about User\n"
    	               "4____Transfer Money\n"
    	               "5____Cash Out\n"
    	               "6____Log Out\n"))
    while option != 6:
        if option == 1:
            createUser();
        elif option == 2:
            deleteUser(); 
        elif option == 3:
            getInfo();
        elif option == 4:
            transferMoneyAdmin()
        elif option == 5:
            cashOut()
        else:
            print("Entered incorrect option")
        option = int(input("\n\n\ninsert option number\n"
    	               "1____Create User\n"
    	               "2____Delete User\n"
    	               "3____Take info about User\n"
    	               "4____Transfer Money\n"
    	               "5____Cash Out\n"
    	               "6____Log Out\n"))
    if option == 6:
        logOut()


def mainProgram():
    modeWindow = True;
    while modeWindow == True:
        mod = input("Mode user or admin:");
        if mod != "user" and mod != "admin":
            print("Error: Entered incorrect mod");
        else:
            print("\nLog in " + mod)
            loged = False
            modeWindow = False
            tryingCount = 1;
            while loged == False and tryingCount <= 3:
                username = input("username:")
                password = getpass.getpass(prompt='Password:')
                if mod == "user":
                    if username in users and users[username] == password:
                        loginDic[username] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        loged = True
                    else:
                        tryingCount += 1
                        print("entered incorrect user or password")
                else:
                    if username in admin and admin[username] == password:
                        loginDic[username] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        loged = True
                    else:
            	        tryingCount += 1
            	        print("entered incorrect user or password")
            if loged == False:
                modeWindow = True

    if modeWindow == False and loged == True:
        if mod == "user":
            selectUserOptions(username)
        else:
            selectAdminOptions()

users = {"Lilit":"12a3", "Anna":"13456ga", "Ani":"pay111"}
admin = {"Alina":"900qa"}
userBalance = {"Lilit":1000, "Anna":1000, "Ani":2000}
loginDic = {}

mainProgram()