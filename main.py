import yfinance as yf
import json
import pandas as pd

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
        data = {}
    return data
    
# class accountData():
#     def __init__ (self, name):
#         self.name = name

def buyStock(account):
    data = getData()
    cash = data[account]['Money']
    print(f'Cash on hand: {cash}')
    while(True):
        try:
            ticker = input("Enter the ticker of the stock you'd like to buy: ")
            ticker = ticker.upper()
            tickerDict = yf.Ticker(ticker)
            tickPrice = tickerDict.info["currentPrice"]
        except KeyError:
            print("This ticker is not recognizable.")
        else: break
    amt = int(input(f"How many {ticker} stocks would you like to buy: "))

    balance = data[account]['Money']
    if(tickPrice*amt) > balance:
        print(f"Your balance is too low. Ticker current price: {tickPrice} Current Balance: {balance}")
    else: 
        balance = balance - tickPrice*amt
        print(f"Bought {ticker} for {tickPrice*amt}. You now have {balance}.")
        data[account]['Money'] = balance
    try:
        data[account]['Stock'][ticker] += amt
    except KeyError:
        data[account]['Stock'][ticker] = 0
        data[account]['Stock'][ticker] += amt
    dumpData(data)
    
def checkStock(account):
    data = getData()
    for name, info in data.items():
        if name == account:
            print(f"For account: {name}")
            for k, v in info.items():
                if k == 'Money':
                    print(f"Cash on hand: {v}")
                if k == 'Stock': #use panda lib on this to display stock data?
                    df = pd.DataFrame(v, index = ['# of Stock'])
                    print('Current Stocks:'),
                    print(df)
                
def sellStock():
    return 1
def checkHistory():
    return 1

def dumpData(data):
   with open("data.json", "w") as f:
      json.dump(data, f, indent=4)

def checkPrice(*args): #show price for current ticker
    ticker = input("Enter the ticker you want to check to the current price for: ")
    ticInfo = yf.Ticker(ticker)
    curValue = ticInfo.info["currentPrice"]
    print(f"The current price of {ticker.capitalize} is {curValue}\n")

def loadAccount(*args): #load user account or create new accounts
    def accountName(data, name):
        for accName in data:
            if accName == name:
                return name
        data[name] = {}
        while(True):
            try:
                balance = int(input("How much money would you like to start this account with: "))
                data[name]['Money'] = balance
                data[name]['Stock'] = {}
                break
            except ValueError:
                print("Please enter a number.")
        return name

    #start here    
    data = getData()
    if data: #if data not empty
        print("Current lists of accounts: ")
        for name2 in data:
            print(f"{name2} ") #finish this, use "sep" or "end"?
        name = input("Enter your account name to log into your account or enter an unique name to create a new account: ")
        acc = accountName(data, name)
    else:
        name = input("You currently have no accounts. Enter an account name: ")
        acc = accountName(data, name)
    print(f"Current account is {name}")
    dumpData(data)
    return acc

def exit(*args): #quit program
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
        if function == 5:
            account = commandList[function][1](account)
        else:
            commandList[function][1](account)

menu()


#{bobyolo: {Netflix: { 294.2: 5}{295: 2}}{Snapchat: {482.2: 1}{384.4: 4}}}{bobdiverfsnied: {MSFT: {900: 439}}} 
#^ currently missing balance