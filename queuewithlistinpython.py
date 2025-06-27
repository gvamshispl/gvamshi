queue=[]
for i in  range(5):
    ele=int(input("enter a number :"))
    queue.append(ele)
print(queue)

def push(element):
    queue.append(element)
    print("stack after adding element:",queue)
def pop():
    e=queue.pop(0)
    print("poped element is:",e)
    print("stack after poping:",queue)
def peek():
    top=queue[0]
    print("top element is:",top)
push(100)
push(200)
pop()
peek()
