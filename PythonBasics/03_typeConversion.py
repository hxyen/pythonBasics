# int-function -> converting a value to an int
birthYear = input("Enter your birth year: ")
age = 2022 - int(birthYear)
print(age)


# all functions
int()
float()  # float-function ->  converting a value to a floating-point number
bool()
str()


# Exercise:  Write a basic calculator program that gives you a sum
x = input("Enter your first value: ")
y = input("Enter your second value: ")
sum = float(x) + float(y)
print("Result:" + str(sum))
