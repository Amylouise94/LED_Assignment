'''
Created on 2 Mar 2018

@author: Amy
'''

from main import *
import urllib.request

def getGridSize(filename):
    
    if filename.startswith('http'):
        
        req = urllib.request.urlopen(filename)
        buffer = req.read().decode('utf-8')
        file = (buffer.split('\n'))
        
        
        line = file[:1]
        
        for i in range(len(line)):
            line[i] = int(line[i])
        
        line = str(line)
        line = line.strip('[')
        line = line.strip(']')
        line = int(line)
    
    else:
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
    getGridSize('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt')