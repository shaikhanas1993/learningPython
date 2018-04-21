def func():
    def do_local():
        spam = "this is local"
        print(id(spam))
    def do_nonlocal():
        nonlocal spam
        spam = "this is non local"
        print(id(spam))
    def jar_local():
        global spam
        spam = "this is global spam"
        print(id(spam))
    
    spam = "test"
    print(id(spam))
    do_local()
    print("After do_local",spam)
    do_nonlocal()
    print("After non local",spam)
    jar_local()
    print("After jar local",spam)


func()
print(spam)
print(id(spam)) 