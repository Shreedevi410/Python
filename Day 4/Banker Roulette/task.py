import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# 1 method
Random_friends = random.choice(friends)
#2 method
index = random.randint(0,4)
print(Random_friends)

print(friends[index])
