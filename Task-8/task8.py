
occupancy = [
    [40, 45, 50, 48, 52],   # Ward 1
    [25, 30, 28, 35, 32],   # Ward 2
    [15, 18, 20, 22, 19]    # Ward 3
]

capacity = [50, 35, 20]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

peak_occupancy = 0
peak_ward = 0
peak_day = ""

for i in range(len(occupancy)):

    print("\nWard", i + 1)

    for j in range(len(occupancy[i])):

        occupied = occupancy[i][j]

        # Calculate utilization percentage
        utilization = (occupied / capacity[i]) * 100

        print(days[j], "- Occupied:", occupied,
              "- Utilization:", round(utilization, 2), "%")

        if occupied > capacity[i]:
            print("Capacity Violation!")

        # Find peak demand
        if occupied > peak_occupancy:
            peak_occupancy = occupied
            peak_ward = i + 1
            peak_day = days[j]

print("\n--- Summary ---")

print("Peak Occupancy:", peak_occupancy)
print("Peak Ward:", peak_ward)
print("Peak Day:", peak_day)
