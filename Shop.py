kg_rice = 100
toy = 500

rice = int(input("\nPlease Enter The Quantity of Purchased Rice: "))
t = int(input("\nPlease Enter The Quantity of Purchased Toys: "))

a = kg_rice * rice
b = toy * t
c = a + b

if c > 1000:
    discount = c * 0.10 
    c -= discount
    print("\nTotal Cost after 10% discount:", c)
else:
    print("\nTotal Cost:", c)
