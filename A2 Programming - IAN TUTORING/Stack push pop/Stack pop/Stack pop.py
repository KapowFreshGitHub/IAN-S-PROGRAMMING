Stack = []

def push():
    item = int(input("Enter number"))
    Stack.append(item)
for x in range(8):
    push()

def pop():
    item =Stack.pop(-1)
    print(Stack)
for y in range(5):
    pop()

