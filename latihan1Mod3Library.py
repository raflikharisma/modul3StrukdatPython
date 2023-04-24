stack = []

stack.append("Rafli")
stack.append("Kharisma")
stack.append("Akbar")
print(stack)

search = stack.index("Kharisma")
while search != -1 and search > 0:
    stack.pop()
    search -= 1

print(stack.pop())
print(not stack)    