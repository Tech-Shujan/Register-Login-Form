username = input('Enter your username')

password = input('Enter your Passoword')

userlist = open(username + '.txt', 'r')

data = username + ' : ' + password

print('You are registered \n Login here!')

useragain = input('Enter your username')

passagain = input('Enter your Password')

checkuser = useragain + ' : ' + passagain

for checkuser in userlist.readlines():
  if checkuser == data:
    print('Hello World!')
  else:
    print('Not Found!')
