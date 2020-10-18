import json

f = open("facebook_combined.txt")
'''line = f.readline()
while line:
    print (line)
    
    line = f.readline()

    line.splitlines
'''

lines = f.read()
str_lines = lines.split()

for i in range(0, len(str_lines)): 
    str_lines[i] = int(str_lines[i]) 

str_lines = sorted(list(dict.fromkeys(str_lines)))

#print(str_lines.count)
#print(str_lines)


nodes = []

for i in str_lines: 
    nodeDic = { }
    nodeDic["name"] = i
    nodeDic["label"] = str(i)
    nodes.append(nodeDic)
 
with open('facebookNodeNew.json', 'w') as outfile:
    json.dump(nodes, outfile)
 

 
f.close()



'''
f = open("facebook_combined.txt")
Links = []

line = f.readline()
while line:   
    l2 = line.split()
    
    sourceIndex = str_lines.index(int(l2[0]))
    targetIndex = str_lines.index(int(l2[1]))    
    linkDic = { }
    linkDic[from] = sourceIndex
    linkDic[to] = targetIndex
    Links.append(linkDic)

    line = f.readline()


 
with open('facebookLinks.json', 'w') as outfile:
    json.dump(Links, outfile)
'''