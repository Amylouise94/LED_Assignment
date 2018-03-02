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

def testRegEx():
    string = "switcy 166,675 through 329,961"
    assert regEx(string) == False
    string2 = "switch 166,675 through 329,961"
    assert regEx(string2) == True
    
def testParse():
    assert parseFile('ttestfile.txt') == False
    assert parseFile("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt") == True
    assert parseFile('testfile.txt') == 'This is a testfile'


if __name__ == '__main__':
    testGrid()
    testSwitch()
    testTurnOn()
    testTurnOff()
    testRegEx()
    testParse()