#N students take K apples and distribute them among each other evenly. The remaining

# (the indivisible) part remains in the basket. How many apples will each single student

# get? How many apples will remain in the basket? The program reads the numbers N and

# K. It should print the two answers for the questions above.
s=int(input("no of students ="))
a=int(input("no apples ="))
apples = a//s
remaining_apples= a%s
print(f"each students got {apples} apples",)
print(f"{remaining_apples} apples are remaing")