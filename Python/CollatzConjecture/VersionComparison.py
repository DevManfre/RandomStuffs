from CollatzConjecture import CollatzConjecture
from CollatzConjecture_v2_DictOptimizated import CollatzConjecture_v2_DictOptimizated
import os

def compareVersion():
    def getPercentImprove(elapsedTime1, elapsedTime2):
         value = (elapsedTime1.elapsedTime-elapsedTime2.elapsedTime)/(elapsedTime1.elapsedTime+elapsedTime2.elapsedTime)
         percent = abs(round(value * 100, 3))
         return f"{percent}%"
    
    os.system("clear")
        
    # Base Version
    baseCollatz = CollatzConjecture(1, 100001)
    print(f"Exec time base version \t\t {baseCollatz.elapsedTime}")

    # Dict Version
    dictCollatz = CollatzConjecture_v2_DictOptimizated(1, 100001)
    print(f"Exec time dict version \t\t {dictCollatz.elapsedTime}")

    # Percent
    print(f"\nOptimization:")
    print(f"\tbase - dict\t{getPercentImprove(baseCollatz, dictCollatz)}")

compareVersion()