# Write a python program to create a class Laptop with properties [id, name, ram] and create 3 objects of it and print all details.

class laptop:
    def __init__ (self, id, name ,ram):
        self.id = id
        self .name =name
        self .ram =ram
        
    def display(self):
        print(f"the id of computer is : {self .id}")
        print(f"the name of computer is  :{self .name}")
        print(f"the ram of computer is : {self .ram}")
        
        
l1 = laptop(id=22201 ,name="lenovo" ,ram="2gb")
l1.display()
l2 = laptop( id= 234556 ,name = "dell" ,ram= "4gb")
l2.display()
l3 = laptop( id= 24568 , name="hp" ,ram="8gb")
l3.display()        
        

        


