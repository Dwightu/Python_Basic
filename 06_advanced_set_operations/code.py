friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne'}

#local_friends = {'Rolf'}
local_friends = friends.difference(abroad)
print(local_friends)


friends2 = local_friends.union(abroad)
print(friends2)


friends3 = friends.intersection(abroad)
