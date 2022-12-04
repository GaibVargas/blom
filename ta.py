from random import randint
from sympy import isprime

def generate_random_number():
    return randint(0, 100000000000)

p = generate_random_number()
while not isprime(p):
    p = generate_random_number()

n_users = 3
users = []
for i in range(n_users):
  n = randint(1, p - 1)
  while n in users:
    n = randint(1, p - 1)
  users.append(n)

coef = []

a = randint(1, p - 1)
b = randint(1, p - 1)
c = randint(1, p - 1)

for i in range(len(users)):
  ai = (a + b * users[i]) % p
  bi = (b + c * users[i]) % p
  coef.append([ai, bi])

def getCoef(user):
  return coef[user]

def getUser(index):
  return users[index]

def getPrime():
  return p