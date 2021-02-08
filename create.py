import json

f = open("levels/1.json", "w")

arr = []

for i in range(10):
    arr.append([])
    for j in range(20):
        arr[i].append(j)

f.write(json.dumps(arr))