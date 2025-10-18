#Create a ATM Meachine


class ATM:

    def __init__(self):
        self.pin = ' '
        self.balance = 0


    def menu(self):
        user_input = input("""
            1. Enter your set Pincode.
            2. Enter your Diposit Amount.
            3. Enter your withdraw Amount.
            4. Enter your Check balance.
            5. Enter Exits Button.
            
            Your Choise: """)
        

        if user_input == '1':
            self.set_pin()
        elif user_input == '2':
            self.user_diposit()
        elif user_input == '3':
            self.user_withdraw()
        elif user_input == '4':
            self.user_check_balance()
        else:
            print("you exits")
        self.menu()
        

    def set_pin(self):
        self.pin = input("Create a New Pincode: ")
        print(self.pin)
        print("print create successful")

    def user_diposit(self):
        user_create_pin = input("enter your create pin: ")
        if user_create_pin == self.pin:
            user_deposit_amount = int(input("enter your amount: "))
            self.balance += user_deposit_amount
            print("deposit successfully")
        else:
            print("invild Pin! try again")

    def user_withdraw(self):
        user_create_pin = input("enter your create pin: ")
        if user_create_pin == self.pin:
            withdraw_amount = int(input("Enter your withdraw amount: "))
            if withdraw_amount <= self.balance:
                self.balance -= withdraw_amount
                print("Your Balance withdraw Successful")
            else:
                print("Ops Sorry! Insuffitient balance.")
        else:
            print("Yor pin the wrong! Please try again")

    def user_check_balance(self):
        user_create_pin = input("enter your create pin: ")
        if user_create_pin == self.pin:
            return self.balance
        else:  
            print("wrong pincode! try now")


atm = ATM() 
atm.menu()