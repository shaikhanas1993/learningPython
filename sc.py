def outer_function():
    global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =',id(a))

    inner_function()
    print('a =',id(a))
     
a = 10
outer_function()
print('a =',id(a))