'''
Created on 1 Mar 2018

@author: HP
'''

import numpy as np

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
    
    def switch(self, startRow, startColumn, stopColumn, stopRow):
        
        for i in range(startRow, stopRow):
            for j in range(startColumn, stopColumn):
                if self.lights[i][j] == False:
                    self.lights[i][j] = True
                else:
                    self.lights[i][j] = False
    
    def turnOn(self, startRow, startColumn, stopColumn, stopRow):
        for i in range(startRow, stopRow):
            for j in range(startColumn, stopColumn):
                self.lights[i][j] = True
    
    def turnOff(self, startRow, startColumn, stopColumn, stopRow):
        for i in range(startRow, stopRow):
            for j in range(startColumn, stopColumn):
                self.lights[i][j] = False
    