row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input(
    "Where do you want to put the treasure?\nEnter column number and row number.\nExample: 23 for column 2, row 3.\n")

column = int(position[0])
row = int(position[1])

map[row-1][column-1] = "💰"

print(f"{row1}\n{row2}\n{row3}")


# Output
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# Where do you want to put the treasure?
# Enter column number and row number.
# Example: 23 for column 2, row 3.
# 31
# ['⬜️', '⬜️', '💰']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']