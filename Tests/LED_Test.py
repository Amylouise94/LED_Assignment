'''
Created on 1 Mar 2018

@author: HP
'''

from LED_Display.main import *
import pytest

def testGrid():
    big = ledDisplay(2)
    assert big.gridSize() == 2
    assert big.count() == 0
    #print(big.gridSize()) 
    #print(big.grid())
    #print(big.count())

def testSwitch():
    grid = ledDisplay(5)
    grid.switch(1, 1, 3, 3)
    #assert grid.count() == 4
    #print(grid.grid())
    grid.switch(1, 2, 4, 4)
    #print(grid.grid())
    #print(grid.count())
    assert grid.count() == 6

def testTurnOn():
    grid = ledDisplay(5)
    grid.turnOn(2, 2, 5, 5)
    grid.turnOn(3, 4 , 5, 3)
    grid.turnOn(1, 1, 2, 2)
    assert grid.count() == 13

if __name__ == '__main__':
    testGrid()
    testSwitch()