import unittest      
import re             
import sqlite3

welcome = ("Welcome to Robert's Sports app")
print(welcome)

aList = ['Hat $19, Sweater $32, Shirt $27, Jacket $50']
print("Example of what we sell",aList)

def main():
#constants, this will become a list   
    Hat = 19 
    Sweater = 32
    Shirt = 27
    Jacket = 50
    TAX_RATE = 0.07275

    
    

#input item
    itemName = str(input("Please make a selection from our list of items: "))
    itemName = itemName.title()
    
    print(itemName)
        

# thinking of adding a while statement to cycle through the error until user
#enter the right amount.    
    
#input price
    itemPrice = int(input("Price:"))
    print(itemName, itemPrice)
    while itemName != "":
        
            
        #program shows error and continue on to the testing phase.
        #itemPrice = float(itemPrice)
        if itemPrice < 0:
            print("Error: Price must be between 200 and 0")
        elif itemPrice > 200:
            print("Error: Price must be between 200 and 0")
        else:
                           
            #input how many
            itemCount = int(input("How many:"))
                   
            #muiltly itemPrice * itmeCount
            itemCombine = float(itemPrice) * int(itemCount)
            print("$",itemCombine, itemName)

            #def taxCount(itemCombine, tax, total):
            # itemCombine += tax
            tax = int(itemCombine * TAX_RATE)
            print("tax", tax)
            total = int(tax + itemCombine)               
            print("Todays total comes to", "$",total, "for 2", itemName)
            conn = sqlite3.connect("merchantapp.db")
    
            curs = conn.cursor()
            # Create a database table with columns for user's name (name), user id (user),  and password (password)
            curs.execute('CREATE TABLE IF NOT EXISTS merchantItem (' +itemName+' var, '+itemPrice+' var, '+total+' var) ')
            curs.execute('INSERT INTO merchantItem VALUES(' +total+' var)')
           

            if __name__== "__main__":
                import doctest
                doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)

            if __name__=="__main__":
                unittest.main()



            # Add some sample data. Note that the admin is the first entry in the table, as is often the case
#curs.execute("INSERT INTO merchantItem VALUES (" +'itemName'+ +'itemPrice'+ +'total'+ ") ")
    #curs.execute("SELECT * FROM merchantItem WHERE total> 100 ")
#print(curs.fetchall())






                

                

        



main()


    
 




