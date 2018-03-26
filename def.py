"""
    Function definition
    *name (Formal Parameter) receives a tuple
    **name (Final Formal Parameter) receives a dictionary
    *name must appear before **name
    lambda's are syntactic sugar for inner functions
"""
# def mySorter(x = None):
#     print x[2]
#     return x

def mysort(x):
    # print x
    return x[1]
pairs = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]
pairs.sort(key=lambda x:x[1])
print pairs

  
    

# student_tuples = [
#         ('john', 'A', 15),
#         ('jane', 'B', 12),
#         ('dave', 'B', 10),
# ]

# student_tuples.sort(key=lambda x:x[2])
# print student_tuples


#Lambda Expressions
# def make_increment(n):
#     return lambda x:x+n
# f =  make_increment(10)
# print f(1)

# def func(n):
#     return lambda a,b:a+b+n

# f = func(10)
# print f(1,1)



#unpacking arguments List


# def func(a,b,c):
#     print "a::",a
#     print "b::",b
#     print "c::",c
# myTuple =  ('asd','bss','css')
# func(*myTuple)


# def func(a,b,c):
#     print "========="
#     print "a ::" + a
#     print "========="
#     print "b ::" + b
#     print "========="
#     print "c ::" + c

# dic = {'a':'a','b':'b','c':'c'}
# func(**dic)


# def test(*args):
#     print args

# test('sadasd','adad','dadad')    

# def shop(*tup,**dic):
#     for item in tup[:]:
#         print item
#     dic = dic.values()  
#     print dic
#     # for key in dic:
#     #     print dic[key]    

# shop("dadad",'sdadada',name='ans',value=10)    


# def cheeseShop(kind,*arg,**keywords):
#     print "================"
#     print arg
#     print "================"
#     print keywords

# cheeseShop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper='Michael Palin',
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")


#keyword arguments
# def test(voltage,action):
#     print "voltage::",voltage
#     print "action::",action

# test(action='take',voltage=10)


# def parrot(voltage,state = 'a stiff',action = 'voom',type = 'Norwegian Blue'):
#     print "----This parror wouldn't",action
#     print "voltage====",voltage

# parrot(voltage="10")



# def test(a,myList = None):
#     if myList is None:
#         myList = []
#     myList.append(a)
#     return myList     
    
# #print test(1)
# print test(2)        


# def test(a,myList = None):
     
#      print myList
#      if myList is None:
#          myList = []
#      myList.append(a)
#      return myList   

# print test(1)
# print test(2)
# print test(3)



# i = 6
# def test(arg = i):
#     return arg

# i = 5
# print test()    


# i = 5

# def test(arg = i):
#     arg = arg + 1
#     return arg

# print test()
# print i

# def g(a,L=[]):
# #    print "L::", L
#     L.append(a)
#     return L

# g(1)
# g(2)
# print g(6)


# i = 5
# def f(arg = i):
#     print arg
# i = 6
# f(i) 

# def ask_ok(prompt,retries=4,complaint="yes or no"):
#     while True:
#         x = raw_input(prompt)
#         if x in ('y','yes'):
#             return True
#         if x in ('n','no'):
#             return False
#         retries = retries - 1
#         if retries<=0:
#             raise IOError("Refused")
#         print complaint
# ask_ok('Do you want to')


# def ask_ok(prompt,retries=4,complaint="yes or no"):
#     while True:
#         x = raw_input(prompt)
#         if x in ('y','yes','ye'):
#             return True
#         if x in ('n','no','nope'):
#             return False
#         retries = retries-1
#         if retries<0:
#             raise IOError("Refused")
#         print complaint

# # ask_ok('Do You')
# ask_ok('Do You',2,'cancel')        
            


# str = "dsadada"
# if 'a' in str:
#     print "hello world"

# list = ['s','a']

# if 'a' in list:
#     print "Gone  case"



# def fib(n):
#     result = []
#     a,b = 0,1
#     while b<n:
#         result.append(b)
#         a,b = b,a+b
#     return result

# resCall = fib(1000)
# print resCall

# def ask_ok(prompt,retries=4,complaint="yes or no please!!"):
#     while True:
#         ok = raw_input(prompt)
#         if ok in ('y','ye','yes'):
#             return True
#         if ok in ('n','no','nope'):
#             return False
#         retries = retries - 1
#         if  retries<0:
#             raise IOError('refuse error')
#         print complaint

# ask_ok('Enter:::')


# def add_two_no(a=10,b=20):
#     return a+b

# print  add_two_no()




# def fibonacci(n):
#     """ Program to calculate fibonacci series"""
#     result = []
#     a,b = 0,1
#     while b<n:
#         result.append(b)
#         a,b = b,a+b
#     return result

# print fibonacci(2000)


#0112358


# def fibonacci(n):
#     result  = []
#     a,b = 0,1
#     while b<n:
#         result.append(b)
#         a,b = b,a+b
#     return result

# f = fibonacci(200)

# print f    





# def fib(n):
#     result = []
#     a,b = 0,1
#     while a<n:i
#         print a
#         result.append(a)
#         a,b = b,a+b
#     return result

# print fib(1000)






# """Learning Functions in Python"""
# def fib(n):
#     result = []
#     a,b = 0,1
#     while a<n:
#         a = 0

        
   

# fib(100)


# def fib(n):
#     result = []
#     a,b = 0,1
#     while a<n:
#         result.append(a)
#         a,b = b,a+b
#     return result    
# print fib(100)


#print f    



# def fib(n):
#     """ Function to print fibonacci series"""
#     a,b = 0,1
#     while a<n:
#         print a
#         a,b = b,a+b

# fib(100)

# n=100

# def fib(n):
#     n = 20
#     print n

# fib(n)

# def fib1(a):
#     print "fib1",a
#     fib(a=35)


# def fib(a):
#     print "fib",a
#     a =  20
#     fib1(a)
#     print "After call",a

# # print n
# a = 10
# fib(a)




# print "a==",a
