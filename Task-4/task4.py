fine_rules = {
    "speeding": 1000,
    "no_helmet": 500,
    "signal_jump": 1500,
    "no_license": 2000
}

vehicle = input("Enter vehicle category (bike/car): ").lower()
n = int(input("Enter number of violations: "))

total_fine = 0
serious_offences = 0

for i in range(n):
    print("\nViolation", i + 1)

    offence = input("Enter offence type: ").lower()
    repeat = input("Repeat offence? (yes/no): ").lower()

    if offence not in fine_rules:
        print("Invalid offence type")
        continue

    fine = fine_rules[offence]

    # Vehicle category rule
    if vehicle == "car":
        fine += 200

    # Repeat offence rule
    if repeat == "yes":
        fine = fine * 2

    # Serious offence check
    if offence == "no_license" or repeat == "yes":
        serious_offences += 1

    total_fine += fine

    print("Fine: ₹", fine)

print("\n--- Penalty Summary ---")
print("Vehicle Category:", vehicle)
print("Total Fine: ₹", total_fine)

if serious_offences >= 2:
    print("Disqualification Status: DISQUALIFIED")
else:
    print("Disqualification Status: NOT DISQUALIFIED")
