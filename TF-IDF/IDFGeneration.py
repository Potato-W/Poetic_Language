import math

idfFile = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/idf.txt"
knownFile = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/known.txt"

all_file = 57694

idf_frequents = []
with open(knownFile, 'r') as f:
    for item in f.readlines():
        item_list = item.split(":")
        #print len(item_list)
        item_name = str(item_list[0])
        item_time = int(item_list[1])
        idf_frequents.append([item_name,item_time])
        #print item_name, item_time
print idf_frequents

with open(idfFile, 'w') as f:
    for item in idf_frequents:
        f.write(item[0] + ' ' + str(math.log(all_file/item[1], 2)) + '\n')
