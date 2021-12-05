#find BMI of a person where take mass and height as input from the user

# BMI=mass in kg / (height in m)2
mass=int(input("enter the mass: "))
height=int(input("enter the height: "))
bmi=mass/height*height
print(f"bmi of person: {bmi}".format(bmi))
