def countdown(n):
    if n==0:
        return 0
    print(n)
    return countdown(n-1)

print(countdown(5))

