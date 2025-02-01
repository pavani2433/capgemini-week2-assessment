class Logger:
    def log(self,*args):
        if len(args)==3:
            print("info")
        elif len(args)==2:
            print("warning")
        elif len(args)==1:
            print("Error")
        else:
            print("Give atleast one argument")
l=Logger()
l.log("Hi")
l.log("Hi","Hello")
l.log("Hi","Hello","Welcome")
l.log()