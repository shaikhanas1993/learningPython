def printTest():
    print "test"

def printHello():
    print "hello"    


def addTwoNumbers(a,b):
    return a + b

if __name__ == "__main__":
    import sys
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    printTest()
    printHello()
    print addTwoNumbers(a,b)