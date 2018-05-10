# coding: UTF-8
import os
import jieba as j
from collections import Counter
import json

class jieba:
    def __init__(self):
        pass

    def PoemSegment(self, poemFile):
        wordList = []
        wordCounter = Counter()
        # with open (poemFile, "r") as f:
        #     for line in f.readlines():
        #         #print line
        #         seg = j.cut(line)
        #         # seg = pseg.cut(line)
        #         #print "/".join(seg)
        #         # for word,flag in seg:
        #         #     # print word
        #         #     if flag == "an" or flag == "n" or flag == "vn":
        #         #         wordList.append(word)
        #         #         wordCounter[word] += 1
        #         #print type(seg)
        #         #print seg
        #         for word in seg:
        #             wordList.append(word)
        #             wordCounter[word] += 1
        seg = j.cut(poemFile)
        for word in seg:
            wordList.append(word)
            wordCounter[word] += 1
        return wordList, wordCounter

    def PoemWord(self, poemFile, outputFile):
        res, resnum = self.PoemSegment(poemFile)
        #print type(resnum)
        word = dict(resnum)
        #print "{} items".format(len(word)) 402663
        count = sorted(word.items(),key=lambda item:item[1],reverse=True)
        with open(outputFile, 'w') as o:
            o.write(count)
        return count

    #TODO prefer to write items as utf-8 and in order


if __name__ == '__main__':
    jieba = jieba()
    poem = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/allpoems.txt"
    poemWord = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/output.txt"
    count = jieba.PoemWord(poem, poemWord)

    print type(count)

    for i in count:
        print "word: {}, times: {}".format(i[0].encode("utf-8"),i[1])
