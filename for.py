myList = [12,'a','s',[1,2,3]]
for item in myList:
    # if type(item) is int:
    #     print "Found int"
    # elif type(item) is str:
    #     print "Found str"
    # elif type(item) is list:
    #     print "Found List"
    if type(item) is list:
        for innerItem in item:
            print innerItem
    else:
        #print "inside else"
        print item


