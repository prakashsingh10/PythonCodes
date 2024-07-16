from customer import Customer
import csv
import controller as c

all_customers = []

#convert customer to csv

def convert_customer_to_csv(list_of_customer):
    file = open("customers.csv", "w")
    file.write()
    file.close()
    for c in list_of_customer:
        f=open("customers.csv", "a")
        f.write(f"{c.id} ,{c.name} ,{c.phone} ,{c.balance} ,{c.citizenship}")
        f.close()
        
#convert csv to customer list 
def convert_csv_to_customer_list():
    all_customers = []
    with open("customers.csv", "r") as file:
        csv_reader = csv.reader()
        for row in csv_reader:
            c=Customer( id=row[0],name=row[1] , balance=float(row[4]),phone=row[2],citizenship=row[3])
            all_customers.append(c)
            return all_customers
        
        
#Add customer 
def add_customer():
    print("adding customer ")
    c=Customer(id="",name="" ,balance=0, phone="",citizenship="")
    c.id=input("enter the customer id :")
    c.name=input("enter the customer name :")
    c.phone=input("enter the customer phone:")
    c.balance=float(input("enter the customer balace:"))
    c.citizenship=input("enter the citizenship number :")
    f=open("customers.csv","a")
    f.write(f"{c.id},{c.name},{c.phone},{c.balance},{c.citizenship}")
    f.close()
    print(f"customers {c.name} added successfully")
     