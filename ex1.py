import sys
for arg in sys.argv[1:]:
    print arg
    try:
        f = open(arg,'r')
    except IOError as e:
        print "Cannot Open",e
    else:
        print f.read()
        # f.close()
    