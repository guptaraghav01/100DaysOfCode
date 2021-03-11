print("This program will calculate the average height of the students.")
student_heights = input("Input a list of student heights(separated by spaces): \n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum_heights = 0
for height in student_heights:
    sum_heights += height

num_students = 0
for student in student_heights:
    num_students += 1

average_height = round(sum_heights/num_students)
print(f"Average student height is: {average_height}")

# Output
# This program will calculate the average height of the students.
# Input a list of student heights(separated by spaces):
# 180 124 165 173 189 169 146
# [180, 124, 165, 173, 189, 169, 146]
# Average student height is: 164