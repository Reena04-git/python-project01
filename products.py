
class Shopping:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self, quantity=1):
        print(self.name, "-", quantity, "x", self.price,
              "=", quantity * self.price)


products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Bottle": 100,
    "Pencil": 5
}

cart = {}
total = 0

print("AVAILABLE PRODUCTS")
for item, price in products.items():
    print(item, ":", price)

while True:
    choice = input("\nEnter product name (to bill or quit type 'exit'): ").strip()

    if choice.lower() == "exit":
        break

    choice = choice.title()

    if choice in products:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            cart[choice] = cart.get(choice, 0) + quantity
            print("Added to cart!")
        else:
            print("Invalid quantity")
    else:
        print("Product not available")

print("\n~~BILL~~")

for item, quantity in cart.items():
    obj = Shopping(item, products[item])
    obj.display(quantity)
    total += products[item] * quantity

if total >= 500:
    discount = total * 0.10
    print("Discount:", discount)
else:
    discount = 0
    print("No discount")

final_amount = total - discount

print("Total:", total)
print("Final Amount:", final_amount)
