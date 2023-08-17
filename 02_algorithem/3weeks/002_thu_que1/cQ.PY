def enq(data) :
    global rear
    
    if (rear+1) % cQsize == front:
        print('cQ is Full')
    
    else:
        rear = (rear +1) % cQsize
        cQsize[rear]

def deQ():
    global front
    front = (front + 1)%cQsize
    return cQ[front]

cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0

enq(1)
enq(2)
enq(3)
print(deQ())
enq(4)