from ta import getCoef, getUser
from user import getKey

user0 = getCoef(0)
user0Value = getUser(0)
user1 = getCoef(1)
user1Value = getUser(1)

key10 = getKey(user0Value, user1)
key01 = getKey(user1Value, user0)

print(key01)
print(key10)