import yfinance as yf

msft = yf.Ticker("MSFT")
# for key, value in msft.info.items():
#     print(key)
print(msft.info["currentPrice"])
#hist = msft.history(period="max")
#print(hist)

def checkPrice():
    return 1
def buyStock():
    return 1
def checkStock():
    return 1
def sellStock():
    return 1
def checkHistory():
    return 1
def loadAccount():
    print("Current lists of accounts: ")
    #write code that display list of account here
    print("Enter your account name to log into your account or enter an unique name to create a new account.")
def exit():
    return 1

def menu():
    loadAccount()
    "Enter a number that correspond with what you wish to do."
    commandList = [["Find more information about a ticker", checkPrice], ["Buy some stock", buyStock], ["Check your current stocks", checkStock],
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