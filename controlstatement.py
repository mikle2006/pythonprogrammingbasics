#program1
age =int(input("How old are you?"))
if age >18:
    print("Your are a voter")
else:
    print("Your are a voter")

#program2
temperature =float(input("Enter current temperature e.g 23.0:"))

if temperature > 25.0:
    print("It is too hot")

elif temperature <25.0:
    print("It is too cold")

else:
    print("Normal temperature")
    print()

#program3
first =int(input("Enter First number:"))
second =int(input("Enter First number:"))
third =int(input("Enter First number:"))

if first>second and first>third:
    print(first,"is the largest number")

elif second >first and second >third:
    print(second,"is the largest number")

elif third >first and second:
    print(third,"is the largest number")