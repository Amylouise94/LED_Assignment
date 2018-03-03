'''
Created on 2 Mar 2018

@author: HP
'''

from main import *

def getGridSize(filename):
    
    with open(filename) as f:
        line = f.readline()
    line = int(line)
    
    displayLED(line, filename)

def displayLED(N, filename):
    
    light = ledDisplay(N)
    
    instructions = parseFile(filename)
    
    for cmd in instructions:
        light.apply(cmd)
    
    light.count()
    
if __name__ == '__main__':
    getGridSize('testfile.txt')