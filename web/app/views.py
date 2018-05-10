#coding: utf-8
from flask import Flask, render_template,url_for,request
from flask import jsonify,json
import os, sys
import random
import re
def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/", methods=['GET', 'POST'])
def index():
    css = url_for("static", filename="css")
    img = url_for("static",filename="img")
    js = url_for("static", filename="js")
    return render_template("index.html", css=css, img=img, js=js)

def randomPoem():
    poem_file = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/json"
    files = os.listdir(poem_file)
    random_num = random.randint(0,len(files)-1)
    new_file = poem_file + "/" + files[random_num]
    with open(new_file, 'r') as f:
        new_file = json.load(f)
        length = len(new_file)
        item_num = random.randint(0,length-1)
        item_title = new_file[item_num]["title"]
        item_author = new_file[item_num]["author"]
        item_paragraphs = new_file[item_num]["paragraphs"]
        item = [item_title, item_author, item_paragraphs]
        return item
        #print item_num, item_title, item_author, item_paragraphs

poem_item = []
keywords = []
poem_sentence = ""
@app.route("/poem", methods=['GET', 'POST'])
def poem():
    global poem_item
    poem_item = randomPoem()
    print "poem_item: {}".format(poem_item)
    return json.jsonify({"poem":poem_item})


@app.route("/word", methods=['GET','POST'])
def word():
    #tfidf_path = os.path.join(pwd,'../../','TF-IDF/')
    tfidf_path = "/Users/wcswang/Desktop/GraPro/Poetic_Language/TFIDF"
    print "[IMPORT TF-IDF FROM] {}".format(tfidf_path)
    add_path(tfidf_path)
    import TFIDFunction
    idffile = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/idf.txt"
    TFIDF = TFIDFunction.TFIDF(idffile)
    global poem_item
    poems = poem_item[2]
    global poem_sentence
    poem_sentence = ""
    for item in poems:
        poem_sentence += item
    poem_sentence = poem_sentence.encode("utf-8")
    print "before:{}".format(poem_sentence)
    poem_sentence = re.sub("，|。|？|（|）|【|】|{|}|《|》|-|“|”|！|：|□|〖|〗|[0-9]|[|]","",poem_sentence)
    print "after:{}".format(poem_sentence)
    global keywords
    keywords = TFIDF.extract_keywords(poem_sentence, 15)
    for keyword in keywords:
        #print type(keyword)
        print keyword.encode("utf-8")
        #print type(keyword.encode("utf-8"))
    return json.jsonify({"keywords":keywords})

@app.route("/longtext", methods=['GET','POST'])
def longtext():
    dr_path = "/Users/wcswang/Desktop/GraPro/Poetic_Language/DR"
    print "[IMPORT DR FROM] {}".format(dr_path)
    add_path(dr_path)
    import toVecFunction
    model_path = "/Users/wcswang/Desktop/GraPro/Poetic_Language/DR/word_vectors.model"
    Word2Vec = toVecFunction.toVec()
    global keywords
    print keywords
    new_keywords = []
    for keyword in keywords:
        # print type(keyword)
        # print keyword.encode("utf-8")
        # print type(keyword.encode("utf-8"))
        new_keywords.append(keyword.encode("utf-8"))
    model = Word2Vec.generateModel(model_path)
    results = Word2Vec.generateLongtext(model, new_keywords)
    return json.jsonify({"longtext":results,"poem":poem_sentence})

# @app.route("/type", methods=['GET','POST'])
