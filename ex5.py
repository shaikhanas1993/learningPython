class MyError(Exception):
    def __init__(self):
        self.message = 'It is My Error'
    def __str__(self):
        return repr(self.message)

try:
    raise MyError()
except MyError as e:
    print e.message


