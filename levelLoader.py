import json

def loadLevel(num):
    f_levels = open("levels/" + str(num) + ".json", "r")

    data = f_levels.read()

    print("chargement monde " + str(num))
    return data
        

print(loadLevel(1))