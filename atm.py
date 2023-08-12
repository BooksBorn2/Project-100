class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
    def check_balance(self):
        print("Your balance is $356.09")
    def withdraw_cash(self):
        print("Withdrawing....")
    
x = Atm("2003475924", "1457")