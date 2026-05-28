"""
Recursion is a function that calls itself. This helps us to loop through a data to get result

The 3 rules of recursion:
RuleWhat it meansBase casealways have a stopping conditionProgresseach call must move closer to the base case
"""

#Factorial
"""factorial(4)
= 4 * factorial(3)        # new call with n=3
= 4 * 3 * factorial(2)    # new call with n=2
= 4 * 3 * 2 * factorial(1)# new call with n=1
= 4 * 3 * 2 * 1 * factorial(0) # new call with n=0
= 4 * 3 * 2 * 1 * 1       # base case returns 1
= 24                       # final answer"""
def factorial(n):
    if n == 0:
        return 1
    return (n * factorial(n-1))

print(factorial(5))