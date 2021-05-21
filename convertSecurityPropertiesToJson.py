#!/usr/bin/python
import time
import re

def converttoJson():
    filepath = 'C:\\Users\\Bavly.Morcos\\Desktop\\test.txt'
    couts = '"'
    first_line = ""
    last_line = ""
    with open(filepath) as fp:
        lines = fp.read().splitlines()
        first_line = fp.readline()
        for last_line in fp:
            pass
    with open(filepath, "w") as fp:
        print("{" + first_line , file=fp)
        for line in lines:
            if len(line.strip()) == 0 :
                pass
            else:
                print(couts + line.replace( '=' , '":"' , 1) + couts + ",", file=fp)
        
        print(last_line + "}" , file=fp)

converttoJson();