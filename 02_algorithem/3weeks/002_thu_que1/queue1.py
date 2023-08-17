def enQ(data):
    global rear
    if rear == Qsize - 1:
      print('Q is Full')   #가득 차면
    else:
        rear +=1
        Q[rear] = data

def deQ():
    global front
    front +=1
    return Q[front]



Qsize = 3
Q = [0] * 10
rear = -1
front = -1      #front:-1


enQ(1)
enQ(2)
rear += 1
Q[rear] = 3
enQ(4)