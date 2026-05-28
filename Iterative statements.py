'''
Python commonly uses 2 types of iterative statments
1. if statement
2. else statement
'''
#if statement
x = 5
y = 16
if (y>x):
    print("y is grater than x")

#else statement
X = 5
Y = 16
if (y>x):
    print("Y is grater than X")
else:
    print("X is greater than Y")

#shorthand if-else (if theres only 1 statement for if and else, it can be declared in the same line)
a = 1
b = 4
print("a") if a>b else print("b")

#Nested if-else (if-else statements can be used within themselves)
marks = 81
attendence = 75

if (marks >= 50):
    if (attendence >=75):
        print("You are promoted")
    else:
        print("low attendence")
else:
    print("FAIL")