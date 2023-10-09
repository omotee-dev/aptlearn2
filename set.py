set1 = {"Omoteye", "Akinteye", "Samuel"}
#print(set1)

listnames= ["Omoteye", "Akinteye", "Samuel", "Omoteye"]
listname = set(listnames)
#print(listname)

set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3}
#print(set2 | set3)
#print(set2 & set3)
#print(set2 - set3)
#print(set2 ^ set3)
set2.add(6)
#print(set3)
#print(set2)
set1.update(set3)
print(set1)