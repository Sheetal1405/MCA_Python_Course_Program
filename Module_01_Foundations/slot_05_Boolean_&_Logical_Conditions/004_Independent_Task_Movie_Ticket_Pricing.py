#Build a ticket price checker:
#Age < 5:Free
#Age 5-17: Rs. 150
#Age 18-59: Rs. 300
#Age 60+: Rs. 100(senior discount)
age = int(input("Enter age: "))

#Write the if/elif/else chain here
if age < 5:
    print("Movie Ticket is free for children below age 5.")
elif age >= 5 and age <=17:
    print("Movie Ticket Price is: Rs. 150")
elif age >= 18 and age<=59:
    print("Movie Ticket Price is: Rs.300")
else:
    print("Movie Ticket Price is: Rs. 100(Senior Citizen Discount)")