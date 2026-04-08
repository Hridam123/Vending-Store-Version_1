# **Advanced Vending System(AVS) v0.1**

_A modular retail simulation built with Python and Pandas_

## **Highlights:**

- Dual Payment Modes: Supports both Pre-paid( balanced based) Post-paid transactions
- Recursive Financial Module: Contains smart logic which ensures that the transactions aren't finalized until full-payment
- Greedy Change Optimization: Mathematically calculates as serves minimum number of coins for every refund and change
- Persistent Data Memory: Sales and Inventory data doesn't reset automatically when the program restarts(in real world situation-power goes out)
- Admin Features: Real-time stock injection and database reset(inventory and sales) built right into the system

## **Overview**

Advanced Vending System (AVS) is a simulation of modern retail technology. While many other
vending machine scripts are based on linear and rigid algorithm which contains monotonous features, 
AVS is built using Object-Oriented Programming and Dependency Injection, ensuring adaptation of
different systems on class-based approach. 

This also means that two of the main components of retail system are separated and operate on their
own paths but have seamless communication. 


## **Primary Objective**

AVS primarily focuses on modernizing the traditional localized retail systetm like the one present
in vending machine. Instead of traditional post-paid services AVS enables user to have pre-paid
balance based payment approach, so that user can bulk buy instead of keep repeating the process. 
(This makes AVS user friendly as well as encourages sales.)

AVS also focuses on using Validation Logic by integrating try/except blocks and while loops, ensuring
that a single wrong input doesn't crash the programs.


## **Key Features**

- Bi-Input Support: The program can handle both Cash and Multiple Coins( Pennies, Nickels, Dimes, Quarters,
 and Dollars seamlessly.
- Recursive payment alogorithm. The program enables recursive payments in both pre-paid service and
  post-paid service.
- Greedy Refund: The program uses an optimized algorithm to refund or return change using the largest
  coin denominations first which reduces the number of coins given.
- Real-time data Analytics: All the sales are stored with their timestap in (all_sales.csv) emsuring real-time
- buisness editing. The csv format also allows the sales to be studied by data Analytics


## **Technical Stack**

- Language: Python 3.12
- Libraries: Pandas( for Database management and receipt generation)
- Architecture: Modular Class-based Structure


## **File Structure**

- main.py: It is the central hub which manages UI and user interaction

- money_manager.py: Handles financial logic and currency calculations

- handle_inventory.py: Used for Inventory checks, Stock updates and Sales Management

- inventory.py: Used for resetting the database for Inventory and Sales

- total_supp.csv: Contains real-time database for stock and prices

- all_sales.csv: Records every sales permanently


### **Author**
*Hridam Adhikari*

*Aspiring Computer Science Student and Math Olympiad Enthusiast*


