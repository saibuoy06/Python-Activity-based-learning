courses = [
    ("Python", "09:00", "10:00", "Room101"),
    ("Maths", "10:00", "11:00", "Room102"),
    ("English", "09:30", "10:30", "Room103"),
    ("Web Development", "11:00", "12:00", "Room101")
]

unavailable_rooms = ("Room105", "Room106")

valid = True

print("--- Timetable Validation ---")

# Check unavailable rooms
for course in courses:
    subject, start, end, room = course

    if room in unavailable_rooms:
        print(subject, "- Room unavailable:", room)
        valid = False

# Check time conflicts
for i in range(len(courses)):
    for j in range(i + 1, len(courses)):

        course1 = courses[i]
        course2 = courses[j]

        # Check overlapping time
        if course1[1] < course2[2] and course2[1] < course1[2]:

            print(
                "Time Conflict:",
                course1[0],
                "and",
                course2[0]
            )

            valid = False

# Final result
print("\n--- Final Result ---")

if valid:
    print("Timetable is VALID")
else:
    print("Timetable is INVALID")
