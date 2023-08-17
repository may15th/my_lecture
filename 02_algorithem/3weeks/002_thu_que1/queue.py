from collections import deque       #double ended que라서 deque

# deq = deque()

# queue.append('A')
# queue.append('B')
# print(queue)
# print(queue.pop(0))     #스택과 다른 유일한 점
# print(queue)


queue = deque()
print(type(queue))      #instance
queue.append('A')
queue.append('B')
print(queue)
print(queue.pop())


# 리스트에서 0번째 요소 빼면 b가 다시 0번째가 되야...
# a뺀자리 값이없음. B땡겨와 C자리 없애는 것 까지 해야.
# 리스트 자료구조 10억개면 10억개 다 재배치 해야 STACK 끝만 빼면 끝인 것과 달라.


# front와 rear개념 사용
# front와 rear 인덱스 사용하면 연산속도 빠르게 할 수 있어.
# pop(0) O(n)