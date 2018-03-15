# -*- coding: utf-8 -*-
import os
import json

poemPath = "./poem/"
poems = os.listdir(poemPath)
poemName = "poet.tang.0.json"

# process Json
with open(poemPath + poemName,) as poem:
    p = json.load(poem)
    paragraphs = p[0]["paragraphs"]#TODO first poem in poemTang
    paragraphs1 = paragraphs[0].encode("utf-8")
    poem = ""
    for i in paragraphs:
        poem += i.encode("utf-8")
    
