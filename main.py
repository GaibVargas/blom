from ta import Ta

trusted_authority = Ta(n_users = 3)
users = trusted_authority.getUsers()

user0 = users[0]
user1 = users[1]

rU = user0.get_user_element()
rV = user1.get_user_element()

key01 = user0.get_key(rV)
key10 = user1.get_key(rU)

print(key01)
print(key10)