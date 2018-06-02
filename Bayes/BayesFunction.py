#coding: utf-8
import os, sys
import time
import random
import jieba
import nltk
import sklearn
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
sys.path.append('../TFIDF')
import TFIDFunction
sys.path.append('../')
import preprocess


def MakeWordsSet(words_file):
    words_set = set()
    with open(words_file, 'r') as fp:
        for line in fp.readlines():
            word = line.strip().decode("utf-8")
            if len(word)>0 and word not in words_set: # 去重
                words_set.add(word)
    return words_set

def TextProcessing(folder_path, test_size=0.2):
    folder_list = os.listdir(folder_path)
    data_list = []
    class_list = []

    # 类间循环
    for folder in folder_list:
        new_folder_path = os.path.join(folder_path, folder)
        files = os.listdir(new_folder_path)
        #print "FILES: {}".format(files)
        # 类内循环
        j = 1
        for file in files:
            if j > 100: # 每类text样本数最多100
                break
            with open(os.path.join(new_folder_path, file), 'r') as fp:
               raw = fp.read()
            word_cut = jieba.cut(raw, cut_all=False) # 精确模式，返回的结构是一个可迭代的genertor
            word_list = list(word_cut) # genertor转化为list，每个词unicode格式
            data_list.append(word_list)
            class_list.append(folder.decode('utf-8'))
            j += 1

    ## 划分训练集和测试集
    # train_data_list, test_data_list, train_class_list, test_class_list = sklearn.cross_validation.train_test_split(data_list, class_list, test_size=test_size)
    data_class_list = zip(data_list, class_list)
    random.shuffle(data_class_list)
    index = int(len(data_class_list)*test_size)+1
    train_list = data_class_list[index:]
    test_list = data_class_list[:index]
    train_data_list, train_class_list = zip(*train_list)
    test_data_list, test_class_list = zip(*test_list)

    # 统计词频放入all_words_dict
    all_words_dict = {}
    for word_list in train_data_list:
        for word in word_list:
            if all_words_dict.has_key(word):
                all_words_dict[word] += 1
            else:
                all_words_dict[word] = 1
    # key函数利用词频进行降序排序
    all_words_tuple_list = sorted(all_words_dict.items(), key=lambda f:f[1], reverse=True) # 内建函数sorted参数需为list
    all_words_list = list(zip(*all_words_tuple_list)[0])
    #print all_words_list

    return all_words_list, train_data_list, test_data_list, train_class_list, test_class_list


def words_dict(all_words_list, deleteN, stopwords_set=set()):
    # 选取特征词
    feature_words = []
    n = 1
    for t in range(deleteN, len(all_words_list), 1):
        if n > 1000: # feature_words的维度1000
            break
        # print all_words_list[t]
        if not all_words_list[t].isdigit() and all_words_list[t] not in stopwords_set and 1<len(all_words_list[t])<5:
            feature_words.append(all_words_list[t])
            n += 1
    return feature_words


def TextFeatures(train_data_list, test_data_list, feature_words):
    def text_features(text, feature_words):
        text_words = set(text)
        ## sklearn特征 list
        features = [1 if word in text_words else 0 for word in feature_words]
        return features
    train_feature_list = [text_features(text, feature_words) for text in train_data_list]
    test_feature_list = [text_features(text, feature_words) for text in test_data_list]
    return train_feature_list, test_feature_list

class Bayes():
    def __init__(self):
        pass
    def classify(self,longtext):
        folder_path = '/Users/wcswang/Desktop/GraPro/Poetic_Language/Bayes/database/sample'
        all_words_list, train_data_list, test_data_list, train_class_list, test_class_list = TextProcessing(folder_path, test_size=0.2)
        stopwords_file = '/Users/wcswang/Desktop/GraPro/Poetic_Language/Bayes/stopwords_cn.txt'
        stopwords_set = MakeWordsSet(stopwords_file)
        deleteNs = range(0, 1000, 20)
        test_accuracy_list = []
        for deleteN in deleteNs:
            feature_words = words_dict(all_words_list, deleteN, stopwords_set)
            train_feature_list, test_feature_list = TextFeatures(train_data_list, test_data_list, feature_words)
        classifier = MultinomialNB().fit(train_feature_list, train_class_list)
        train_feature_list, predict_feature_list = TextFeatures(train_data_list, longtext, feature_words)
        class_typetmp = classifier.predict(predict_feature_list)[0]

        class_listfile = "/Users/wcswang/Desktop/GraPro/Poetic_Language/Bayes/database/classlist.txt"
        class_transfer = {}
        with open(class_listfile, 'r') as f:
            for line in f.readlines():
                l = line.split(" ")
                class_transfer[l[0]]=l[1]
        class_type = class_transfer[class_typetmp]
        return class_type



if __name__ == '__main__':

    print "start"

    idffile = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/idf.txt"
    predict_poem = "/Users/wcswang/Desktop/GraPro/Poetic_Language/Bayes/database/sample/C00001/76.txt"
    tfidf = TFIDFunction.TFIDF(idffile)
    sentence = preprocess.Process(predict_poem)
    tags = tfidf.extract_keywords(sentence)
    Bay = Bayes()
    class_type = Bay.classify(tags)
    print class_type
