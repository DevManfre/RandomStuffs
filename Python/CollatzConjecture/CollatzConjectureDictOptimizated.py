from CollatzConjecture import CollatzConjecture

class CollatzConjectureDictOptimizated(CollatzConjecture):
    def __init__ (self, *args):
        self.sequence = {
            1:[1]
        }
        
        super().__init__(args)

    def _getSequence(self, n : int) -> list:
        if n in self.sequence.keys():
            return self.sequence[n]
        elif self._isPair(n):
            self.sequence[n] = [n] + self._getSequence(int(n/2))
        else:
            self.sequence[n] = [n] + self._getSequence(int(3*n+1))
        
        return self.sequence[n]
