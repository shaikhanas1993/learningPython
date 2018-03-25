"""
    Break statements break the innner Most loop
    With Break statement,else clause is not run after the iteration got exhausted
"""

#break statement
# for n in range(2,50):
#     for x in range(2,n):
#         if n%x==0:
#             break
#     else:
#         print n

#continue statemennt

# for num in range(2,10):
#     if num%2==0:
#         print "Found an even number::",num
#         continue
#     print num
# 

for num in range(10):
    
    if num%2==0 and num!=0:
        print "Even Number::",num
        continue
    print num
    
# for w in range(10):
#     print w
#     # break
# else:
#     print "else"    
    


# for n in range(2,10):
#     print "n==",n
#     for x in range(2,n):
#         print "n===",n
#         print "x===",x
#         if n%x==0:
#             print n,'equals',x,'*',n/x
#             break
#     else:
#         print n

#program to search for prime numbers
# for n in range(2,10):
#     for x in range(2,n):
#         if n%x==0:
#             print n,'=',x,n/x
#             break
#     else:
#         print n


# for n in range(2,10):
#     for x  in range(2,n):
#         if n%x==0:
#             break
#     else:
#         print n  
# 

# for n in range(2,100):
#     for x in range(2,n):
#         if n%x==0:
#             break
#     else:
#         print n



      