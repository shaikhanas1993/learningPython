def divide(x,y):
    try:
        result = x/y/z
    except ZeroDivisionError as e:
        print "Found Exception"
    else:
        #result = 1
        print result
    finally:
        print "Finally"

divide(10,10)
print "tantana"

# try:
#     #raise KeyboardInterrupt
#     print "sdad"
# finally:
#     print "Hello,World!"