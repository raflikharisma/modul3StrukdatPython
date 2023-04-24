# create an empty list called stack
stack = []

# define a function to add elements to the stack
def push(stack, element):
    stack.append(element)

# define a function to remove elements from the stack
def pop(stack):
    if len(stack) == 0:
        return None
    else:
        return stack.pop()

# add elements to the stack
push(stack, "Rafli")
push(stack, "Kharisma")
push(stack, "Akbar")

# print the stack
print(stack)

# search for the index of "Kharisma" in the stack
search = -1
for i in range(len(stack)):
    if stack[i] == "Kharisma":
        search = i

# remove elements from the stack until "Kharisma" is at the top
while search != -1 and search < len(stack)-1:
    pop(stack)
    search += 1

# remove and print the top element from the stack
top = pop(stack)
print(top)

# check if the stack is empty
if len(stack) == 0:
    print(True)
else:
    print(False)