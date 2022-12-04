from ta import getPrime

def getKey(value, coefients):
  return (coefients[0] + coefients[1] * value) % getPrime()