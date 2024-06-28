electricity_bill={
    "january":200,
    "febrary":250,
    "march":300,
    "april":350,
    "may":280,
    "june":360,
    "july":400.
    "august":290,
    "september":180,
    "october":390,
    "november":370,
    "december":280
}
total=sum(electricity_bill)

average_electricity_bill=total/12
print(f"total sum of electricity bill from jan to dec is :{total_sum}")
print(f"the average of electericty bill is :{average_electricity_bill}")