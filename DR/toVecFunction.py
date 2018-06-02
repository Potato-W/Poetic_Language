#coding: utf-8
import os
import jieba as j
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
class toVec():
    def __init__(self):
        pass

    def generateFile(self, poem_file, words_file):
        poem_files = os.listdir(poem_file)
        save_file = open(words_file, 'w')
        for poem in poem_files:
            poem_ = poem_file + "/" + poem
            print poem_
            with open(poem_,'r') as f:
                for line in f.readlines():
                    wordList = []
                    seg = j.cut(line)
                    for word in seg:
                        wordList.append(word)
                    save_line = ' '.join(wordList).encode("utf-8")
                    save_file.write(save_line + '\n')
        save_file.close()

    def generateModel(self, words_file):
        #save_dir = os.path.dirname((words_file))
        vector_file = "/Users/wcswang/Desktop/GraPro/Poetic_Language/DR/word_vectors.model"

        if os.path.exists(vector_file):
            print('find word vector file, loading directly...')
            model = Word2Vec.load(vector_file)
        else:
            print('calculating word vectors...')
            model = Word2Vec(LineSentence(words_file), size=400, window=3, min_count=10,
                             workers=multiprocessing.cpu_count())
            # 将计算结果存储起来
            model.save(vector_file)
        return model

    def relativeWords(self,model,words):
        relative_words = {}
        print words
        for word in words:
            word_s = word.decode("utf-8")
            try:
                print model
                simular = model.most_similar(word_s)
                result =[item[0].encode("utf-8") for item in simular]
                relative_words[word] = result
            except Exception as e:
                print e
                print "ERROR:  WORD NOT IN VOCABULARY!"
                relative_words[word] = []
        return relative_words

    def generateLongtext(self,model,words):
        longtext = self.relativeWords(model,words)
        for k,v in longtext.items():
            k_lens = ""
            for i in v:
                k_lens = k_lens + i + " "
            longtext[k] = k_lens
        return longtext


if __name__ == '__main__':
    poem_file = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/txt"
    words_file = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/words.txt"
    Vec = toVec()
    #Word2Vec.generateFile(poem_file, words_file)
    model = Vec.generateModel(words_file)
    word = ["随","幽映","衣裳","白云","流水","闲门","落花","青春","道","读书"]
    words= Vec.relativeWords(model,word)
    longtext = Vec.generateLongtext(model, word)
    for k,v in longtext.items():
        print "{}:{}".format(k,v)
