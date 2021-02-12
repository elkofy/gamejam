import json
import globals

class Score():
    score = {}
    name = None

    def __init__(self, name):
        self.name = name
        f_levels = open("scores.json", "r")
        data = f_levels.read()
        self.score = json.loads(data)

    def add(self, score):
        self.score[self.name] = score
        f = open("scores.json", "w")
        f.write(json.dumps(self.score))
    
    def get(self):
        if globals.LOGS:
            print('get', self.name)
        if not self.name in self.score:
            return 0
        else:   
            return self.score[self.name]

