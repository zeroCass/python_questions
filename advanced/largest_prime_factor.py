



import math

# # funcao que verifica se um numero n eh primo
# def is_prime (number: int) -> bool:
#     i = 2
#     while i <= math.sqrt(number):
#         if int(number) % i == 0:
#             return False
#         i += 1
#     return True


# #print(is_prime(35))

# n = int(input())
# i = 2
# largest_prime = 0

# while i < n:
#     if is_prime(i):
#         if n % i == 0:
#             largest_prime = i
#     i += 1

# print(largest_prime)


def largest_prime_factor(number):
  i = 2
  while number > 1:
    if number % i == 0:
      number /= i
    else:
      i += 1
  return i

print(largest_prime_factor(600851475143))