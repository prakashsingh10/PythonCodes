import controller as c
option_text = """
what do want to do in the bank section ?
1.Add customer 
2.view customer 
3.view all customers 
4.update customer 
5.delete customer 

"""
option = int(input(option_text))
if option == 1:
    c.add_customer()
elif option == 2:
    c.view_customer()
elif option == 3:
    print("view customer by id ") 
    c.view_single_customer()
elif option == 4:
    print("update customer ")
    c.update_customer()
elif option ==5:
    print("delete customer ")
    c.delete_customer() 
else:
    print("invalid option given")               