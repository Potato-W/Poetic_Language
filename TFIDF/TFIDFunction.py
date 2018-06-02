# coding:utf-8
import sys, os
def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)
jieba_path = "/Users/wcswang/Desktop/GraPro/Poetic_Language/Participle/jieba"
print jieba_path
add_path(jieba_path)
import jiebaFunction
process_path = "/Users/wcswang/Desktop/GraPro/Poetic_Language/"
add_path(process_path)
import preprocess
import IDFLoad

class TFIDF():
    def __init__(self, idf_path):
        self.idf_loader = IDFLoad.IDFLoader(idf_path)
        self.idf_freq = self.idf_loader.idf_freq
        self.mean_idf = self.idf_loader.mean_idf

    def extract_keywords(self, sentence, topK=20):    # 提取关键词
        # 过滤
        #seg_list = segment(sentence)
        jieba = jiebaFunction.jieba()
        seg_list, seg_count = jieba.PoemSegment(sentence)
        freq = {}
        for w in seg_list:
            freq[w] = freq.get(w, 0.0) + 1.0
        total = sum(freq.values())
        for k in freq:   # 计算 TF-IDF
            freq[k] *= self.idf_freq.get(k, self.mean_idf) / total
        tags = sorted(freq, key=freq.__getitem__, reverse=True)  # 排序
        if topK:
            return tags[:topK]
        else:
            return tags

idffile = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/idf.txt"
document = "/Users/wcswang/Desktop/GraPro/Poetic_Language/Bayes/database/sample/C00001/76.txt"
topK = 10
tdidf = TFIDF(idffile)
sentence = preprocess.Process(document)
print sentence
tags = tdidf.extract_keywords(sentence)
for tag in tags:
    print tag.encode('utf-8')
