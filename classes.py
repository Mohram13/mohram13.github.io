class Point():
    # Automatically be called every time that I triy to create a new poin/object
    # self reptesents the object in question.
    def __init__(self, inputx, inputy):
        self.x = inputx
        self.y = inputy

p =Point(2,8)
print(p.x)
print(p.y)
 