# Develop a software application for a bank that includes functionalities to add and view customer information. 
# Each customer should have an ID, name, phone number, and balance ,citizenship

class Customer:
    def __init__(self, id, name, phone  , balance , citizenship):
        self.id =id
        self.name = name
        self.phone = phone
        self.balance = balance
        self.citizenship = citizenship
        
    def display_customer(self):
        print(f"enter the customer is {self.id}")
        print(f"enter the customer name is {self.name}")
        print(f"enter the customer phone is {self.phone}")
        print(f"enter the customer balance is {self.balance}")
        print(f"enter the customer citizenship number is {self.citizenship}")
        
        
           
        
        
        
        