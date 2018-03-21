# coding: utf-8
import requests
import json
import re
import time
import jieba
import jieba.posseg as pseg
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread
import numpy as np
from PIL import Image
import random

listID = # custom define
listURL = "https://api.imjad.cn/cloudmusic/?type=playlist&id=" + str(listID)

# get list
r = requests.get(listURL)
content = json.loads(r.content)
playList = content["playlist"]["tracks"]

print type(playList)
print playList[0].keys()
print len(playList)

def GetURL(url):
    r = requests.get(url)
    content = json.loads(r.content)
    # song's detail
    if "songs" in content:
        name = content["songs"][0]["ar"][0]["name"]
        return name
    # song's lyric
    if "lrc" in content:
        if "tlyric" in content:
            lyric = content["tlyric"]["lyric"]
        else:
            lyric = content["lrc"]["lyric"]
        return lyric

# process raw lyric
def CleanLyric(lyric):
    try:
        lyricList = lyric.split("\n")
        for lrc in lyricList:
            if lrc[0:3] == "[by":
                continue
            lrc = re.sub("([0-9])", "",lrc)
            lrc = lrc.replace("[:.]","")
            with open ("lyric.txt",'a') as l:
                l.write(lrc.encode("utf-8"))
                l.write("\n")
    except Exception as e:
        pass

# get song info
def GetSong():
    singer = []
    detailURL = "https://api.imjad.cn/cloudmusic/?type=detail&id="
    lyricURL = "https://api.imjad.cn/cloudmusic/?type=lyric&id="
    number = 0
    # write song into file ,if down for any reason, sleep 10s and try again
    while True:
        try:
            song = playList[number]
            print number
            songID = str(song["id"])
            # get singer
            print GetURL(detailURL + songID)
            singer.append(GetURL(detailURL + songID))
            # get lyric
            lyric = GetURL(lyricURL + songID)
            print lyric
            CleanLyric(lyric)
            number += 1
        except Exception as e:
            time.sleep(10)
        if number == 178:
            break

    # print singers sorted by times
    res = {}
    for i in singer:
        res[i] = singer.count(i)
        count = sorted(res.items(),key=lambda item:item[1],reverse=True)
    for i in count:
        print "singer: {}, times: {}".format(i[0].encode("utf-8"),i[1])

def AnalyzeSong():
    wordList = []
    wordCounter = Counter()
    with open ("lyric.txt","r") as f:
        for line in f.readlines():
            #print line
            # seg = jieba.cut(line)
            seg = pseg.cut(line)
            #print "/".join(seg)
            for word,flag in seg:
                # print word
                if flag == "an" or flag == "n" or flag == "vn":
                    wordList.append(word)
                    wordCounter[word] += 1
    wordList = list(set(wordList))
    word = {}
    for i in wordList:
        word[i] = wordCounter[i]
        count = sorted(word.items(),key=lambda item:item[1],reverse=True)
    for i in count:
        print "word: {}, times: {}".format(i[0].encode("utf-8"),i[1])
    return word


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
def DrawWordCloud(wordList):
    mask = np.array(Image.open("mask.png"))
    stopwords = set()
    stopwords.update(["是","让","会","能","去","有","做","要"])
    wc = WordCloud(background_color="white",
               max_words=1000,
               mask=mask,
               stopwords=stopwords,
               font_path = 'Light.ttc',
               min_font_size = 10,
               max_font_size = 30,
               random_state = 1
               )
    #wc.generate(wordList)
    wc.generate_from_frequencies(wordList)
    default_colors = wc.to_array()
    # plt.title("Custom colors")
    # plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
    #            interpolation="bilinear")
    wc.to_file("wordcloud.png")
    plt.axis("off")
    plt.figure()
    plt.title("Default colors")
    plt.imshow(default_colors, interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    #AnalyzeSong()
    wordList = AnalyzeSong()
    DrawWordCloud(wordList)





# get singer
# get
