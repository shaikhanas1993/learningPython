try:
    raise NameError('Hi There')
except NameError:
    print 'hi'
    raise