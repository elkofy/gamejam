import colors

class object:
    def __init__(self, color):
        self.color = color

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

a = object(colors.CYAN)
b = object(colors.RED)
c = object(colors.GREEN)
d = object(colors.YELLOW)
e = object(colors.BLUE)

objArr = [a, b, c, d, e]