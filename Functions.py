#1.Built-Functions/Standard Library Functions

x = max(67,89,90,23,67,45)
print("The maximum number is",x)

y=min(67,89, 90, 23, 67,45)
print("The minimum number is",y)

z= pow(2,3)
print("The power of 2 is",z)

#.User-Defined Functions
def greeting():
    print("Hello world!")

    greeting() #callinga function

def school():
    print("My coding school is eMobilis")

    school()

#Parameter and Argument
def add(num1, num2):
    print(num1 +num2)

add(5,10)
add(20,10)


def student(fullname,course, gender):
    print(fullname,course,gender)

student("Marry Mbotela","MIT","Female")
student("Steven letto","MIT","Female")
student("Onesmus mainge","MIT","Female")
student("Joseph Kuria","MIT","Female")
student("Austin fernandes","MIT","Female")

#A python program that displasy details of five employee
#Fintech using parameter and argument
#Fullname,email,age,position,salary,marriage status


def employee(fullname,email,age,position,salary,marriage_status):
    age=int(age)
    salary=float(salary)
    print(fullname,email,age,position,salary,marriage_status)
employee("Michael muriithi","mungaimichael689@gmail.com","45","CEO","60000","married")
employee("Joseph Njau","mungaimichael689@gmail.com","32","Assistant of CE0","55000","married")
employee("Joseph Njau","mungaimichael689@gmail.com","32","Assistant of CE0","55000","married")
employee("Joseph Njau","mungaimichael689@gmail.com","32","Assistant of CE0","55000","married")
employee("Joseph Njau","mungaimichael689@gmail.com","32","Assistant of CE0","55000","married")