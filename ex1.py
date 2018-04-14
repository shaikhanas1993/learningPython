# import sys
# for arg in sys.argv[1:]:
#     print arg
#     try:
#         f = open(arg,'r')
#     except IOError as e:
#         print "Cannot Open",e
#     else:
#         print f.read()
#         # f.close()
    
# try:
#     x = 1/1
#     # print x
# except ZeroDivisionError as e:
#     print e
# else:
#     print x


try:
    raise Exception('spam','eggs')
except Exception as inst:
    print type(inst.args)
    print inst.args[0]

