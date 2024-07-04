#type of function
#1 no parameter and no return type

def display_data():
    print("my nam is prakash ")
    print("i live in kalanki ")
    
display_data()


##2 parametr and no return type

def add(n1 ,n2):  #parameter
    total=n1 + n2
    print(f"total is {total}")
add(50,60) #arguments    


###3 parameter and return type

def find_cube(number):
    cube = number*number*number
    return cube 
my_value =find_cube(3)
print(my_value)


####4 no parameter and return type

def minvoter_age():
    return 18
ram_age = 12
if ram_age >=minvoter_age():
    print("ram is ready to vote")
    
else:
    print("ram is not ellisible for vote")
