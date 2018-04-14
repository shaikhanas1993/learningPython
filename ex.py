# while True:
#     try:
#         x = 1/q
#         print x
#         break
#     except (ZeroDivisionError,TypeError,ValueError,NameError) as e:
#         print "Error Occured",e
#         break

# import sys
# print sys.exc_info()


import sys
try:
    f = open('/home/anas/Code/python/learningPython/Readme')
    s = f.readline()
    i  = int(s.strip())/0
    print i
    #print sys.exc_info()[0]
except IOError as e:
    print 'sad', e
except ValueError as e:
    print "dad", e
except:
    print sys.exc_info()
    print "Unexpected Error",sys.exc_info()[0]
    raise