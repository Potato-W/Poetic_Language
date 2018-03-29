import os
import jieba as j
from collections import Counter

class jieba:
    def __init__(self):
        pass

    def PoemSegment(self, poemFile):
        wordList = []
        wordCounter = Counter()
        with open (poemFile, "r") as f:
            for line in f.readlines():
                #print line
                seg = j.cut(line)
                # seg = pseg.cut(line)
                #print "/".join(seg)
                # for word,flag in seg:
                #     # print word
                #     if flag == "an" or flag == "n" or flag == "vn":
                #         wordList.append(word)
                #         wordCounter[word] += 1
                for word in seg:
                    wordList.append(word)
                    wordCounter[word] += 1
        wordList = list(set(wordList))
        word = {}
        for i in wordList:
            word[i] = wordCounter[i]
            count = sorted(word.items(),key=lambda item:item[1],reverse=True)
        # for i in count:
        #     print "word: {}, times: {}".format(i[0].encode("utf-8"),i[1])
        return count


if __name__ == '__main__':
    poem = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/allpoems.txt"
    print poem
    jieba = jieba()
    res = jieba.PoemSegment(poem)
    for i in res:
        print "word: {}, times: {}".format(i[0].encode("utf-8"),i[1])
