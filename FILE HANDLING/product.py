# Write a program that saves the details of 10 products to a file using user input, 
# including the fields: id, name, quantity (qty), and price.

class Product:
    def __init__(self ,id , name , quantity , price ):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def display(self):
        print(f"product id is : {self.id}")
        print(f"product name is : {self.name}")
        print(f"product quantity is :{self.quantity}")
        print(f"product price is : {self.price}")  
        
        
          