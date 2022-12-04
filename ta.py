from random import randint
from sympy import isprime
from user import User

class Ta:
  def __init__(self, n_users):
    self.n_users = n_users
    self.users = []
    self.user_elements = []
    self.p = self.generate_prime_number()

    self.a = randint(1, self.p - 1)
    self.b = randint(1, self.p - 1)
    self.c = randint(1, self.p - 1)

    for i in range(self.n_users):
      rU = self.generate_user_element()
      coef = self.generate_coef(rU)
      
      newUser = User(rU, coef, self.p)
      self.users.append(newUser)

  def generate_random_number(self):
    return randint(0, 10000000000000000)

  def generate_prime_number(self):
    p = self.generate_random_number()
    while not isprime(p):
      p = self.generate_random_number()
    return p

  def generate_user_element(self):
    rU = randint(1, self.p - 1)
    while rU in self.user_elements:
      rU = randint(1, self.p - 1)
    self.user_elements.append(rU)
    return rU


  def generate_coef(self, rU):
    ai = (self.a + self.b * rU) % self.p
    bi = (self.b + self.c * rU) % self.p
    return [ai, bi]

  def getUsers(self):
    return self.users