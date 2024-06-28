#Add your Electricity Bill From Jan dec In Dec in Dictionary and find total and average 
electericity_bill={
    "jan":100,
    "feb":200,
    "mar":250,
    "apr":300,
    "may":350,
    "jun":375,
    "jul":275,
    "aug":150,
    "sep":225,
    "oct":335,
    "nov":280,
    "dec":270 
}
total_sum=sum(electericity_bill.values())
average_bill= total_sum/len(electericity_bill)


print(f"the total sum of the bill is :Rs {total_sum :.2f}")
print(f"the average of the bill is :Rs{average_bill: 2f}")