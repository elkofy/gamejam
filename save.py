import json
import globals

class Save:

    levels = {}

    def __init__(self):
        f = open("save.json", "r")
        data = f.read()
        #print("JE SUIS ICICICICICICI")
        self.levels = json.loads(data)
        if globals.LOGS:
            print(self.levels)

    def get_lvl(self, name):
        if not name in self.levels:
            return 1
        else:
            return self.levels[name]
        
    def add(self, name, level):
        self.levels[globals.NAME] = globals.NUM_LVL
        if globals.LOGS:
            print(self.levels)
        f = open("save.json", "w")
        f.write(json.dumps(self.levels))


