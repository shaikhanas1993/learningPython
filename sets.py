mylist = ['apple','apple','banana']
set_of_list = set(mylist)
#converting set to list to retrieve value
back_to_list = list(set_of_list)
del set_of_list
print back_to_list[0]
