def divide(x,y):
    try:
        result = x/y
    except Exception:
        print "Found exception"
    else:
        print result
    finally:
        print "End"

divide(10,0)

divide("0",0)
divide(1,1)