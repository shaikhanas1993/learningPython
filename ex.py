while True:
    try:
        x = 1/q
        print x
        break
    except (ZeroDivisionError,TypeError,ValueError,NameError) as e:
        print "Error Occured",e
        break