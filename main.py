print("""Welcome to ABCD General Store!""")
print("""We have these items in stock :-""")
print("""Potato: 15/kg \nOnion: 50/kg \nGarlic: 150/kg
\nChocolate: 50/pcs \nChips: 10/pcs \nMaggi: 15/pcs
\nMasala: 50/pcs \nSoap: 80/pcs \nShampoo: 500/pcs
\nSugar: 70/kg \nSalt: 30/kg""")

items = input("What you want to buy: ")

if items.lower() not in ["potato", "onion", "garlic", "chocolate", "chips", "maggi", "masala", "soap", "shampoo", "sugar", "salt"]:
    print("""Sorry, we do not have that product in our stock! Your request has been noted as a text file in your device. You can mail that file to abc@gmail.com and we will consider it!""")
    file = open("missing_item.txt", "a")
    file.write(items + "\n")
    file.close()
else:
    quantity = int(input("Enter quantity: "))
    checkout = input("Do you want to proceed to checkout? [y/n] ")

    if checkout.lower() == "y":
        print("Item =", items)
        print("Quantity =", quantity)

        if items.lower() == "potato":
            print("Total Price =", 15 * quantity)
        elif items.lower() == "onion":
            print("Total Price =", 50 * quantity)
        elif items.lower() == "garlic":
            print("Total Price =", 150 * quantity)
        elif items.lower() == "chocolate":
            print("Total Price =", 50 * quantity)
        elif items.lower() == "chips":
            print("Total Price =", 10 * quantity)
        elif items.lower() == "maggi":
            print("Total Price =", 15 * quantity)
        elif items.lower() == "masala":
            print("Total Price =", 50 * quantity)
        elif items.lower() == "soap":
            print("Total Price =", 80 * quantity)
        elif items.lower() == "shampoo":
            print("Total Price =", 500 * quantity)
        elif items.lower() == "sugar":
            print("Total Price =", 70 * quantity)
        else:
            print("Total Price =", 30 * quantity)

        address = input("Enter Address: ")
        order_details = f"Item: {items} ; Quantity: {quantity} ; Address: {address}\n"

        order_file = open("order_details.txt", "a")
        order_file.write(order_details)
        order_file.close()

        print("""Order Placed! \nPlease share a text file newly created on your computer named 'order_details.txt' to abc@gmail.com along with the screenshot of the payment made. \nYou can pay on upi id 6200528007@ybl!""")
        print("""Your order will be shipped shortly after receiving all the required documents!""")
