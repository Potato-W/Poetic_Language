import os,sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
# # known words txt
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
with open(unknownRawFile, 'rw') as f:
    for line in f.readlines():
        line = line.replace('(', '').replace(')', '')
        line = line.split(',', 1)
        line = line[0].decode('unicode-escape')
        line = line.replace('u','').replace('\'','')
        # print type(line)
        # print line
        res.append(line)
with open(unknownFile, 'w') as f:
    for i in res:
        print type(i)
        f.write(i)
        f.write('\n')
