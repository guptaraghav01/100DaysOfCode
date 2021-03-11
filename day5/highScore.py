print("This program will calculate the highest score from the given list.")
student_scores = input("Input a list of student scores(separated by spaces): \n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score>highest_score:
        highest_score = score

print(f"The highest score is: {highest_score}")

# Output
# This program will calculate the highest score from the given list.
# Input a list of student scores(separated by spaces):
# 78 65 89 86 55 91 64 89     
# [78, 65, 89, 86, 55, 91, 64, 89]
# The highest score is: 91