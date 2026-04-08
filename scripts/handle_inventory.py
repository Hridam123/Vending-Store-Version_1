import pandas as pd
from datetime import datetime


class Handling:

    def __init__(self):
        self.storage=pd.read_csv("total_supp.csv",index_col="Supplies")
        self.total_sales=pd.read_csv("all_sales.csv",index_col="Serial_No")
        self.serial_number=self.total_sales.Supplies.count()#Generates unique serial number by using existing data
        self.receipt_number=0
        self.current_items_purchased=[]#Records every item purchased in real-time


    def in_stock(self, item:str, number_of_items:int):
        """
        Checks if certain amount of a product is available

        Arguments:
            item(str): The name of the product
            number_of_items(int): Quantity of product(item) requested by the user
        Returns:
            (boolean) True if stock is sufficient, and False if otherwise

        """
        data_of_item= self.storage.loc[item]

        if data_of_item.Pieces_available.iloc[0]>=number_of_items:
            return True

        return False


    def change_inventory(self, item:str, number_of_items:int):

        """
        Reduces the stock of available items when certain product is purchased

        Arguments:
            item(str): The name of the product
            number_of_items(int): Quantity of product(item) requested by the user

        """
        self.storage.at[item, "Pieces_available"] -= number_of_items
        self.storage.to_csv("total_supp.csv")


    def new_item(self, item:str, piece:int, price:float):
        """
        Stores new item in Inventory as per product data provided

        Arguments:
            item(str): The name of the product to be added
            piece(int): The number of product(item) added
            price(float): The price of product(item) added
        """
        self.storage.loc[item] = {
            "Pieces_available": piece,
            "Price": price,
        }

        self.storage.to_csv("total_supp.csv")


    def manage_sales(self, item:str, number_of_items:int):
        """
        Takes input for products sold and records it in CSV

        Arguments:
            item(str): The name of the product
            number_of_items(int): Quantity of product(item) requested by the user

        Note:
             This sales method updates everytime a user completes transaction for an item
        """
        current_time= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        price_of_item= self.storage.loc[item].Price.iloc[0]
        self.receipt_print(item, number_of_items, price_of_item, current_time)

        self.total_sales.loc[self.serial_number+1]={#Stores product data based on unique chronological serial number
            "Supplies": item,
            "Price":price_of_item,
            "Date____Time": current_time,
            "Quantity":number_of_items,
            "Total_Price": (round(price_of_item * number_of_items, 2))
        }

        self.total_sales.to_csv("all_sales.csv")
        self.serial_number+=1 #Increases serial number to ensure that each product gets unique number


    def receipt_print(self,item:str, number_of_items:int, price_of_item:float, current_time):
        """
        Stores real-time purchase data for receipt

        Arguments:
            item(str): The name of the product
            number_of_items(int): Quantity of product(item) requested by the user
            price_of_item(float): The price of the product(item) purchased.
            current_time: The time at which product was purchased

        """
        self.current_items_purchased.append({# Adds product data, forming list of each product sold during a purchase
            "Supplies": item,
            "Price": price_of_item,
            "Date____Time": current_time,
            "Quantity": number_of_items,
            "Total_Price": (price_of_item * number_of_items)
        })

