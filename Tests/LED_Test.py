'''
Created on 1 Mar 2018

@author: Amy
'''

from LED_Display.main import *
import pytest

def testGrid():
    big = ledDisplay(2)
    assert big.gridSize() == 4
    assert big.count() == 0

def testSwitch():
    grid = ledDisplay(5)
    grid.switch(1, 1, 3, 3)
    grid.switch(1, 2, 4, 4)
    assert grid.count() == 9

def testTurnOn():
    grid = ledDisplay(5)
    grid.turnOn(2, 2, 4, 4)
    grid.turnOn(3, 4 , 4, 3)
    grid.turnOn(1, 1, 2, 2)
    assert grid.count() == 12

def testTurnOff():
    grid = ledDisplay(6)
    grid.turnOn(0, 0, 5, 5)
    grid.turnOff(0, 2, 5, 4)
    grid.turnOff(1, 2, 5, 3)
    grid.turnOff(0, 1, 0, 4)
    assert grid.count() == 17

def testApply():
    grid = ledDisplay(10)
    string = "switcy 6,8 through 2,9"
    grid.apply(string)
    
    string2 = "switch 6,8 through 9,9"
    grid.apply(string2)
    
    string3 = "turn on 1,1 through 3,4"
    grid.apply(string3)
    
    string3 = "turnb off 1,1 through 3,4"
    grid.apply(string3)
    
    assert grid.count() == 20
    
def testParse():
    assert parseFile('ttestfile.txt') == False
    assert parseFile("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")[:1] == ['1000'] 

def testRange():
    grid = ledDisplay(10)
    assert grid.checkRange(11) == 9
    assert grid.checkRange(5) == 5
    assert grid.checkRange(-2) == 0

if __name__ == '__main__':
    testGrid()
    testSwitch()
    testTurnOn()
    testTurnOff()
    testApply()
    testParse()
    testRange()