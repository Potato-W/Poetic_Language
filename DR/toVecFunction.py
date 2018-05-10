#coding: utf-8
class toVec():
    def __init__(self):
        pass

    def generateModel(self, words_file):
        save_dir = os.path.dirname((words_file))
        vector_file = "/Users/wcswang/Desktop/GraPro/Poetic_Language/DR/word_vectors.model"

        if os.path.exists(vector_file):
            print('find word vector file, loading directly...')
            model = Word2Vec.load(vector_file)
        else:
            print('calculating word vectors...')
            model = Word2Vec(LineSentence(words_file), size=400, window=3, min_count=10,
                             workers=multiprocessing.cpu_count())
            # 将计算结果存储起来，下次就不用重新计算了
            model.save(vector_file)
        return model

    def Word2Vec(self,word):

        return words
    def generateLongtext(self):
        return longtext
