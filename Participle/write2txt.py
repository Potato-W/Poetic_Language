import os,sys
import json
import math
reload(sys)
sys.setdefaultencoding('utf-8')
# known words txt
# knownRawFile = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/output.json"
# knownFile = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/known.txt"
# with open(knownRawFile, 'r') as f:
#     knownRawdata = json.load(f)
#
# knownRawdata = sorted(knownRawdata.items(), key = lambda item:item[1], reverse=True)
# with open(knownFile, 'w') as f:
#     for data in knownRawdata:
#         print data[0], data[1]
#         item = str(data[0].encode("utf-8")) + ":" + str(data[1])
#         f.write(item)
#         f.write("\n")

# unkown words txt
unknownRawFile = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/entropyres.txt"
unknownFile = "/Users/wcswang/Desktop/GraPro/Poetic_Language/poem/unknown.txt"

res = []
all_file = 57649
with open(unknownRawFile, 'rw') as f:
    for line in f.readlines():
        line = line.replace('(', '').replace(')', '')
        line = line.split(',', 1)
        line_name = line[0].decode('unicode-escape')
        line_name = line_name.replace('u','').replace('\'','')
        line_para = str(line[1]).replace('[', '').replace(']', '')
        line_para = line_para.split(',')
        line_time = int(line_para[0])
        # print line_time
        # print type(line)
        # print line
        res.append([line_name, line_time])
with open(unknownFile, 'w') as f:
    for item in res:
        #print type(i)
        f.write(item[0] + ' ' + str(math.log(all_file/item[1], 2)) + '\n')
