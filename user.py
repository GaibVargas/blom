class User:
  def __init__(self, user_element, coef, p):
    self.user_element = user_element
    self.ai = coef[0]
    self.bi = coef[1]
    self.p = p

  def get_key(self, x):
    return (self.ai + self.bi * x) % self.p

  def get_user_element(self):
    return self.user_element