
class BankAccount:
    def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
        
        self.first_name= first_name
        self.last_name= last_name
        self.account_id= account_id
        self.account_type= account_type
        self.pin= pin
        self.balance= balance
        
        
    def deposit(self):
        money_added = int(input("Enter the amount to be deposited: "))
        self.balance = money_added+ self.balance
        print('Money deposited successfully!\n New balance is- ', self.balance, "$")
        
    def withdraw(self):
        withdraw_amt= int(input("Enter amount you want to withdraw- "))   
        new_balance= self.balance - withdraw_amt
        if new_balance< 0:
            print("Insufficient balance to withdraw funds. Broke?")
        else:
            self.balance= new_balance
            print("Money withdrawn successfully\n Withdrawn amount- ", withdraw_amt,"$")
        
    def display_balance(self):
        print("Your current balance is- ", self.balance,'$')
        
druv= BankAccount('Druv','Bruv', 45872,'Savings', 5544, 0)   

druv.deposit()
druv.withdraw()
druv.display_balance()


 
        
        
                    
        
    
    
    
    
