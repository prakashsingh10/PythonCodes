#wap to print even number fro, start to end


def display_even(first,last):
    for i in range(first,last+1):
        if i % 2 == 0:
            print(i)
            
            
            
start =100
end =150
display_even(start,end)    
print("\t")
display_even(500,580)       