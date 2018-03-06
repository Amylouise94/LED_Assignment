'''
Created on 2 Mar 2018

@author: Amy
'''

from main import *
import urllib.request
import click

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    
    print("input", input)
    
    if input.startswith('http'):
        
        req = urllib.request.urlopen(input)
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
        with open(input) as f:
            line = f.readline()
        line = int(line)
    
    
    displayLED(line, input)


def displayLED(N, filename):
    
    light = ledDisplay(N)
    
    instructions = parseFile(filename)
    
    for cmd in instructions:
        
        light.apply(cmd)
        
    light.count()
    
    
if __name__ == '__main__':
    main()