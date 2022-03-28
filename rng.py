class PseudoRNG:
    
    def __init__(self,a,c,val,m = 2147483647):
        self.m = m
        self.a = a
        self.c = c
        self.val = val

    def nextInt(self):
        """
        computes the next integer in the sequence and stores it in self.val
        """
        self.val = (self.a * self.val + self.c) % self.m
    
    def randInt(self,inf,sup):
        """
        @param inf int
        @param sup int
        @return a random integer between inf (included) and sup (excluded)
        should modify self.val also
        """
        self.nextInt()
        return inf + (self.val % (sup - inf))

