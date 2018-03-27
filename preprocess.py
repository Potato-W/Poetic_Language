# -*- coding: utf-8 -*-

import os
import json
import re

dirPath = "./poem/"

# process one poem
def ProcessOne(filePath):
    outfile = filePath.replace("json", "txt")
    #outfile = outfile[:-4] + ".txt"#TODO
    with open(filePath) as p:
        poems = json.load(p)
        for poetic in poems:
            poemPara = poetic["paragraphs"]
            poem = ""
            for i in poemPara:
                poem += i.encode("utf-8")
            # poem = poem.replace("，", "")
            # poem = poem.replace("。", "")
            poem = re.sub("，|。|？|（|）|【|】|{|}|《|》|-|“|”|！|：|□|〖|〗|[0-9]|[|]","",poem)
            with open(outfile, 'a') as f:
                f.write(poem)
                f.write('\n')

# list folder
def ProcessList(dirPath):
    poems = os.listdir(dirPath + "json")
    for poem in poems:
        poemPath = dirPath + "json/" + poem
        ProcessOne(poemPath)

# a whole file may be convenient for process
# def Merge(dirPath):

if __name__ == '__main__':
    ProcessList(dirPath)
