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
        #if req is not None:
        #    return True
        #else:
        #    return False
        
    else:    
        if not os.path.isfile(input):
            #return False
            print(input,"does not exist")
        else:
            file = open(input, 'r')
            if file is not None:
                return file
        

class ledDisplay():
    '''
    classdocs
    '''
    
    lights = None

    def __init__(self, size):
        self.size = size
        self.lights = [[False]*size for i in range(size)]
    
    def gridSize(self):
        return self.size*self.size
        
    def grid(self):
        return self.lights
    
    def count(self):
        self.count = np.sum(self.lights)
        on = self.count
        off = self.size*self.size - self.count
        print('There are', on, "lights on and", off,'lights off')
        return self.count
    
    def apply(self, cmd):
        
        pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        m = pat.match(cmd)
        if m is not None:
            if m.group(1) == 'switch':
                self.switch(m.group(2), m.group(3), m.group(4), m.group(5))
            elif m.group(1) == 'turn on':
                self.turnOn(m.group(2), m.group(3), m.group(4), m.group(5))
            elif m.group(1) == 'turn off':
                self.turnOff(m.group(2), m.group(3), m.group(4), m.group(5))
            else:
                pass
    
    
    def switch(self, startRow, startColumn, stopRow, stopColumn):
        
        startRow, startColumn, stopRow, stopColumn = int(startRow), int(startColumn), int(stopRow), int(stopColumn)
        
        self.checkRange(startRow)
        self.checkRange(startColumn)
        self.checkRange(stopRow)
        self.checkRange(stopColumn)
        
        for i in range(startRow, stopRow+1):
            for j in range(startColumn, stopColumn+1):
                if self.lights[i][j] == False:
                    self.lights[i][j] = True
                else:
                    self.lights[i][j] = False
    
    def turnOn(self, startRow, startColumn, stopRow, stopColumn):
        
        startRow, startColumn, stopRow, stopColumn = int(startRow), int(startColumn), int(stopRow), int(stopColumn)
       
        self.checkRange(startRow)
        self.checkRange(startColumn)
        self.checkRange(stopRow)
        self.checkRange(stopColumn)
       
        for i in range(startRow, stopRow+1):
            for j in range(startColumn, stopColumn+1):
                self.lights[i][j] = True
    
    def turnOff(self, startRow, startColumn, stopRow, stopColumn):
        
        startRow, startColumn, stopRow, stopColumn = int(startRow), int(startColumn), int(stopRow), int(stopColumn)
       
        self.checkRange(startRow)
        self.checkRange(startColumn)
        self.checkRange(stopRow)
        self.checkRange(stopColumn)
        
        for i in range(startRow, stopRow+1):
            for j in range(startColumn, stopColumn+1):
                self.lights[i][j] = False
    
    def checkRange(self, num):
        if 0 <= num < self.gridSize():
            return num
        
        elif 0 > num:
            return 0
        
        else:
            ans = self.gridSize() -1
            return ans
    