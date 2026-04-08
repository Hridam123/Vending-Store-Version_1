import pandas as pd
from money_manager import MoneyCalculator
from handle_inventory import Handling
from inventory import StoreInventor

store_inventory=StoreInventor()
handling=Handling()
money=MoneyCalculator(handling)

WIDTH=60

def receipt():
    """
    Generates and prints out the transaction receipt into the console by aggregating data for
    purchased items from 'Handling' module

    Note:
        If the user's payment is insufficient or transaction is cut out mid-way, the function
        terminates early before returning

    """

    all_items_purchased = handling.current_items_purchased
    current_items_purchased = pd.DataFrame(all_items_purchased)
    total_shopping = current_items_purchased.Total_Price.sum()#Aggregates total Transaction value from a single session
    user_money = money.total_money_input
    cash_out = user_money-total_shopping
    if user_money<total_shopping:#Returns function if no purchase completed
        return False
    print("\n"*2)
    print("\n" + "=" * WIDTH)
    print("      OFFICIAL RECEIPT      ")
    print("=" * WIDTH)
    print(current_items_purchased.to_string(index=False))
    print("=" * WIDTH)
    print(" "*(WIDTH-10)+f"Total_Price: ${total_shopping:.2f}")# Round to 2 decimal places to handle floating-point arithmetic errors in currency
    print(" "*(WIDTH-10)+f"User_Pay   : ${user_money:.2f}")
    print(" "*(WIDTH-10)+f"Change     : ${cash_out:.2f}")
    print("=" * WIDTH)
    print("   Thank you for shopping!  ")



def main():
    user_choice=""

    balance=input("If you want to add balance then buy press P, else press any other key: ").upper()

    print("\n"*2)

    if balance=="P":
        money.balance(0)

    while user_choice!="Exit":

        items = handling.storage.index
        list_of_items = items.to_list()

        print(handling.storage)
        print("\n")
        user_choice = input("What would you like to purchase (Type 'Exit' to quit the machine): ").title()

        if user_choice in list_of_items:#Checks for required items in the inventory

            while True:

                try:
                    number_of_items = int(input(f"How many {user_choice} would you like to purchase?: "))
                    print("\n"*2)
                    break
                except ValueError:#Loops back until a valid integer value is assigned
                    print(f"Please enter an integer value. Example: If you require two {user_choice} press 2")#Error Message

            money.item=False #Assigns value money.item=False to identify that hasn't been processed

            if handling.in_stock(user_choice, number_of_items):
                # Ensures that inventory can satisfy the request before initiating payment
                if balance=="P":
                    paid=money.purchase(user_choice,number_of_items)
                else:
                    paid=money.pay_stuff(user_choice,number_of_items)
                if paid==False:
                    break
                handling.change_inventory(user_choice, number_of_items)#Reduces products from the Inventory based on Product data
                handling.manage_sales(user_choice, number_of_items)

            else:
                print("Not enough Items.")

        elif user_choice=="Reset":#Secret service for admin, RESETS the supplies
            store_inventory.store_supply()
            break

        elif user_choice=="Add Item":#Secret service for admin, ADDS an item

            name_of_item=input("What is the item being added?: ")

            while True:#Loops until correct datatype is assigned

                try:
                    quantity= int(input("How many item are being added?: "))
                    price=float(input("Enter the price for the item: "))
                    print("\n"*2)
                    break
                except ValueError:
                    print("One of the two values you entered were invalid please type again")

            handling.new_item(name_of_item, quantity, price)

        elif user_choice=="Exit":
            if handling.current_items_purchased:
                receipt()
            else:
                print("No item Purchased")

            break

        elif user_choice=="Sales":
            store_inventory.sales_data()
            #Resets the sales data
            break

        else:
            print("No such items available. Please check your syntax")


if __name__=="__main__":
    main()#Promotes modules reusability
