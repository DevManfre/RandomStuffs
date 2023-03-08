import time
from CollatzConjecture import CollatzConjecture

class CollatzConjectureDictOptimizated(CollatzConjecture):
    def __init__ (self, *args):
        self.optimization = {1:[1]}

        # Case: 1 int param
        if len(args) == 1 and type(args[0]) is int:
            self.n = args[0]
            start = time.time()
            self.sequence = self.__getSequence(self.n)
            end = time.time()
            self.elapsedTime = end - start
        # Case: 2 int param
        elif len(args) == 2 and type(args[0]) is type(args[1]) is int:
            start = time.time()
            self.sequence = {x : self.__getSequence(x) for x in range(args[0], args[1])}
            end = time.time()
            self.elapsedTime = end - start
        # Case: 1 list or tuple param
        elif len(args) ==1 and type(args[0]) is tuple or type(args[0]) is list:
            start = time.time()
            self.sequence = {x : self.__getSequence(x) for x in range(args[0][0], args[0][1])}
            end = time.time()
            self.elapsedTime = end - start

    def __getSequence(self, n : int) -> list:
        if n in self.optimization.keys():
            return self.optimization[n]
        elif CollatzConjectureDictOptimizated.__isPair(n):
            self.optimization[n] = [n] + self.__getSequence(int(n/2))
        else:
            self.optimization[n] = [n] + self.__getSequence(int(3*n+1))
        
        return self.optimization[n]
    
    def __isPair(n : int) -> bool:
        if n % 2 == 0:
            return True
        return False

