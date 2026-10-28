email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")

email_valid = True
id_valid = True

# Email validation
if email.count("@") != 1:
    print("Invalid Email: Missing or extra @ separator")
    email_valid = False
else:
    username, domain = email.split("@")

    if username == "":
        print("Invalid Email: Username is missing")
        email_valid = False

    elif not username.replace(".", "").isalnum():
        print("Invalid Email: Invalid characters in username")
        email_valid = False

    if "." not in domain:
        print("Invalid Email: Missing '.' in domain")
        email_valid = False

    elif domain.startswith(".") or domain.endswith("."):
        print("Invalid Email: Malformed domain")
        email_valid = False

# Registration ID validation
# Example format: AIML-2026-101

parts = reg_id.split("-")

if len(parts) != 3:
    print("Invalid ID: Incorrect '-' separators")
    id_valid = False

else:
    branch, year, number = parts

    if not branch.isalpha():
        print("Invalid ID: Branch must contain letters only")
        id_valid = False

    if not year.isdigit() or len(year) != 4:
        print("Invalid ID: Year must contain 4 digits")
        id_valid = False

    if not number.isdigit() or len(number) != 3:
        print("Invalid ID: Student number must contain 3 digits")
        id_valid = False

# Final Result
print("\n--- Validation Result ---")

if email_valid:
    print("Email: VALID")
else:
    print("Email: INVALID")

if id_valid:
    print("Registration ID: VALID")
else:
    print("Registration ID: INVALID")
