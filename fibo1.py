
def fib(n):
    a,b = 0,1
    while b<n:
        print b
        a,b = b,a+b


def fib2(n):
    a,b=0,1
    result = []
    while b<n:
        result.append(b)
        a,b = b,a+b
    return result

def printHello():
    print "hello world!"

if __name__ == "__main__":
    import sys
    print sys.argv[1]
    printHello()