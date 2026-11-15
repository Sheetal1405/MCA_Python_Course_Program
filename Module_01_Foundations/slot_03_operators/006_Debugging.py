#BROKEN - forgot to convert before adding
price = input("Enter price:")
quantity = input("Enter quantity:")
total = price* quantity    #TypeError-ish result: string repeated, not multiplied correctly

#FIXED
total = int(price) * int(quantity)
print("Total:", total)