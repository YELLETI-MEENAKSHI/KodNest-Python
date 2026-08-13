def display_invoice_total(price, quantity):
    # Write your code here
    total = price*quantity
    print(f"Total: {total}")
    pass


price = int(input("enter price:"))
quantity = int(input("enter quantity:"))

display_invoice_total(price, quantity)