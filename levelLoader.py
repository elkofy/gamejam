import json

def loadLevel(num):
    f_levels = open("levels/" + str(num) + ".json", "r")

    data = f_levels.read()
    lvl = json.loads(data)

    print("chargement monde " + str(num))

    return lvl        

print(loadLevel(1))