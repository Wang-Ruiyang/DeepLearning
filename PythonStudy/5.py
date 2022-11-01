class Displayer:
    def display(self,message):
        print(message)

class LoggerMixin:
    def log(self,message,filename="logfile.txt"):
        with open(filename,"a") as f:
            f.write(message)

    def display(self,message):
        super().display(message)
        self.log(message)

class MySubClass(LoggerMixin,Displayer):
    def log(self,message):
        super().log(message,filename="subclasslog.txt")

subclass = MySubClass()
subclass.display("This is a test.")
