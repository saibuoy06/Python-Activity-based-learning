# Stock in 3 warehouses for 3 products
stock = [
    [50, 30, 70],   # Warehouse 1
    [20, 60, 40],   # Warehouse 2
    [80, 25, 50]    # Warehouse 3
]

products = ["Product A", "Product B", "Product C"]

# Required target stock for each product
target = [50, 40, 50]

for i in range(len(stock)):
    print("\nWarehouse", i + 1)

    for j in range(len(stock[i])):

        quantity = stock[i][j]
        required = target[j]

        print(products[j], "- Stock:", quantity,
              "- Target:", required)

        # Check shortage or surplus
        if quantity < required:
            shortage = required - quantity
            print("Shortage:", shortage)

        elif quantity > required:
            surplus = quantity - required
            print("Surplus:", surplus)

        else:
            print("Stock meets target")


print("\n--- Required Transfers ---")

# Compare warehouses and transfer stock
for p in range(len(products)):

    for i in range(len(stock)):
        if stock[i][p] < target[p]:

            needed = target[p] - stock[i][p]

            for j in range(len(stock)):

                if stock[j][p] > target[p]:

                    available = stock[j][p] - target[p]

                    transfer = min(needed, available)

                    if transfer > 0:
                        print(
                            products[p],
                            ": Transfer",
                            transfer,
                            "from Warehouse", j + 1,
                            "to Warehouse", i + 1
                        )

                        stock[j][p] -= transfer
                        stock[i][p] += transfer
                        needed -= transfer

                    if needed == 0:
                        break
