import yfinance as yf
import json

#msft = yf.Ticker("MSFT")
# for key, value in msft.info.items():
#     print(key)
#print(msft.info["currentPrice"])
#hist = msft.history(period="max")
#print(hist)

def getData():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        data = {'no': 'test', 'yes': 'test2'}
    return data
class accountData():
    def __init__ (self, name, balance, stock = ''):
        self.name = name
        self.bal = balance
        self.stock = stock

def dumpData(data):
   with open("data.json", "w") as f:
      json.dump(data, f, indent=4)
def checkPrice(): #show price for current ticker
    ticker = input("Enter the ticker you want to check to the current price for: ")
    ticInfo = yf.Ticker(ticker)
    curValue = ticInfo.info["currentPrice"]
    print(f"The current price of {ticker.capitalize} is {curValue}\n")

def buyStock():
    return 1
def checkStock():
    return 1
def sellStock():
    return 1
def checkHistory():
    return 1

def loadAccount(): #load user account or create new accounts
    def accountName(data, name):
        for accName, data in data.items():
            if accName == name:
                return accountData(name, data['Money'], data['Stock'])
        data[name] = {}
        while(True):
            try:
                balance = int(input("How much money would you like to start this account with: "))
                data[name]['Money'] = balance
                break
            except ValueError:
                print("Please enter a number.")
        return accountData(name, data[name]['Money'])

    #start here    
    data = getData()
    if data:
        print("Current lists of accounts: ")
        for name2 in data:
            print(f"{name2} ") #finish this, use "sep" or "end"?
        name = input("Enter your account name to log into your account or enter an unique name to create a new account: ")
        acc = accountName(data, name)
    else:
        name = input("You currently have no accounts. Enter an account name: ")
        acc = accountName(data, name)
    print(f"Current account is {acc.name}")
    dumpData(data)
    return acc

def exit(): #quit program
    return 1

def menu(): #ui 
    account = loadAccount()
    print("Enter a number that correspond with what you wish to do.")
    commandList = [["Check a ticker current price", checkPrice], ["Buy some stock", buyStock], ["Check your current stocks", checkStock],
                ["Sell stock", sellStock],
                ["Check account history", checkHistory],
                ["Start a new or load an account", loadAccount], ["Exit program", exit]]             
    function = 0
    while function != len(commandList)-1:
        for i in range(0,len(commandList)): 
            print(i+1, commandList[i][0])
        function= int(input())-1
        commandList[function][1]()

menu()


#{bobyolo: {Netflix: { 294.2: 5}{295: 2}}{Snapchat: {482.2: 1}{384.4: 4}}}{bobdiverfsnied: {MSFT: {900: 439}}} 
#^ currently missing balance