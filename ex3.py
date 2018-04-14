class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)


raise MyError('oops!')















# class MyError(Exception):
#     def __init__(self,value):
#         #print dir(self)
#         # print self
#         self.value = value
#     def __str__(self):
#         print dir(self)
#         return str(self.value)

# try:
#     raise MyError(2*2)
# except MyError as e:
#     e
    

