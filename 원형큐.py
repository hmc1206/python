# import queue
MAX_QSIZE=5
def Queue(): #비어있는 원형 큐 생성
    global queue,rear,front
    global items
    items = [None]*MAX_QSIZE
    queue=[]
    rear = front = 0

def isEmpty():
    global rear
    global front
    return rear==front

def isFull():
    global rear
    global front
    return front % MAX_QSIZE == (rear+1) % MAX_QSIZE

def clear():
    global queue
    queue=[]

def enqueue(x):
    global queue, rear, items
    rear = (rear+1) % MAX_QSIZE
    items[rear] = x
    queue.insert(rear,x)

def dequeue():
    global queue
    global front,items
    if not isEmpty():
        front = (front+1) % MAX_QSIZE
        queue.remove(items[front])
    return items[front]

def peek():
    global queue
    global front
    if not(isEmpty()):
        return queue((front+1) % MAX_QSIZE)

def size():
    global queue
    return len(queue)


Queue()

enqueue('A')
enqueue('B')
enqueue('C')
print(queue)

print("삭제>> ", dequeue())
print(queue)

enqueue('D')
print(queue)

print("삭제>> ", dequeue())
print(queue)

# Queue()

# for i in range(0,5):
#     enqueue(i)

# print(queue)


# print('큐가 비어있나요? %s' % isEmpty())

# for _ in range(2):
#     print('삭제한 값은? ',dequeue())


