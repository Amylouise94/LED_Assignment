'''
Created on 1 Mar 2018

@author: HP
'''

import numpy as np
import requests
import re
import os

def parseFile(input):
    if input.startswith('http'):
        req = requests.get(input).text
        if req is not None:
            return True
        else:
            return False
        
    else:    
        if not os.path.isfile(input):
            return False
            #print(input,"does not exist")
        else:
            file = open(input, 'r')
            if file is not None:
                for line in file.readlines():
                    return line
                
            file.close()
parseFile('testfile.txt')
parseFile("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
      
def regEx(line):
    pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    m = pat.match(line)     
    if m is not None:
        return True
    else:
        return False
    

class ledDisplay():
    '''
    classdocs
    '''
    
    lights = None

    def __init__(self, size):
        self.size = size
        self.lights = [[False]*size for i in range(size)]
    
    def gridSize(self):
        return self.size
        
    def grid(self):
        return self.lights
    
    def count(self):
        self.count = np.sum(self.lights)
        return self.count
    
    def switch(self, startRow, startColumn, stopRow, stopColumn):
        
        for i in range(startRow, stopRow+1):
            for j in range(startColumn, stopColumn+1):
                if self.lights[i][j] == False:
                    self.lights[i][j] = True
                else:
                    self.lights[i][j] = False
    
    def turnOn(self, startRow, startColumn, stopRow, stopColumn):
        for i in range(startRow, stopRow+1):
            for j in range(startColumn, stopColumn+1):
                self.lights[i][j] = True
    
    def turnOff(self, startRow, startColumn, stopRow, stopColumn):
        for i in range(startRow, stopRow+1):
            for j in range(startColumn, stopColumn+1):
                self.lights[i][j] = False
    