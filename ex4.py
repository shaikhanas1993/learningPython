class Error(Exception):
    pass

class InputError(Error):
    def __init__(self,expr,msg):
        self.expre = expr
        self.msg = msg
    def __str__(self):
        return repr(self.expre),repr(self.msg)

class TransitionError(Error):
    def __init__(self,prev,next,msg):
        self.prev = prev
        self.next = next
        self.msg = msg
    
    def __str__(self):
        return repr(self.msg)


raise InputError('','sdad')