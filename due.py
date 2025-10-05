# A program to calculate the customer due amount after paying a bill of a certain amount 

# Function for amounts

def to_be_paid(bill_amount, amount_amount):
    due = bill_amount - amount_amount
    return max(due, 0)

# User input for bills and payment 

bill = int(input("Enter the bill amount: $"))
payment = int(input("Enter the payment amount: $"))

# Calling function and printing output

due = to_be_paid(bill, payment)
print(f"The total to be paid is: ${due}")