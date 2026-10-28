# Product data: (Product ID, Price, Stock Quantity)

products = (
    ("P101", 500, 10),
    ("P102", 800, 3),
    ("P103", -200, 8),
    ("P104", 1200, 0),
    ("P105", 300, 15)
)

total_inventory_value = 0

print("--- Product Catalogue Audit ---")

for product in products:

    product_id, price, stock = product

    # Check invalid records
    if product_id == "" or price < 0 or stock < 0:
        print(product_id, "- Invalid Record")
        continue

    # Calculate inventory value
    inventory_value = price * stock
    total_inventory_value += inventory_value

    print("\nProduct ID:", product_id)
    print("Price: ₹", price)
    print("Stock:", stock)
    print("Inventory Value: ₹", inventory_value)

    # Check replenishment
    if stock < 5:
        print("Status: Replenishment Required")
    else:
        print("Status: Sufficient Stock")

print("\n--- Summary ---")
print("Total Inventory Value: ₹", total_inventory_value)
