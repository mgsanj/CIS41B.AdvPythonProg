import sqlite3

file = 'Products.csv'
# ----- question 1 -------
class Product():
    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return str(self.product + ': ' + str(self.price) + ', ' + str(self.quantity))
# ------- add -----------
    def sort(self):
        return self.product
    
    def search(self, productName):
        if productName == self.product:
            return self.price, self.quantity
#look to next question for how I use the Product objects
# -------------------------
    
    
# -------- question 2 ------
class Product_Warehouse():
   
    def __init__(self):
        self.listP = []
            
    def __getitem__(self, index):  #bracket operator
        prodObject = self.listP[index]
        return prodObject
    
    
    def __iter__(self):
        for element in self.listP:  
            yield element  
#refer to next problem for function Reader() which would also be inside Product_Warehouse() in order to create self.listP or the list of Product objects curated from the Products.csv file
# ------------------------
# ------ question 3 ------
            
    def Reader(self, csvfile):
        csv = open(csvfile)
        for line in csv:
            rline = line.rstrip()
            cline = rline.split(',')
            if cline[0].isalpha() == True:
                for item in cline[1:]:
                    if item.isdigit() == True:
                        e = Product(cline[0],float(cline[1]),int(cline[2]))
                        print(e)
                        self.listP.append(e)    
#Product_Warehouse().Reader('Product.csv')
# ------------------------
# ------ question 4 ------
#For this question, I chose to define a function inside of Product Warehouse in order to access self.listP
    
    def Sort(self):
        self.listP.sort(key=lambda x: x.product)  #sorts by name of product
#Product_Warehouse().Sort()
# ------------------------
# ------ question 5 ------
'''
def insert(query,tup):
        global sqliteConnection
        try:
            cursor = sqliteConnection.cursor()
            cursor.execute(query, tup)
            print("Search query: ",query)
            sqliteConnection.commit()
            print("Inserted successfully into table")
        except sqlite3.Error as error:
            print("Failed to insert: ", error)    
    

connect(database)


    for product in Product_Warehouse().Reader('Products.csv'): #goes through each Product object in the list made in the Product_Warehouse class
        insert_query = """INSERT INTO Database (product, price, quantity) VALUES (?, ?, ?)"""
        tup = (product.product, product.price, product.quantity)
        insert(insert_query,tup)
'''
#Insert the Product not the Product fields!!!!!!!!
# ------------------------

   
    
        
    
if __name__ == '__main__':
    csv = "/Users/SanjanaGadaginmath/Desktop/2021-2022 School Year/School/Third Quarter/Adv. Python Programming/Midterm/Products.csv"
    warehouse = Product_Warehouse()
    warehouse.Reader(csv)
    warehouse.Sort()
    
    
    
    

'''
3. Read the CSV data.  Store each Product data in a Product object and insert the Product object into Product warehouse.
'''

'''
4. Sort the Product Warehouse products by name.  Use the built-in Python sorting routines to sort the products.
'''

'''
5. Insert a Product object into an Sqlite database.  Assume the table in the database has been created.
'''