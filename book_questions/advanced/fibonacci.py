

numbers = {}
def fibonacci (n):
    if n in numbers:
        return numbers[n]


    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    numbers[n] = value
    return value


print(fibonacci(10))
print(numbers)