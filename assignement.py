#A python program that checks whether a number is even orr odd

number =int(input("Enter the number here"))
if number %2 == 0:
    print(number,"its an even number")

else:
    print (number ,"its an odd number")




#A python program that checks whether a letter is a vowel or consonants
letter =input("Enter a single  letter")
if len(letter) ==1 and letter.isalpha():
    if letter in "aeiou":
        print("Letter is a vowel.")
    else:
        print("Letter is a consonant.")




#A python program that returns the perimeter of a rectangle
length =float(input("Enter the length of the rectangle here:"))
width =float(input("Enter the width here of the rectangle:"))

perimeter =2*(length + width)

print("the perimeter of the rectangle is:{perimeter}")