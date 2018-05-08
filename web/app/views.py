from flask import Flask, render_template,url_for,request
from flask import jsonify,json
import os
import random

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


@app.route("/poem", methods=['GET', 'POST'])
def poem():
    poem_item = randomPoem()
    print "poem_item: {}".format(poem_item)
    return json.jsonify({"poem":poem_item})

# @app.route("/word", methods=['GET','POST'])
#
# @app.route("/longtext", methods=['GET','POST'])
#
# @app.route("/type", methods=['GET','POST'])
