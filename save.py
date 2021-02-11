import json


def get_lvl(name):
    f_levels = open("score.json", "r")
    data = f_levels.read()
    return json.loads(data)[name]


def add(name, level):
    self.score[self.name] = score
    f = open("score.json", "rw")
    data = f_levels.read()
    levels = json.loads(data)
    levels[name] = level
    f.write(json.dumps(levels))

