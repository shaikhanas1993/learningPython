
# from math import pi
# print [str(round(pi,x)) for x in range(10)]

# print str([1,2,3,4])


# from math import pi
# print [str(round(pi,i)) for i in range(1,6)]


#amazing one liners

# print [(x,y) for x in range(5) for y in range(10) if x!=y]
# #equivalence

# coms = []
# for x in range(5):
#     for y in range(10):
#         if x!=y:
#             coms.append((x,y))


# print coms

#print [(x,y) for x in [1,2,3] for y in [3,4,5] if x!=y]

# _ = [(x,y) for x in [1,2] for y in [1,4] if x!=y]

# print _[0][1]


# print [x**2 for x in range(0,11)]

#squares = map(lambda x:x**2,range(11))
#print squares


# squares = []
# for x in range(0,11):
#     squares.append(x**2)
# print squares

#print [x**2 for x in range(11)]




# print sum([1,2,3,4,5,6],10)


# def sum(seq):
#     return reduce(lambda x,y:x+y,seq,0)
# print sum([1,2,3])




# def sum(seq):
#     return reduce(lambda x,y:x+y,seq,0)
# print sum([121,123])


# def add(x,y):
#     return x+y
# def sum(seq):
#     return reduce(add,seq,0)

# print sum([1,2,4,5,6,7,6])

# def sum(seq):
#     print seq
#     def add(x,y):
#         print "x===",x
#         print "y===",y
#         return x+y
#     return reduce(add,seq,0)
# print sum(range(1,11))


# def add(x,y):
#     return x+y
# print reduce(add,[1,2,3,4,5,6,7,8,9,10])



#reduce function

# def add(x,y):
#     print "x===",x
#     print "y===",y
#     return x+y
# print reduce(add,[1,2])


# seq = range(8)
# def add(x,y):
#     if type(x)!=None or type(y)!=None:
#         return x + y 
#     else:
#         return 0
    

# print map(add,seq,seq)
#for filter function i must return a boolean
# def f(x):
#     print x
#     if x%3 ==0 or x%5==0:
#         return True

# print filter(f,[1,2,3,4,4,5])
        


#map function

# def cube(x):return x*x*x
# print map(cube,[1,2,3,4,5])

#def f(x): return x%3==0 or x%5==0
#print filter(f,range(2,6))







# def f(x):
#     print x%3==0 or x%5==0
#     return x%3==0 or x%5==0


# print filter(f,(1,2,3,4,5,6))


# def f(x) : return x%3==0 or x % 5==0

# arr = filter(f,range(2,6))
# print arr





# from collections import deque
# queue = deque([1,2,3,4,5])
# #print queue

# queue.appendleft('sdad')
# #print queue
# queue.popleft()
# print queue 

#dequeue
# from collections import deque
# queue = deque([1,2,3,4,5])
# print queue

# queue.popleft()
# print queue
# queue.pop()
# print queue

# print queue[0]