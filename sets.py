mylist = ['apple','apple','banana']
a = set(mylist)
#converting set to list to retrieve value
# back_to_list = list(set_of_list)
# del set_of_list
# print back_to_list[0]

b = set(['jason','banana'])
print a - b #there in a but not in b 
print b-a # remove everything  a has,leaving only b's element that are not present in a

print a & b # intersection that is both a & b have

print a | b # union operation

print a ^ b #remove common elements between a & b

