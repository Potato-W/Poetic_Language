from flask import Flask, render_template,url_for,request,jsonify
import os
import random

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    css = url_for("static", filename="css")
    img = url_for("static",filename="img")
    return render_template("index.html", css=css, img=img)

def randomPoem():
    poem_file = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/json"
    files = os.listdir(poem_file)
    random.shuffle(files)
    new_file = poem_file + "/" + files[0]
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


@app.route("/random", methods=['GET', 'POST'])
def random():
    poem = randomPoem()
    return json.jsonify({"poem":poem})
