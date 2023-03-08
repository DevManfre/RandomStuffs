from CollatzConjecture import CollatzConjecture
from CollatzConjectureDictOptimizated import CollatzConjectureDictOptimizated

import os
import sys

def compareVersion():
    def getPercentTimeImprove(obj1 : CollatzConjecture, obj2 : CollatzConjecture):
        value = (obj1.elapsedTime-obj2.elapsedTime)/(obj1.elapsedTime)
        
        return round(value * 100, 3)
    
    def getPercentSpaceImprove(obj1 : CollatzConjecture, obj2 : CollatzConjecture):
        value = (sys.getsizeof(obj1)-sys.getsizeof(obj2))/(sys.getsizeof(obj1))
        
        return round(value * 100, 3)

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

    print(f"Memory Occupation:")
    for k in versions.keys():
        if versions[k] == versions["Base"]:
            ris = round(sys.getsizeof(versions[k])/1024/1024, 3)
            print(f"\t{k} version\t\t{ris}Mb")
        else:
            print(f"{k} and base aren't equals...")
    print()

    print(f"Optimization:")
    for k in versions.keys():
        if versions[k] == versions["Base"]:
            timeOptimization = getPercentTimeImprove(versions["Base"], versions[k])
            spaceOptimization = getPercentSpaceImprove(versions["Base"], versions[k])
            if int(timeOptimization) == 0:
                continue
            print(f"\t{k} - Base\t\tTime percent = {timeOptimization}%\t\tSpace percent = {spaceOptimization}%")
        else:
            print(f"{k} and base aren't equals...")
    print()

compareVersion()