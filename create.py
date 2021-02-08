import json
import random
import globals

f = open("levels/1.json", "w")

arr = []

for i in range(globals.GAME_HEIGHT):
    arr.append([])
    for j in range(globals.GAME_WIDTH):
        arr[i].append(random.randint(0, 4))

print(arr)
f.write(json.dumps(arr))