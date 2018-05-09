from lxml import etree
import requests
import os

def get_pages(key):
    url_base = "https://www.gushiwen.org/shiwen/"
    #key = "default_1A3A1"
    url = url_base+key + ".aspx"
    res = requests.get(url)
    res.encoding = 'utf-8'
    return res

def spider(res):
    #print(res.text)
    root = etree.HTML(res.content)
    # end_ = root.xpath('//div[@class="pages"]/span[@style="color:#65645F; background-color:#E1E0C7; border:0px; width:auto;"]')[0]
    # end_ = end_.xpath('string(.)').encode("utf-8")
    # end = 50 if end_ > 50 else end_
    # print "end: {}".format(end)
    items = root.xpath('//div[@class="sons"]/div[@class="cont"]/div[@class="contson"]')
    return items


if __name__ == '__main__':
    classlist = []
    classfile = "/Users/wcswang/Desktop/GraPro/Poetic_Language/Bayes/database/classlist.txt"
    with open(classfile, 'r') as f:
        for line in f.readlines():
            classlist.append(line.split(' '))
    print "classlist: {}".format(classlist)
    #checklist(classlist)
    for item in classlist:
        class_num = item[0]
        class_key = item[2][:-7]
        print "class_key: {}".format(class_key)
        class_path = "/Users/wcswang/Desktop/GraPro/Poetic_Language/Bayes/database/sample/"
        class_path = class_path + class_num
        if not os.path.exists(class_path):
            os.mkdir(class_path)
        class_item_num = 0
        for i in range(1,11):
            class_key_ = class_key + str(i)
            res = get_pages(class_key_)
            try:
                items = spider(res)
                print items
                for item in items:
                    item = item.xpath('string(.)').encode("utf-8")
                    item_path = class_path + "/" + str(class_item_num) + ".txt"
                    #print "store in "
                    with open(item_path, 'w') as f:
                        f.write(item)
                    class_item_num = class_item_num + 1
                print "[DONE PAGE {}, ALL 10 PAGES]".format(i)
            except Exception as e:
                print e

        print "[DONE CLASS {}]".format(class_num)
