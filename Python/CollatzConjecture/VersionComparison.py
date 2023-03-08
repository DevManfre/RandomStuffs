from CollatzConjecture import CollatzConjecture
from CollatzConjectureDictOptimizated import CollatzConjectureDictOptimizated

import os

def compareVersion():
    def getPercentImprove(obj1 : CollatzConjecture, obj2 : CollatzConjecture):
        value = (obj1.elapsedTime-obj2.elapsedTime)/(obj1.elapsedTime+obj2.elapsedTime)
        
        return abs(round(value * 100, 3))
    
    os.system("clear")

    start, end = 1, 100001
    versions = {
        "Base": CollatzConjecture(start, end),
        "Dict": CollatzConjectureDictOptimizated(start, end)
    }

    print("Execution time:")
    for k in versions.keys():
        print(f"\t{k} version \t\t {versions[k].elapsedTime}s")
    print()

    print(f"\nOptimization:")
    for k in versions.keys():
        if versions[k] == versions["Base"]:
            optimization = getPercentImprove(versions["Base"], versions[k])
            if int(optimization) == 0:
                continue
            print(f"\t{k} - Base\t\t{optimization}%")
        else:
            print(f"{k} and base aren't equals...")
    print()

compareVersion()
