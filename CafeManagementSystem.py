# CafeManagementSystem
menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 80
}
bill = {}

print("Welcome to Python Restaurant!")
for key, value in menu.items():
    print(f"{key.capitalize()}: ${value}")

order_total = 0
while True:
    item = input("Enter the name of the item you want to order ('EXIT' to exit): ").lower()
    if item == 'exit':
        break
    elif item in menu:
        try:
            quantity = int(input("Enter the quantity you want: "))
            if quantity <= 0:
                print("Please enter a valid quantity greater than 0.")
                continue
            order_total += menu[item] * quantity
            if item in bill:
                bill[item] += quantity
            else:
                bill[item] = quantity
            print(f"Your item '{item}' has been added to your cart.")
        except ValueError:
            print("Invalid input for quantity. Please enter a valid number.")
    else:
        print(f"Ordered item '{item}' isn't available in the menu.\n")

# Display the bill details
print("\nYour total amount to pay is: $", order_total)
print("\nItem\tQuantity\tPrice")

for item, qty in bill.items():
    item_cost = qty * menu[item]
    print(f"{item.capitalize()}\t{qty}\t\t${item_cost}")

print("\nYour total price: $", order_total)
