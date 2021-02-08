import json
import random

f = open("levels/1.json", "w")

arr = []

for i in range(10):
    arr.append([])
    for j in range(20):
        arr[i].append(random.randint(0, 1))

print(arr)
f.write(json.dumps(arr))