
#  Given the integer N - the number of minutes that is passed since midnight - how many

# hours and minutes are displayed on the 24h digital clock?
n=int(input("minutes passed: "))
hours = n//60
minutes=n%60
print(f"{n}minutes passed {hours}:{minutes}")