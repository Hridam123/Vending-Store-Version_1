REFERENCE={"P":"Pennies", "N":"Nickels", "D":"Dimes", "Q": "Quarters", "M": "Dollars"}
COIN_VALUE= {"Pennies": 1, "Nickels":5, "Dimes":10, "Quarters":25, "Dollars":100}
#Constants for storing value of coins which can be referred as per user input
class MoneyCalculator():

    def __init__(self, inventory_handle):
        self.money_entered=0#Records the total sum of money entered during transaction
        self.total_balance=0
        self.rem_balance=0#Stores pre-paid balance after use of service
        self.total_money_input=0#Records the total sum of money entered during transaction
        self.item=False
        self.next_coins=True
        self.inventory_handler=inventory_handle



    def pay_stuff(self,product:str,number_of_items:int):
        """
        Takes in user input and calls the relevant payment method

        Arguments:
            product(str): The name of the item requested by the user
            number_of_items(int): Quantity of product(item) requested by the user

        Note:
            If the user wishes to exit the transaction the method terminates early .

        Returns:
              (boolean) False, when the transaction is stopped midway

        """
        while True:#Loops until appropriate user input is entered so that code won't hit an error
            payment_options= input("How would you like to pay?\n"
                                   "Press A for Cash or Press B for coins: ").title()
            print("\n"*2)
            if payment_options=="A" or payment_options=="B":
                break
            elif payment_options=="Exit":
                return False
            else:
                print("Invalid Method. Choose again.")

        if payment_options=="A":
            return self.pay_cash(product,number_of_items)
        # Returns False if transaction is cut off midway in the method called
        elif payment_options=="B":
            return self.pay_coins(product,"general",number_of_items)
        # Returns False if transaction is cut off midway in the method called



    def pay_coins(self, product:str, transaction:str,number_of_items:int):
        """
        Takes in user's coin input and initiates product purchase for standard purchase.
        Takes in user's coin input and tops up user balance for pre-paid purchase

        Arguments:
            product(str): The name of the item requested by the user
            transaction(str): The type of transaction being carried out 'pre-paid'(balance) or 'post-paid'
            number_of_items(int): Quantity of product(item) requested by the user

        Returns:
            -(boolean)False if transaction is stopped midway
            -self.money_entered to add money into the balance( pre-paid service)

        Note:
            This method has two major roles based on the transaction type.
            -For Post-Paid transaction this method stores the money inserted by the user to
                proceed purchase
            -For Pre-Paid transaction( balance) this method tops up which adds on the balance
                entered previously
        """
        other_coins= self.next_coins

        while other_coins:#Loops until user inputs all the coins that they want

            while True:#Loops until correct value is assigned, so that code won't hit an error
                enter_coins=input(" Enter the coins:\n"
                                    "Press P for Pennies\n"
                                    "Press N for Nickles\n"
                                    "Press D for Dimes\n"
                                    "Press Q for Quarter\n"
                                    "Press M for Dollar\n" )

                if enter_coins in REFERENCE:
                    money_options = REFERENCE[enter_coins]
                    break
                else:
                    print("\n"*2)
                    print("That's not a valid input.")

            while True:
                number_of_coins= (input(f"How many {money_options} coins: "))
                print("\n"*2)

                if number_of_coins=="Exit":
                    print("Transaction Cancelled. Returning your money...")
                    change_in_cents = int(round(self.money_entered * 100))#Money converted in cents to ensure proper calculation
                    self.greedy_change(change_in_cents)
                    self.money_entered=0#Refreshes the total money entered to 0 after money is refunded
                    return False

                try:
                    count=int(number_of_coins)
                    money_entered= COIN_VALUE[money_options]*count
                    amount= money_entered/100
                    self.money_entered+= amount
                    #"self.money_entered" tracks down user balance as per money input and products purchased
                    self.total_money_input+=amount
                    break
                except ValueError:
                    print("Invalid value. Please enter a whole number (e.g., 5)")

            another=input("If you want to insert any other coin. Press 'Y' :").upper()
            print("\n")

            if another=="Y":
                pass
            else:
                other_coins=False

        if transaction=="general":
            self.money_manage(product, "coins",number_of_items)
        elif transaction=="balance":
            return self.money_entered



    def pay_cash(self, product:str, number_of_items:int):
        """
        Takes in user's cash input and initiates product purchase for standard purchase.
        Takes in user's cash input and tops up user balance for pre-paid purchase


        Arguments:
            product(str): The name of the item requested by the user
            number_of_items(int): Quantity of product(item) requested by the user

        Returns:
            Returns:
            -(boolean)False if transaction is stopped midway

        Note:
            This method is be used both for top-up of pre-paid service and payment for
            post-paid service.
        """
        while True:
            incoming_cash=input("Enter the bill: $")
            print("\n")
            if incoming_cash=="Exit":
                return

            try:
                cash_input= int(incoming_cash)
                break
            except ValueError:
                print("Invalid Value. Please enter a whole number or exit")

        self.money_entered+= cash_input
        self.total_money_input+= cash_input
        self.money_manage(product, "cash",number_of_items)


    def money_manage(self,item:str,t_type:str,number_of_items:int):
        """
            Handles the core transaction logic and fund distribution.

            Arguments:
                item(str): The name of the product
                t_type(str): The type of transaction being carried out 'pre-paid'(balance) or 'post-paid'
                number_of_items(int): Quantity of product(item) requested by the user

            Notes:
                It evaluates if the supplied fund( user-entered funds) meet the calculated cost. If the
            user input is greater than the price of product, it triggers item delivery, calculates
            change and resets specific money trackers to 0. Otherwise, if user input is less than
            price of product, it recursively prompts for additional payment based on transaction type.

            Returns:
                (float) The remaining balance or current amount entered based on success of transaction
        """
        if self.money_entered>=self.amount_calculate(item,number_of_items):
            residual_amount=self.money_entered-(self.amount_calculate(item,number_of_items))
            print("Item delivered")
            change_in_cents= int(round(residual_amount*100))

            if t_type=="balance":
                print(f"Your remaining balance is {round(residual_amount,2)}")
                print("\n"*2)
            else:
                self.greedy_change(change_in_cents)
                print(f"Total change: {round(residual_amount,2)}")
                print("\n"*2)
            self.rem_balance=residual_amount
            self.item=True
            self.money_entered = 0
            return residual_amount#Returns the change amount after successful transaction

        else:
            print(f"Your current balance of {self.money_entered} is not sufficient.")
            print("\n"*2)

            if t_type=="cash":
                self.pay_cash(item,number_of_items)
                # Recursive prompt for more cash
            elif t_type=="coins":
                self.pay_coins(item, "general",number_of_items)
                # Recursive prompt for more coins
            else:
                return self.money_entered# Returns the total money after failed transaction


    def amount_calculate(self, item:str,number_of_items:int):
        """
        Extracts and returns the price for the product purchased

        Arguments:
            item(str): The name of the product to be purchased.
            number_of_items(int):  Quantity of product(item) requested by the user

        Returns:
            (float) Total price for a given amount of product
            purchased

        """
        item_data= self.inventory_handler.storage[self.inventory_handler.storage.index==item]
        item_price= item_data.Price.item()
        return item_price*number_of_items

    def balance(self,number_of_items:int):
        """
        Facilitates the top-up process for the user's pre-paid balance.

        Arguments:
            number_of_items(int): The quantity of products purchased( It is passed through
            all payment methods for consistency)

        Note: This method updates total_balance attribute as per increase in pre-paid balance.
        """

        self.money_entered=0
        while True:
            balance_options= input("Press C  to proceed with coins and M to proceed with cash: ").upper()
            print("\n"*2)
            if balance_options=="C" or balance_options=="M":
                break
            else:
                print("Invalid Input. Try again")

        if balance_options=="C":
            self.total_balance+=self.pay_coins("No_item", "balance", number_of_items)
        elif balance_options=="M":

            while True:

                try:
                    new_bill = int(input("Enter the bill: $"))
                    print("\n")
                    self.total_balance+=new_bill
                    self.total_money_input+=new_bill
                    break
                except ValueError:
                    print("\n")
                    print("Invalid Value. Please re-enter the data!.")


    def purchase(self, item:str,number_of_items:int):
        """
        Manages the transaction flow for pre-paid(balance-based) purchases.

        Arguments:
            item(str): The name of the product to be purchased.
            number_of_items(int):  Quantity of product(item) requested by the user

        Notes:
            This method stores balance for a particular session and passes it to initiate
            the purchase. If the existing balance is insufficient for the purchase, then it
            also prompts user to add more funds before the purchase.

        """
        while self.item==False:
            self.money_entered=self.total_balance
            remaining_balance=self.money_manage(item, "balance",number_of_items)

            if remaining_balance==self.total_balance:
                #Checks for insufficient balance by comparing if remaining balance is same as current balance
                print("Amount In sufficient. Enter more money to proceed: ")
                print("\n"*2)
                self.balance(number_of_items)

            if self.item==True:
                self.total_balance=remaining_balance
                #Stores remaining balance after purchase as the total balance left wich can be used


    def greedy_change(self, change_in_cents:int):
        """
        Implements a greedy algorithm to dispense the minimum number of coins.

        Arguments:
            change_in_cents(int):The remaining balance converted to an integer
            (number of cents-formed by multiplying dollar value with 100) to avoid floating
            point errors

        """
        print("Here is your change")

        for key, value in reversed(COIN_VALUE.items()):
            #Takes value from the last stored constant as the cents should be divided from highest coin value to lowest
            coins= int(change_in_cents//value)
            change_in_cents%=value

            if coins>0:
                print(f"{coins} {key}")











