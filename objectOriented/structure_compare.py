class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.y > other.y

if __name__ == '__main__':
    pa = Point(0, 1)
    pb = Point(1, 0)
    print(pa < pb)
    print(pa > pb)