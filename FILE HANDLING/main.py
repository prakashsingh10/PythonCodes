from product import Product 

total_products = int(input(f"enter the number of products :"))
list = []
 
 
for i in range(total_products):
    i = input(f"enter the product id :")
    n = input(f"enter the product name :")
    q=int(input(f"enter the product quantity :"))
    p= int(input(f"enter the product price :"))
    pro=Product(id=i ,name=n ,quantity=q ,price=p)
    f=open("produ.csv","a")
    f.write(f"Product id is :{pro.id}\nProduct name is :{pro.name}\nProduct quantity is :{pro.quantity}\nProduct price is :{pro.price}\n")
    f.close()
    
