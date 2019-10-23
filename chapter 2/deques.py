from collections import deque

dq = deque(range(100),maxlen=10)
print(dq)
# deque([90, 91, 92, 93, 94, 95, 96, 97, 98, 99], maxlen=10)

dq.rotate(3)
print(dq)
# deque([97, 98, 99, 90, 91, 92, 93, 94, 95, 96], maxlen=10)

dq.rotate(-4)
print(dq)
# deque([91, 92, 93, 94, 95, 96, 97, 98, 99, 90], maxlen=10)

dq.appendleft(-1)
print(dq)
# deque([-1, 91, 92, 93, 94, 95, 96, 97, 98, 99], maxlen=10)

dq.append(1)
print(dq)
# deque([91, 92, 93, 94, 95, 96, 97, 98, 99, 1], maxlen=10)

dq.extendleft([-1])
print(dq)
# deque([-1, 91, 92, 93, 94, 95, 96, 97, 98, 99], maxlen=10)

dq.extend([1])
print(dq)
# deque([91, 92, 93, 94, 95, 96, 97, 98, 99, 1], maxlen=10) 


