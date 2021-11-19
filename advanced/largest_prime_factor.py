"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? 
"""


# logica:
# fazer uma funcao que verifique se um numero eh primo - para manter o software mais otimizado, 
# eh realizado uma verificao do segundo numero primo ate a raiz desse numero
# 
# na funcao largest_prime, dentro de um loop que percorre todos os numeros impares, sera verificado
# se esse numero eh primo ou nao ultizando outra funcao, caso seja primo, eh verficado se o numero passado
# para a funcao eh divisivel por esse primo, se sim, efetuamos a divisao e o numero primo eh guardado em um array (poderia se armazenado em uma variavel tbm)
#
# eh imporante ressaltar que realizar a divisao por esse numero eh um passo importante para que o algortimo se torne otimizado



import math

def is_prime (number: int) -> bool:
  """ verifica se uma numero eh primo e retorna true/false """
  if number == 2:
      return True
  elif number % 2 == 0:
    return False
  
  for i in range(3, 1 + int(math.sqrt(number))):
    if number % i == 0:
      return False
  return True





def largest_prime (number: int) -> int:
  """ verifica qual eh o maior fator primo de uma numero """
  primes = []
  i = 2
  while number > 1:
    if is_prime(i) and number % i == 0:
        number = number / i
        primes.append(i)
    else:
      i += 1
  print('primes = {}'.format(primes))
  return primes[len(primes)-1]          # retorna ultimo elemento


print(largest_prime(600851475143))

