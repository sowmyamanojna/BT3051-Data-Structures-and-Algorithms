class ComplexNumber:
    def __init__ (self,r,i):
        self._real = r
        self._imag = i
        print("__init__:", __name__)

    def __repr__(self):
        string = ""
        string += str(self._real) + "+i" + str(self._imag)
        print("repr function: ", __name__)
        
        return string

print("CNF:", __name__)
print(1+2)