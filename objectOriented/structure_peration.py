class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def info(self):
        print(self.x, self.y)

if __name__ == '__main__':
    pa = Point(1, 2)
    pb = Point(3, 4)
    pc = pa+pb
    pc.info()