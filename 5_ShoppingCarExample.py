item = input("what item would you like to buy?:")
price = input("what is the price?: ")
price = int(price)

quantity = input("How many would you like?: ")
quantity = int(quantity)

total = price * quantity
print(f"You have bought {quantity} {item}(s)")
print(f"Your total price is: {total}$")



