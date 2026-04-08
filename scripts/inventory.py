import pandas as pd

class StoreInventor:

    def __init__(self):
        self.Inventory={
            "Supplies":["Chips", "Sandwich", "Bread", "Burger", "Coffee", "Juice"],
            "Pieces_available":[10,10,10,10,10,10],
            "Price":[2.46, 3.01, 3.26, 3.38, 3.40, 3.57]
        }

        self.sales={"Serial_No":[],"Supplies":[], "Price":[], "Quantity":[], "Date____Time":[], "Total_Price":[]}
        #Creates dictionary with empty lists where real-times sales data are stored

    def store_supply(self):
        """
        Takes in Inventory data to output it into CSV file
        Note:
            This method only runs at the start of creation of program or
            when the products are restocked
        """
        df_supplies=pd.DataFrame(self.Inventory)
        df_supplies=df_supplies.set_index("Supplies")
        df_supplies.to_csv("total_supp.csv")


    def sales_data(self):
        """
        Takes in store data to output it into CSV file
        Note:
            This method only runs during the creation of new sales data
        """
        sales = pd.DataFrame(self.sales)
        sales=sales.set_index("Serial_No")
        sales.to_csv("all_sales.csv")
