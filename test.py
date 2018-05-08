import os
import random
import json

poem_file = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/json"
files = os.listdir(poem_file)
#print files
random.shuffle(files)
#print files
new_file = poem_file + "/" + files[0]
print new_file
with open(new_file, 'r') as f:
    new_file = json.load(f)
    length = len(new_file)
    item_num = random.randint(0,length-1)
    item_title = new_file[item_num]["title"]
    item_author = new_file[item_num]["author"]
    item_paragraphs = new_file[item_num]["paragraphs"]
    item = [item_title, item_author, item_paragraphs]
    print item
    print item_num, item_title, item_author, item_paragraphs
