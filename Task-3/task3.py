products = [
    ["Shirt", 500, 2],
    ["Shoes", 1200, 1],
    ["Bag", 800, 1],
    ["Watch", 1000, 1]
]

budget = 3000
total = 0

# Calculate total cost
for product in products:
    name = product[0]
    price = product[1]
    quantity = product[2]

    cost = price * quantity
    total += cost

print("Total before discount: ₹", total)

# Apply 10% discount if total is above ₹3000
if total > 3000:
    discount = total * 0.10
else:
    discount = 0

final_total = total - discount

print("Discount: ₹", discount)
print("Total after discount: ₹", final_total)
print("Budget: ₹", budget)

# Reduce purchases until within budget
if final_total <= budget:
    print("Purchase is within budget.")

else:
    print("\nBudget exceeded!")
    print("Reduce the following purchases:")

    for product in reversed(products):
        while product[2] > 0 and final_total > budget:
            product[2] -= 1
            final_total -= product[1] * 0.90

            print("Reduce 1", product[0])

print("\nFinal Shopping List:")

for product in products:
    print(product[0], "- Quantity:", product[2])

print("Final Cost: ₹", round(final_total, 2))
