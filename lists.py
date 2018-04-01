# from collections import deque
# queue = deque([1,2,3,4,5])
# #print queue

# queue.appendleft('sdad')
# #print queue
# queue.popleft()
# print queue 


from collections import deque
queue = deque([1,2,3,4,5])
print queue

queue.popleft()
print queue
queue.pop()
print queue

print queue[0]