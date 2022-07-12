friends = ["Lem", "Jorell", "Jarrett", "Jason", "Javier"]
numbers = [2, 4]
print(friends[1])
print(friends[-2])
print(friends[1:])
print(friends[0])

friends.extend(numbers)
friends.append("Quinden")
friends.insert(3, "Ben")

print(friends)

friends.remove(2)
friends.remove(4)

print(friends)
friends.pop()

print(friends.index("Ben"))
friends.sort()
print(friends)

