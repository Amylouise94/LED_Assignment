'''
Created on 1 Mar 2018

@author: Amy
'''

import numpy as np
import urllib.request
import re
import os

def parseFile(filename):
    if filename.startswith('http'):
        
        req = urllib.request.urlopen(filename)
        buffer = req.read().decode('utf-8')
        file = (buffer.split('\n'))
       
        return file
        
    else:    
        if not os.path.isfile(filename):
            print(filename,"does not exist")
        
        else:
            file = open(filename, 'r')
            if file is not None:
                return file
        

class ledDisplay():
    '''
    classdocs
    '''
    
    lights = None
    size = 0

    def __init__(self, size):
        self.size = size
        self.lights = [[False]*size for i in range(size)]
    
    
    def lineSize(self):
        return self.size
    
    
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
        
        x1 = self.checkRange(startRow)
        y1 = self.checkRange(startColumn)
        x2 = self.checkRange(stopRow)
        y2 = self.checkRange(stopColumn)
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if self.lights[i][j] == False:
                    self.lights[i][j] = True
                else:
                    self.lights[i][j] = False
    
    
    def turnOn(self, startRow, startColumn, stopRow, stopColumn):
        
        startRow, startColumn, stopRow, stopColumn = int(startRow), int(startColumn), int(stopRow), int(stopColumn)
       
        x1 = self.checkRange(startRow)
        y1 = self.checkRange(startColumn)
        x2 = self.checkRange(stopRow)
        y2 = self.checkRange(stopColumn)
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                self.lights[i][j] = True
    
    
    def turnOff(self, startRow, startColumn, stopRow, stopColumn):
        
        startRow, startColumn, stopRow, stopColumn = int(startRow), int(startColumn), int(stopRow), int(stopColumn)
       
        x1 = self.checkRange(startRow)
        y1 = self.checkRange(startColumn)
        x2 = self.checkRange(stopRow)
        y2 = self.checkRange(stopColumn)
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                self.lights[i][j] = False
    
    
    def checkRange(self, num):
        
        size = self.lineSize()
        
        if 0 <= num < size:
            return num
        
        elif 0 > num:
            return 0
        
        else:
            ans = size -1
            return ans
    