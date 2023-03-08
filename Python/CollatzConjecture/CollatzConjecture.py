import time

class CollatzConjecture:
    def __init__ (self, *args):
        # Case: 1 int param
        if len(args) == 1 and type(args[0]) is int:
            self.n = args[0]
            start = time.time()
            self.sequence = self._getSequence(self.n)
            end = time.time()
            self.elapsedTime = end - start
        # Case: 2 int param
        elif len(args) == 2 and type(args[0]) is type(args[1]) is int:
            start = time.time()
            self.sequence = {x : self._getSequence(x) for x in range(args[0], args[1])}
            end = time.time()
            self.elapsedTime = end - start
        # Case: 1 list or tuple param
        elif len(args) ==1 and type(args[0]) is tuple or type(args[0]) is list:
            start = time.time()
            self.sequence = {x : self._getSequence(x) for x in range(args[0][0], args[0][1])}
            end = time.time()
            self.elapsedTime = end - start

    def _getSequence(self, n : int) -> list:
        if n == 1:
            return [1]
        elif self._isPair(n):
            return [n] + self._getSequence(int(n/2))
        return [n] + self._getSequence(int(3*n+1))
    
    def _isPair(self, n : int) -> bool:
        if n % 2 == 0:
            return True
        return False
    
    def __str__(self) -> str:
        try:
            type(self.n)
            return f"{self.n} -> {str(self.sequence)}"
        except Exception:
            string = ""
            for k in self.sequence.keys():
                string += f"{k} -> {self.sequence[k]}\n"
            return string[:len(string)-1]

    def fullDescription(self):
        return f"{self.__str__()}\nElapsed time = {self.elapsedTime}"