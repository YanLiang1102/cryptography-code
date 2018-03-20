import sys
import os
import pickle
from sage.all import *
class Stack():
    def __init__(self):
        self.__storage = []
    def isEmpty(self):
        return len(self.__storage) == 0
    def push(self,p):
        self.__storage.append(p)
    def pop(self):
        return self.__storage.pop()
def exploreTheBestResult(bestfilename):
    data=pickle.load(open(bestfilename,"rb"))
    print(data["globalbest"]);
    print(data["solutioncount"]);

def main():
    bestfilename=sys.argv[1]
    exploreTheBestResult(bestfilename);
if __name__ == "__main__":
    main()
