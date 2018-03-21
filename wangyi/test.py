# coding: utf-8
import re
import jieba
from collections import Counter

lyric = "[by:春晓酱]\n[00:09.930]我素来寡言少语\n[00:18.030]若不是说予你听，我便无话可说\n[00:27.030]但我将为你唱情歌，直到生命的尽头\n[00:33.930]因为我的感觉\n[00:37.330]无法隐瞒\n[00:43.030]当你难过时，我会为你吟唱一首甜蜜的小夜曲\n[00:51.330]每晚入睡前，我还会为你哼上一首摇篮曲\n[01:00.030]有生之年，你都会听到我为你歌唱\n[01:07.330]因为我实在无法隐瞒自己的感觉\n[01:13.030]是的，我无处隐藏这种感觉\n"
lyric = lyric.decode("utf-8")

# lyricList = lyric.split("\n")
# for lrc in lyricList:
#     if lrc[0:3] == "[by":
#         continue
#     lrc = re.sub("([0-9])", "",lrc)
#     lrc = lrc.replace("[:.]","")
#     with open ("lyrictest.txt",'a') as l:
#         l.write(lrc.encode("utf-8"))
#         l.write("\n")
#     print lrc

wordList = []
wordCounter = Counter()
with open ("lyrictest.txt","r") as f:
    for line in f.readlines():
        #print line
        seg = jieba.cut(line)
        #print "/".join(seg)
        for word in seg:
            print word
            wordList.append(word)
            wordCounter[word] += 1
            
wordList = list(set(wordList))
print wordList
print wordCounter
for i in wordList:
    print "word:{} times:{}".format(i.encode("utf-8"), wordCounter[i])
