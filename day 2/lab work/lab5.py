# Suppose In the first test there are three groups. The first group has 20 students and thus needs 10

# desks. The second group has 21 students, so they can get by with no fewer than 11 desks.
a=int(input("no. of students in class a :"))
classA=a//2
b=int(input("no of students in class b :"))
classB=b//2
c=int(input("no of students in class c :"))
classc =c//2
print(f"no of chairs needed in class A= {classA}")
print(f"no of chairs needed in class A= {classB}")
print(f"no of chairs needed in class A= {classc}")
remaining_chairsA=a%2
remaining_chairsB=b%2
remaining_chairsC=c%2
print(f"remaining chairs in class A: {remaining_chairsA}")
print(f"remaining chairs in class A: {remaining_chairsB}")
print(f"remaining chairs in class A: {remaining_chairsC}")

