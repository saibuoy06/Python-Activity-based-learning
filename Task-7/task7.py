reg_id = input("Enter Registration ID: ")

parts = reg_id.split("-")

if len(parts) == 3:
    year = parts[0]
    branch = parts[1]
    number = parts[2]

    # Validate structure
    if year.isdigit() and len(year) == 4 and \
       branch.isalpha() and \
       number.isdigit():

        print("\n--- Student Details ---")
        print("Registration ID:", reg_id)
        print("Admission Year:", year)
        print("Branch:", branch.upper())
        print("Student Number:", number)

        # Branch classification
        if branch.upper() == "AIML":
            print("Branch Category: Artificial Intelligence & ML")
        elif branch.upper() == "CSE":
            print("Branch Category: Computer Science")
        elif branch.upper() == "ECE":
            print("Branch Category: Electronics")
        elif branch.upper() == "EEE":
            print("Branch Category: Electrical")
        else:
            print("Branch Category: Other")

        # Admission year classification
        if year == "2026":
            print("Admission Category: Current Batch")
        elif int(year) < 2026:
            print("Admission Category: Previous Batch")
        else:
            print("Admission Category: Future Batch")

    else:
        print("Invalid Registration ID structure")

else:
    print("Invalid ID: Use format YYYY-BRANCH-NUMBER")
