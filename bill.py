def bill_pay(bill,tip):
    total=(bill+(bill*(0.01*tip)))
    total= round(total)
    print(f"Amount due to pay is ₹{total}")

print("Welcome to the billing counter")
amt=int(input("Enter the bill amount: "))
t=int(input("Enter the tip percentage of your choice: "))

bill_pay(amt,t)
