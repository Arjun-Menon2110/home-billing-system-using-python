from datetime import datetime 

# Title
print(" --------Home Billing System--------   ")

# Input total amount
total = int(input("Enter Your Total Amount="))
bill = {}

# Get current date and format it
today = datetime.now()
formatted_date = today.strftime("%d-%m-%Y")

# Collect product details
while True:
    product = input("Enter Your Product Name (type 'end' to finish): ")
    if product.lower() == "end":
        break
    
    price = int(input(f"Enter the price of {product}: "))
    bill[product] = price

# Display the bill
print(f"\nxxxxxxxx {formatted_date} xxxxxxx")
for item, price in bill.items():
    print(f"{item} = {price}")

# Calculate the remaining amount
total_calculated = sum(bill.values())
remaining = total - total_calculated
print(f"\nYour calculation of bill is: {total} - {total_calculated} = {remaining}")

# Generate and save the bill to a text file
filename = f"bill_{formatted_date.replace('-', '_')}.txt"
with open(filename, "w") as file:
    file.write(f" --------Home Billing System--------\n")
    file.write(f"Date: {formatted_date}\n\n")
    file.write("Items and Prices:\n")
    for item, price in bill.items():
        file.write(f"{item} = {price}\n")
    file.write(f"\nTotal Calculation: {total} - {total_calculated} = {remaining}\n")

print(f"\nBill saved to {filename}")
