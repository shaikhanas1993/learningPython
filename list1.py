matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print zip(*matrix)


#Amazing one liner
#print [[row[i] for row in matrix] for i in range(4)]

#other way
# transposed_list = []
# for i in range(4):
#     transposed_list.append([row[i] for row in matrix])
# print transposed_list



##print [[row[i] for row in matrix] for i in range(4)]


#amazing one liners
#print [[row[i] for row in matrix] for i in range(4)]


#print matrix
#print [[row[i] for row in matrix] for i in range(4)]
#print [ for i in range(4)]
# lists = []
# for i in range(4):
#     innerList = []
#     for row in matrix:
#         innerList.append(row[i])
#     lists.append(innerList)
# print lists

# list = []
# for row in matrix:
#     innerList = []
#     for i in range(4):
#         innerList.append(row[i])
#     list.append(innerList)
# print list

