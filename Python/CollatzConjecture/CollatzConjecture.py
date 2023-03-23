import time
import sys

class CollatzConjecture:
    def __init__ (self, *args):
        self.elapsedTime = time.time()

        self.sequence = {
            1:[1]
        }

        # Case: 1 int param
        if len(args) == 1 and type(args[0]) is int:
            self.n = args[0]
            self.sequence = self._getSequence(self.n)
        # Case: 2 int param
        elif len(args) == 2 and type(args[0]) is type(args[1]) is int:
            self.sequence = {x : self._getSequence(x) for x in range(args[0], args[1])}
        # Case: 1 list or tuple param
        elif len(args) ==1 and type(args[0]) is tuple or type(args[0]) is list:
            self.sequence = {x : self._getSequence(x) for x in range(args[0][0], args[0][1])}
        
        self.elapsedTime = time.time() - self.elapsedTime

    def generator(self):
        if type(self.sequence) is list:
            # if there is only one sequence
            return self.sequence
        elif type(self.sequence) is dict:
            for key in self.sequence.keys():
                for n in self.sequence[key]:
                    yield n
        
    def _getSequence(self, n : int) -> list:
        if n in self.sequence.keys():
            return self.sequence[n]
        elif self._isPair(n):
            self.sequence[n] = [n] + self._getSequence(int(n/2))
        else:
            self.sequence[n] = [n] + self._getSequence(int(3*n+1))
        
        return self.sequence[n]
    
    def _isPair(self, n : int) -> bool:
        if n % 2 == 0:
            return True
        return False
    
    def fullDescription(self) -> None:
        return f"{self.__str__()}\nElapsed time = {self.elapsedTime}"

    def __str__(self) -> str:
        try:
            type(self.n)
            return f"{self.n} -> {str(self.sequence)}"
        except Exception:
            string = ""
            for k in self.sequence.keys():
                string += f"{k} -> {self.sequence[k]}\n"
            return string[:len(string)-1]

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, CollatzConjecture):
            if type(self.sequence) == type(__o.sequence) == list or type(self.sequence) == type(__o.sequence) == dict:
                return self.sequence == __o.sequence
        
        return False
    
    def __sizeof__(self) -> int:
        elements = [
            self.elapsedTime,
            self.sequence
        ]

        try:
            elements.append(self.n)
        except Exception:
            pass

        return sum([sys.getsizeof(el) for el in elements])