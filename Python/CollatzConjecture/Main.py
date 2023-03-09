from CollatzConjecture import CollatzConjecture
from CollatzConjectureDictOptimizated import CollatzConjectureDictOptimizated

import os
import sys

class VersionComparison:
    def __init__(self, start, end):
        self.versions = {
            "Base": CollatzConjecture(start, end),
            "Dict": CollatzConjectureDictOptimizated(start, end),
        }
    
    def getPercentTimeImprove(obj1 : CollatzConjecture, obj2 : CollatzConjecture):
        value = (obj1.elapsedTime-obj2.elapsedTime)/(obj1.elapsedTime)
        
        return round(value * 100, 3)
    
    def getPercentSpaceImprove(obj1 : CollatzConjecture, obj2 : CollatzConjecture):
        value = (sys.getsizeof(obj1)-sys.getsizeof(obj2))/(sys.getsizeof(obj1))
        
        return round(value * 100, 3)
    
    def getPerformance(self):
        os.system("clear")

        print("Execution time:")
        for k in self.versions.keys():
            print(f"\t{k} version \t\t {self.versions[k].elapsedTime}s")
        print()

        print(f"Memory Occupation:")
        for k in self.versions.keys():
            if self.versions[k] == self.versions["Base"]:
                ris = round(sys.getsizeof(self.versions[k])/1024/1024, 3)
                print(f"\t{k} version\t\t{ris}Mb")
            else:
                print(f"{k} and base aren't equals...")
        print()

        print(f"Optimization:")
        for k in self.versions.keys():
            if self.versions[k] == self.versions["Base"]:
                timeOptimization = VersionComparison.getPercentTimeImprove(self.versions["Base"], self.versions[k])
                spaceOptimization = VersionComparison.getPercentSpaceImprove(self.versions["Base"], self.versions[k])
                
                if int(timeOptimization) == 0:
                    continue
                print(f"\t{k} - Base\t\tTime percent = {timeOptimization}%\t\tSpace percent = {spaceOptimization}%")
            else:
                print(f"{k} and base aren't equals...")
        print()

if __name__ == "__main__":
    VersionComparison(1, 100001).getPerformance()