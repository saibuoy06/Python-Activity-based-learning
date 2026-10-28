marks = [75, 68, 38, 82, 59]

pass_mark = 40
max_mark = 100
max_grace = 5

final_marks = []
grace_used = 0

for mark in marks:
    if mark < pass_mark:
        needed = pass_mark - mark

        if needed <= max_grace:
            mark = mark + needed
            grace_used += needed

    if mark > max_mark:
        mark = max_mark

    final_marks.append(mark)

print("Original Marks:", marks)
print("Final Marks:", final_marks)
print("Grace Marks Used:", grace_used)

if all(mark >= pass_mark for mark in final_marks):
    percentage = sum(final_marks) / len(final_marks)

    print("Result: PASS")
    print("Percentage:", percentage)

    if percentage >= 75:
        print("Classification: Distinction")
    elif percentage >= 60:
        print("Classification: First Class")
    elif percentage >= 50:
        print("Classification: Second Class")
    else:
        print("Classification: Pass")
else:
    print("Result: FAIL")
