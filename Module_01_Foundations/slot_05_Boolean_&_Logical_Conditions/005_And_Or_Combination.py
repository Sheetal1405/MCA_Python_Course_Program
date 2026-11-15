#A user gets a loan only if they are employed AND have a credit score above 700

is_employed = input("Are you employed?(yes/no): ") == "yes"
credit_score = int(input("Enter credit score: "))

if is_employed and credit_score > 700:
    print("Loan Approved")

else:
    print("Loan Rejected")