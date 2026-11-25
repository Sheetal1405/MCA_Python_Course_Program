class Electricity_Bill:
    def calculate_bill(self,units):
        if units<=100:
            bill = units*3
        elif units>=101 and units<=200:
            bill = units*5
        elif units>200:
            bill = units*8
        return bill
    def check_consumption(self, units):
        if units<=100:
            msg =  "Low Consumption"
        elif units>=101 and units<=200:
            msg = "Moderate Consumption"
        elif units>200:
            msg = "High Consumption"
        return msg

h1 =Electricity_Bill()
h2 =Electricity_Bill()
h3 =Electricity_Bill()
h4 =Electricity_Bill()
h5 =Electricity_Bill()

unit = int(input("Enter Units:"))
print(h1.calculate_bill(unit))
print(h1.check_consumption(unit))
