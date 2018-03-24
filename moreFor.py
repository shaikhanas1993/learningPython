"""/
   This example goes deep inside for loop/
   Lists are mutable unlike str which are immutable
   you can multiple references of same list by assigning to several variables

   For inserting while iterating in a list, make use of slice which creates 
   the entire of the list 

""" 

words = ['cat', 'window', 'defenestrate','dadadadadadad']
copied = words #both are exactly point to the same object


# for w in words:
#     print w,len(w)
#i=0
# for w in copied[:]:
#     if len(w)>6:
#         copied.insert(0,w)
   
# print words
# if type(copied) is list:
#     print "hwllo world!!"
# words.append("hello")

# words[0] = "changes"
# del copied[1]
# print "===================="
# for w in copied:
#     print w 
# print "===================="
# for w in words:
#     print w 

#sliced version of iteration of a list while performing insertion within the list
#Lesson Learned :: always use a slice version of iteration over list
for w in words[:]:
    
    if len(w)>6:
        print w
        words.insert(0,w)
print "=====Words::============="
print words
print "======Copied::==========="
print copied





#copied.append("hello")
#print words