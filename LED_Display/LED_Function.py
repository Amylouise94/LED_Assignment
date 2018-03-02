'''
Created on 2 Mar 2018

@author: HP
'''

from main import *

def displayLED(N, filename):
    
    light = ledDisplay(N)
    
    instructions = parseFile(filename)
    #print(instructions)
    
    for cmd in instructions:
        light.apply(cmd)
    
    light.count()
    
if __name__ == '__main__':
    displayLED(6, 'testfile.txt')