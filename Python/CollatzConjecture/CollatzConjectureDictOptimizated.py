from CollatzConjecture import CollatzConjecture
import sys

class CollatzConjectureDictOptimizated(CollatzConjecture):
    def __init__ (self, *args):
        self.optimization = {
            1:[1]
        }
        
        super().__init__(args)

    def _getSequence(self, n : int) -> list:
        if n in self.optimization.keys():
            return self.optimization[n]
        elif self._isPair(n):
            self.optimization[n] = [n] + self._getSequence(int(n/2))
        else:
            self.optimization[n] = [n] + self._getSequence(int(3*n+1))
        
        return self.optimization[n]
    
    def __sizeof__(self) -> int:
        return super().__sizeof__() + sys.getsizeof(self.optimization)