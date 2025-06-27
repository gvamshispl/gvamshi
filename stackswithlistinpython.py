stack=[]
for i in  range(5):
    ele=int(input("enter a number :"))
    stack.append(ele)
print(stack)

def push(element):
    stack.append(element)
    print("stack after adding element:",stack)

def pop():
    e=stack.pop()
    print("poped element is:",e)
    print("stack after poping:",stack)

def peek():
    top=stack[len(stack)-1]
    print("top element is:",top)
    
push(100)
push(200)
pop()
peek()



                                                                                                                                                                                                                                                                                                                                           
