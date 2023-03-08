from CollatzConjecture import CollatzConjecture
from CollatzConjectureDictOptimizated import CollatzConjectureDictOptimizated

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
    dictCollatz = CollatzConjectureDictOptimizated(1, 100001)
    print(f"Exec time dict version \t\t {dictCollatz.elapsedTime}")

    # Percent
    if (baseCollatz == dictCollatz):
        print(f"\nOptimization:")
        print(f"\tdict - base\t{getPercentImprove(baseCollatz, dictCollatz)}")
    else:
        print("The objects aren't equals...")
    print()

compareVersion()