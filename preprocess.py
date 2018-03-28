# -*- coding: utf-8 -*-

import os
import json
import re

# process one poem
def ProcessOne(filePath):
    outfile = filePath.replace("json", "txt")
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
                f.write("\n")

# list folder
def ProcessList(dirPath):
    poems = os.listdir(dirPath + "json")
    for poem in poems:
        poemPath = dirPath + "json/" + poem
        ProcessOne(poemPath)

# a whole file may be convenient for process
def Merge(dirPath):
    poems = os.listdir(dirPath + "txt")
    outfile = dirPath + "allpoems.txt"
    allpoems = open(outfile, "w")
    for poem in poems:
        # print poem
        poemPath = dirPath + "txt/" +poem
        with open(poemPath, "r") as f:
            for line in f:
                allpoems.writelines(line)
            allpoems.write("\n")
    allpoems.close()

if __name__ == '__main__':
    poemDirPath = "./poem/"
    #ProcessList(poemDirPath)
    Merge(poemDirPath)
